# Django
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext as _


# local Django
from core.loading import is_model_registered
from .base import BaseModel, UID


__all__ = []


# -------------------
# >>>  Term Model <<<
# -------------------

if not is_model_registered('scul', 'Term'):
    
    class Term(BaseModel):

        id = models.UUIDField(primary_key=True, default=UID.uuid4, editable=False)
        name = models.CharField(_('term_name'), max_length=50)
        start_date = models.DateField(_("term_start_date"), auto_now=False, auto_now_add=False)
        end_date = models.DateField(_("term_end_date"), auto_now=False, auto_now_add=False)

        class Meta:
            db_table = "scul_terms"
            verbose_name = "Term"
            verbose_name_plural = "Terms"
            
            
        # Class Methods
        # -------------
        
        def __str__(self):
            """
            Return term name

            Returns:
                str: -
            """            
            return "{} ({} - {})".format(self.name, self.start_date, self.end_date)

        # Custom Functions
        # ----------------       


    __all__.append('Term')
    
    
# ----------------------
# >>>  Session Model <<<
# ----------------------

if not is_model_registered('scul', 'Session'):
    
    class Session(BaseModel):

        id = models.UUIDField(primary_key=True, default=UID.uuid4, editable=False)
        name = models.CharField(_('session_name'), max_length=50)
        
        class_fk = models.ForeignKey("scul.Classroom",
                                     verbose_name=_('classroom'),
                                     on_delete=models.PROTECT,
                                     related_name='c_sess')
        
        teacher_fk = models.ForeignKey("authuser.Teacher",
                                     verbose_name=_('teacher'),
                                     on_delete=models.PROTECT,
                                     related_name='tch_sess')
        
        term_fk = models.ForeignKey("scul.Term",
                                verbose_name=_('term'),
                                on_delete=models.PROTECT,
                                related_name='ter_sess')

        class Meta:
            db_table = "scul_sessions"
            verbose_name = "Session"
            verbose_name_plural = "Sessions"
            
            
        # Class Methods
        # -------------
        
        def __str__(self):
            """
            Return sessions name

            Returns:
                str: -
            """
            return self.name
        


        # Custom Functions
        # ----------------


    __all__.append('Session')
    

# Signals
# -------

@receiver(pre_save, sender=Session)
def generate_session_name(sender, instance, *args, **kwargs):
    """
    Generate session name

    Args:
        sender (models.Model): Session
        instance (object): record of Session
    """
    instance.name = "{} - {} ({})".format(instance.class_fk.name, instance.teacher_fk, instance.term_fk)
