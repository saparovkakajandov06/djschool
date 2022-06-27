# >>>  Constants <<<
# ------------------


__all__ = ['UT_NAN', 'UT_STUDENT', 'UT_PARENT', 'UT_TEACHER', 
            'UAT_INT', 'UAT_STR', 'UAT_DATE', 'UAT_LIST', 'UAT_LINK', 
            'USER_TYPE_CHOICES', 'DATA_TYPE_CHOICES', 'DATA_TYPE_CLASSES']

# > Type of user
from django.forms import widgets


UT_NAN = 1
UT_STUDENT = 2
UT_PARENT = 3
UT_TEACHER = 4

# > User Attribute types
UAT_INT = 0     # Integer
UAT_STR = 1     # Char 
UAT_DATE = 2    # Date
UAT_LIST = 5    # Choices
UAT_LINK = 6    # Foreign key

# > Set of user type
USER_TYPE_CHOICES = (
    (UT_NAN, 'none'),
    (UT_STUDENT, 'student'),
    (UT_PARENT, 'parent'),
    (UT_TEACHER, 'teacher'),
)

# > Set of attribute type
DATA_TYPE_CHOICES = (
    (UAT_INT, 'Int'),
    (UAT_STR, 'String'),
    (UAT_DATE, 'Date'),
    (UAT_LIST, 'Static list'),
    (UAT_LINK, 'Relation'),
)

DATA_TYPE_CLASSES = {
    UAT_INT: { 'class': 'IntegerField', 'model': 'forms', 'widget': 'NumberInput'},
    UAT_STR: { 'class': 'CharField', 'model': 'forms', 'widget': 'TextInput'},
    UAT_DATE: { 'class': 'DateField', 'model': 'widgets', 'widget': 'AdminDateWidget'},
    UAT_LIST: { 'class': 'ChoiceField', 'model': 'forms', 'widget': 'Select'},
    UAT_LINK: { 'class': 'ModelChoiceField', 'model': 'forms', 'widget': 'Select'},
}
