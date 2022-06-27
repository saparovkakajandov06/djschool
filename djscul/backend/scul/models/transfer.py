# Django
from django.db import models
from django.utils.translation import gettext as _

# local Django
from core.loading import is_model_registered
from .base import BaseModel


__all__ = []


# -----------------------
# >>>  Transfer Model <<<
# -----------------------

if not is_model_registered('scul', 'Transfer'):
    
    class Transfer(BaseModel):

        trans_type = models.PositiveSmallIntegerField(
            _('transaction_type'),
            choices=((0, 'from-class-to-class'), (1, 'graduate'), (2, 'another-school')),
            default=0,
            help_text=_('transaction_type'))
        
        from_class = models.ForeignKey("scul.Classroom",
                                       verbose_name=_('from_class'),
                                       on_delete=models.PROTECT,
                                       related_name='cls_fromtrans')
        
        to_class = models.ForeignKey("scul.Classroom",
                                     verbose_name=_('to_class'),
                                     on_delete=models.PROTECT,
                                     related_name='cls_totrans')
        
        student_fk = models.ForeignKey("authuser.Student",
                                verbose_name=_('student'),
                                on_delete=models.PROTECT,
                                related_name='st_trans')

       
        class Meta:
            db_table = "scul_trans"
            verbose_name = "Transfer"
            verbose_name_plural = "Transfers"
            
            
        # Class Methods
        # -------------
        
        def __str__(self):
            """
            Return transfer name

            Returns:
                str: -
            """
            return "{}".format(self.get_trans_type_display)

        # Custom Functions
        # ----------------       


    __all__.append('Transfer')