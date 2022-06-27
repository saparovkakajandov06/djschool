# 3rd party library
import uuid as UID

# Django
from django.conf import settings
from django.db import models
from django.urls import reverse     # NOQA: import in other models
from django.utils import timezone
from django.utils.translation import gettext as _

# local Django
from backend.authuser.models import User

## Custom middleware
from ..middleware import local

__all__ = ['BaseModel', 'BLANK', 'NULL_AND_BLANK', 'UID']


## Custom constants
NULL_AND_BLANK = {'blank': True, 'null': True}
BLANK = {'blank': True}


class BaseModel(models.Model):
    """ 
    Base Model 
    """

    created_at = models.DateTimeField(_('created_at'), default=timezone.now)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)
    author_fk = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  verbose_name=_('creator'),
                                  null=True,
                                  on_delete=models.CASCADE)

    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        """
        Custom method: Set creator name on save process
        """
        from django.contrib.auth.models import AnonymousUser

        # If record new and user exist
        if self.pk is None and hasattr(local, 'user'):
            self.author_fk = local.user
        
        elif self.pk is None:
            user = User.objects.filter(is_superuser=True)
            if user.exists():
                self.author_fk_id = user.first().pk
            else:
                self.author_fk = AnonymousUser()

        return super(BaseModel, self).save(*args, **kwargs)
