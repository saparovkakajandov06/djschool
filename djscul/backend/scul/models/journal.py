# Django
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

# local Django
from core.loading import is_model_registered
from .base import BaseModel


__all__ = []


# ----------------------
# >>>  Journal Model <<<
# ----------------------

if not is_model_registered('scul', 'Journal'):
    
    class Journal(BaseModel):

        score = models.PositiveSmallIntegerField(_('subject_name'), default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
        score_type = models.PositiveSmallIntegerField(
            _('score_type'),
            choices=((0, _('daily')), (1, _('test')), (2, _('quarter')), (3, _('exam')), (4, _('annual'))),
            default=0,
            help_text=_('scor_type'))

        student_fk = models.ForeignKey("authuser.Student",
                                verbose_name=_('student'),
                                on_delete=models.PROTECT,
                                related_name='stu_scores')
        subject_fk = models.ForeignKey("scul.Subject",
                                verbose_name=_('subject'),
                                on_delete=models.PROTECT,
                                related_name='sub_scores')        
               
        class Meta:
            db_table = "scul_journals"
            verbose_name = "Journal"
            verbose_name_plural = "Journals"
            
            
        # Class Methods
        # -------------

        def __str__(self):
            """
            Return journal name

            Returns:
                str: -
            """
            return "{}".format(self.name)
        
        
        # Custom Functions
        # ----------------       


    __all__.append('Journal')
