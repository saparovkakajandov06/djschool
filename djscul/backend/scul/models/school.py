# Django
from django.db import models
from django.utils.translation import gettext as _

# local Django
from core.loading import is_model_registered
from .base import BaseModel, UID


__all__ = []


# ----------------------
# >>>  Country Model <<<
# ----------------------

if not is_model_registered('scul', 'Country'):
    
    class Country(BaseModel):

        name = models.CharField(_('country_name'), max_length=30, unique=True)

        class Meta:
            db_table = "scul_countries"
            verbose_name = "Country"
            verbose_name_plural = "Countries"


        # Class Methods
        # -------------
                    
        def __str__(self):
            """
            Return country name

            Returns:
                str: -
            """
            return self.name

    __all__.append('Country')


# ---------------------
# >>>  School Model <<<
# ---------------------

if not is_model_registered('scul', 'School'):
    
    class School(BaseModel):

        id = models.UUIDField(primary_key=True, default=UID.uuid4, editable=False)
        name = models.CharField(_('name_of_school'), max_length=255)
        instit = models.CharField(_('educational_institution'), max_length=255)
        region = models.CharField(_('region_of_school'), max_length=255)
        
        country_fk = models.ForeignKey("scul.Country",
                                        verbose_name=_('country'),
                                        on_delete=models.PROTECT,
                                        related_name='cou_schools')

        class Meta:
            db_table = "scul_schools"
            verbose_name = "School"
            verbose_name_plural = "Schools"
            
            
        # Class Methods
        # -------------
        
        def __str__(self):
            """
            Return school name

            Returns:
                str: -
            """
            return "{} - {} ({})".format(self.name, self.instit, self.region)

        # Custom Functions
        # ----------------       


    __all__.append('School')