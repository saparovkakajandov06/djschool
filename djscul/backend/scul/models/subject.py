# Django
from django.db import models
from django.utils.translation import gettext as _

# local Django
from core.loading import is_model_registered
from .base import BaseModel, UID


__all__ = []


# ----------------------
# >>>  Subject Model <<<
# ----------------------

if not is_model_registered('scul', 'Subject'):
    
    class Subject(BaseModel):

        id = models.UUIDField(primary_key=True, default=UID.uuid4, editable=False)
        name = models.CharField(_('subject_name'), max_length=25)
        short = models.CharField(_("remark"), max_length=5)
        
        class Meta:
            db_table = "scul_subjects"
            verbose_name = "Subject"
            verbose_name_plural = "Subjects"
            
            
        # Class Methods
        # -------------

        def __str__(self):
            """
            Return subject name

            Returns:
                str: -
            """
            return "{}".format(self.name)
        
        
        # Custom Functions
        # ----------------       


    __all__.append('Subject')
