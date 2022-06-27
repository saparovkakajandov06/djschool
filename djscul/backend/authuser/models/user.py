# standard library
import random

# 3rd party library
from unidecode import unidecode
import uuid


# Django
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# local Django
from backend.authuser.constants import *


__all__ = ['User', 'UserAttribute', 'UserAttributeData']


def generate_uuid() -> str:
    """
    # Generate a UUID.
    """
    return str(uuid.uuid4())


def generate_account_name(name, surname, phone):
    """
    # Generate unique username
    """
    
    # Generate username from name and surname
    username = "{0}{1}".format(name[0], surname).lower()
    username = unidecode(username)

    # If username is empty, set phone number 
    if not username:
        username = phone.replace('+', '').strip()

    # Generate unique username
    counter = 1
    while User.objects.filter(username=username):
        username = "{0}{1}".format(name[0], surname).lower() + str(counter)
        username = unidecode(username)
        counter  = '{:03d}'.format(random.randrange(1, 999))

    return username


# -------------------
# >>>  User Model <<<
# -------------------

class User(AbstractUser):
    """
    Substituting a custom User model
    """
    
    uuid_key = models.CharField(max_length=100, default=generate_uuid, db_index=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=UT_NAN)

    dob = models.DateField(_("Date of birth"), blank=True, null=True)
 
    phone_rex = RegexValidator(regex=r'^(?:\+993)?[ ]?(?:\([1-5]?[1-5]{2,3}\)[ .-]?[0-9]{1}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|[1-5]?[1-5]{2,3}[ .-]?[0-9]{1}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|[1-5]?[1-5]{2,3}[0-9]{5,6})$'
        , message="Phone number must be entered in the format: '+993 131 99999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_rex], max_length=15, blank=True)

    mobile_rex = RegexValidator(regex=r'^(?:\+993)?[ ]?(?:\(6[1-5]?\)[ .-]?[0-9]{2}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|6[1-5]?[ .-]?[0-9]{2}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|6[1-5]?[0-9]{6})$'
        , message="Phone number must be entered in the format: '+993 61 999999'. Up to 15 digits allowed.")
    mobile = models.CharField(validators=[mobile_rex], max_length=15, blank=True)

    @property
    def info(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.phone)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        
        # If new created user set username and password
        if self.pk is None and self.username is None:
            self.username = generate_account_name(self.first_name, self.last_name, self.phone)
            self.password = '12345'

        super(User, self).save(*args, **kwargs)


# ----------------------------
# >>>  UserAttribute Model <<<
# ----------------------------

class UserAttribute(models.Model):
    """
    The User Attribute table contains additional user fields.
    """

    user_type = models.PositiveSmallIntegerField(verbose_name='User', choices=USER_TYPE_CHOICES, default=UT_NAN) 
    att_name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)       
    att_type = models.PositiveSmallIntegerField(verbose_name=_("Type"), choices=DATA_TYPE_CHOICES, default=UAT_INT)
    att_len = models.PositiveSmallIntegerField(verbose_name=_("Length"), blank=True, default=0)
    att_info = models.CharField(verbose_name=_("Info"), 
        help_text=_("Set model name if type is relation"), 
        max_length=25, blank=True)

    class Meta:
        db_table = 'auth_user_attribute'
        verbose_name = _("User Attribute")
        verbose_name_plural = _("User Attributes")

    def __str__(self):
        return self.att_name


# --------------------------------
# >>>  UserAttributeData Model <<<
# --------------------------------

class UserAttributeData(models.Model):
    """
    The User Attribute Data table holds data of each additional user fields.
    """

    att_value = models.CharField(verbose_name=_("Attribute Value"), help_text=_("User Attribute Value"), max_length=255)
    created_at = models.DateTimeField(verbose_name='Created at', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    user_fk = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name="fields_data")
    attrib_fk = models.ForeignKey(UserAttribute, verbose_name=_("Attribute name"), on_delete=models.RESTRICT)   


    @property
    def attribute(self):
        return '{}: {}'.format(self.attrib_fk.att_name, self.att_value)

    class Meta:
        db_table = 'auth_ud_value'
        verbose_name = _("User Attribute value")
        verbose_name_plural = _("User Attribute values")

    def __str__(self):
        return self.att_value
