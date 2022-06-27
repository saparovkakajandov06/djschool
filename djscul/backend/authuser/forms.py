# Django
from django import forms
from django.contrib.admin import widgets

# local Django
from .models import *
from .constants import *


__all__ = ['PersonAdminForm']


def get_attrib_data(user) -> dict:
    """
    # Get User attribute data
    """
    rst = UserAttributeData.objects.filter(user_fk_id=user).select_related('attrib_fk')
    dct = {row.attrib_fk.att_name: row.att_value for row in rst}

    return dct

# --------------------------
# >>>  Person Admin Form <<<
# --------------------------

class PersonAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        # Set initial parameters and add custom fields
        """
        # Call parent method
        super(PersonAdminForm, self).__init__(*args, **kwargs)
        
        # Set some field required
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['phone'].required = True

        # Declare new dictionary
        new_fields = {}

        # Get model name attached to form
        child = self._meta.model._meta.model_name
        self.user_type = eval('UT_' + child.upper())

        # Get list of dynamic field names 
        fields_rst = UserAttribute.objects.filter(user_type=self.user_type).only('att_name')
        for f in fields_rst:
            data_type = DATA_TYPE_CLASSES[f.att_type]
            # Get module name from dictionary
            model = eval(data_type['model'])
            # Get field type class from dictionary
            field = getattr(forms, data_type['class'])
            # Get widget type class from dictionary
            widget = getattr(model, data_type['widget'])

            att = {'widget': widget, 'required': False}
            if f.att_type == UAT_LIST:
                lst = f.att_info.split(',')
                dic = [(row, row) for row in lst]
                att.update({'choices': dic})

            new_fields[f.att_name] = field(**att)        

        # Expand current fields list with new  
        self.fields.update(new_fields)

        # Load data from database
        if self.instance.pk:
            data = get_attrib_data(self.instance.pk)         
            for row in data:
                self.fields[row].initial = data[row]

    def clean(self):
        """
        # Clean form data
        """
        from datetime import date

        cleaned_data = super(PersonAdminForm, self).clean().copy()
        for index in cleaned_data:
            if index == 'dob':
                continue
            
            # Chande data format if type is date
            if type(cleaned_data[index]) == date:
                cleaned_data[index] = cleaned_data[index].strftime("%d.%m.%Y")
            else:
                cleaned_data[index] = str(cleaned_data[index])

        return cleaned_data

    class Meta:
        fields = '__all__'
