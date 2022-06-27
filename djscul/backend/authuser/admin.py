# Django
from django.contrib import admin, messages
from django.contrib.admin.options import flatten_fieldsets
from django.contrib.auth.admin import UserAdmin as UserAdminBase

# local Django
from .models import *
from .forms import *


# -------------------
# >>>  User Admin <<<
# -------------------

# https://realpython.com/manage-users-in-django-admin/

class UserAdmin(UserAdminBase):
    """
    User Admin Model
    """

    model = User

    list_display = ('username', 'user_type', 'is_staff', 'is_active')
    
    list_filter = ('user_type', 'is_staff', 'is_active',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password', 'user_type'), }),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email'), }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        ('Authentication', {'fields': ('uuid_key', )}),
    )

    search_fields = ('username',)
    ordering = ('username',)


    # -= CLASS METHODS =-

    def get_form(self, request, obj=None, **kwargs):
        # Get parent form
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        # Protect superuser parameters from changes by non-superuser admin
        if not is_superuser:
            form.base_fields['username'].disabled = True
            form.base_fields['groups'].disabled = True
            form.base_fields['user_permissions'].disabled = True
            form.base_fields['is_active'].disabled = True
            form.base_fields['is_staff'].disabled = True
            form.base_fields['is_superuser'].disabled = True

        return form

# Re-register UserAdmin
admin.site.register(User, UserAdmin)


# ----------------------------
# >>>  UserAttribute Admin <<<
# ----------------------------

@admin.register(UserAttribute)
class UserAttributeAdmin(admin.ModelAdmin):
    """
    UserDataField Admin Model
    """
    
    # ListView: List of fields to be displayed
    list_display = ('att_name', 'user_type', 'att_type', 'att_len', 'att_info')


    # -= CLASS METHODS =-

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        # Show Model if superuser
        if request.user.is_superuser:
            return super().get_model_perms(request)

        return {}


# --------------------------------
# >>>  UserAttributeData Admin <<<
# --------------------------------

@admin.register(UserAttributeData)
class UserAttributeDataAdmin(admin.ModelAdmin):
    """
    UserDataValue Admin Model
    """
    
    # FormView: 
    fields = ['user_fk', 'attrib_fk', 'att_value', ]

    # ListView: List of fields to be displayed
    list_display = ('user_fk', 'attrib_fk', 'att_value', )

    # FormView: List of excluded fields from view
    exclude = ('created_at',)


    # -= CLASS METHODS =-

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        # Show Model if superuser
        if request.user.is_superuser:
            return super().get_model_perms(request)

        return {}


# -----------------------------
# >>>  USER RELATED MODELS  <<<
# -----------------------------

class PersonAdmin(admin.ModelAdmin):
    """
    Person Admin Model
    """
    
    # Custom declared properties
    user_type = 0
    new_fields = []

    # FormView: List of excluded fields from view
    #fields = ('first_name', 'last_name', 'email', 'dob', 'phone', 'mobile')

    #change_form_template='admin/authuser/student_change_form.html'
    
    form = PersonAdminForm

    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'dob', 'phone', 'mobile')}),
    )     


    # -= CLASS METHODS =-

    def get_fieldsets(self, request, obj=None):
        """
        Class method: Add additional fieldset
        """

        # Get model name attached to form
        child = self.model._meta.model_name
        # Save user_type list
        self.user_type = eval('UT_' + child.upper())

        # Get Model fieldset
        fieldsets  = super(PersonAdmin, self).get_fieldsets(request, obj)
        
        # Get list of fields name
        new_fields = []
        fields_rst = UserAttribute.objects.filter(user_type=self.user_type).only('att_name')
        
        # Prepare list of dynamic fields name
        for f in fields_rst:
            new_fields.append(f.att_name)

        # Save new fields list
        self.new_fields = new_fields     

        # Convert fieldset to list
        new_fieldsets = list(fieldsets)
        # Add new fieldset with dynamic fields
        new_fieldsets.append(['Addtional information', {'fields': new_fields}])
        
        return new_fieldsets


    def get_form(self, request, obj=None, **kwargs):
        """
        Class method: Add new added formset fields to form
        """

        # Set fieldsets as fields
        kwargs['fields'] = flatten_fieldsets(self.fieldsets)
        
        return super(PersonAdmin, self).get_form(request, obj, **kwargs)


    def save_model(self, request, obj, form, change):
        """
        # Create or update existing user data
        """
        
        # >>> All operation before create/update user data

        # Set user type
        obj.user_type = self.user_type

        # Get custom attribute for user
        cleaned_data = form.cleaned_data
                
        # Call parent save method
        super(PersonAdmin, self).save_model(request, obj, form, change)

        
        # >>> All operation after create/update user data
        
        fields = list(UserAttribute.objects.filter(user_type=self.user_type).only('pk', 'att_name'))
        fields = {row.att_name: row.pk for row in fields}

        data = []
        # Get custom fields and data
        for f in self.new_fields:
            
            dic = {
                'attrib_fk_id': fields[f],
                'att_value': cleaned_data.get(f, ''),
                'user_fk_id': obj.pk
            }
            
            # data.append(UserAttributeData(**dic))
            data.append(dic)

        # Create or update custom fields
        for row in data:
            # Prepare filter data
            flt = row.copy()
            # Remove field 'att_value'
            flt.pop('att_value')
            # Create or update exist record
            UserAttributeData.objects.update_or_create(**flt, defaults=row)


    # -= CUSTOM FIELDS =-

    def get_dob(self):
        return self.profile.dob;


# Register Student model with Person Admin
admin.site.register(Student, PersonAdmin)

admin.site.register(Parent, PersonAdmin)

admin.site.register(Teacher, PersonAdmin)
