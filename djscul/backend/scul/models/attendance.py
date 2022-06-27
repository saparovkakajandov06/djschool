# Django
from django.db import models
from django.utils.translation import gettext as _

# local Django
from core.loading import is_model_registered
from .base import BaseModel


__all__ = []


# -------------------------
# >>>  Attendance Model <<<
# -------------------------

if not is_model_registered('scul', 'Attendance'):
    
    class Attendance(BaseModel):

        student_fk = models.ForeignKey("authuser.Student",
                                verbose_name=_('student'),
                                on_delete=models.PROTECT,
                                related_name='stu_attends')
        subject_fk = models.ForeignKey("scul.Subject",
                                verbose_name=_('subject'),
                                on_delete=models.PROTECT,
                                related_name='sub_attends')        
               
        class Meta:
            db_table = "scul_attends"
            verbose_name = "Attendance"
            verbose_name_plural = "Attendances"
            
            
        # Class Methods
        # -------------

        def __str__(self):
            """
            Return attendance

            Returns:
                str: -
            """
            return "{}".format(self.name)
        
        
        # Custom Functions
        # ----------------       


    __all__.append('Attendance')
