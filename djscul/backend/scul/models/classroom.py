# Django
from django.db import models
from django.utils.translation import gettext as _

# local Django
from core.loading import is_model_registered
from .base import BaseModel, UID


__all__ = []


# ------------------------
# >>>  Classroom Model <<<
# ------------------------

if not is_model_registered('scul', 'Classroom'):
    
    class Classroom(BaseModel):

        id = models.UUIDField(primary_key=True, default=UID.uuid4, editable=False)
        name = models.CharField(_('class_name'), max_length=50)
        year = models.PositiveSmallIntegerField(_('year'))        
        remark = models.CharField(_("remark"), max_length=100)
        
        is_local = models.BooleanField(_("is_local"))
        status = models.BooleanField(_("status"))
        
        school_fk = models.ForeignKey("scul.School",
                                        verbose_name=_('school'),
                                        on_delete=models.PROTECT,
                                        related_name='sch_classes')
        
        class Meta:
            db_table = "scul_classes"
            verbose_name = "Classroom"
            verbose_name_plural = "Classrooms"
            
            
        # Class Methods
        # -------------

        def __str__(self):
            """
            Return classroom name

            Returns:
                str: -
            """            
            return "{} ({}, {})".format(self.name, self.year, self.is_local)
        
        
        # Custom Functions
        # ----------------       


    __all__.append('Classroom')