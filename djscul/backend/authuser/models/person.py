# standard library
import random

# 3rd party library
from unidecode import unidecode

# Django
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

# local Django
from .user import *
from core.loading import is_model_registered
from backend.authuser.constants import *


__all__ = []


# -----------------------
# >>>  Person Manager <<<
# -----------------------

class PersonManager(BaseUserManager):
    
    user_type = 0

    def get_queryset(self):
        
        # Get model name attached to form
        child = self.model._meta.model_name
        self.user_type = eval('UT_' + child.upper())

        return super(PersonManager, self).get_queryset().filter(user_type=self.user_type)


# ----------------------------
# >>>  Student Proxy Model <<<
# ----------------------------

if not is_model_registered('authuser', 'Student'):
    class Student(User):

        objects = PersonManager()

        class Meta:
            proxy = True
            
        def __str__(self):
            return self.info

    __all__.append('Student')


# ---------------------------
# >>>  Parent Proxy Model <<<
# ---------------------------

if not is_model_registered('authuser', 'Parent'):
    class Parent(User):

        objects = PersonManager()

        class Meta:
            proxy = True

        def __str__(self):
            return self.info
        
    __all__.append('Parent')


# ----------------------------
# >>>  Teacher Proxy Model <<<
# ----------------------------

if not is_model_registered('authuser', 'Teacher'):
    class Teacher(User):

        objects = PersonManager()

        class Meta:
            proxy = True
            
        def __str__(self):
            return self.info

    __all__.append('Teacher')
