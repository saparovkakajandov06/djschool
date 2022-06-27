# Django
from django.contrib import admin

# local Django
from .models import *


# -------------------
# >>>  Base Admin <<<
# -------------------

class BaseAdmin(admin.ModelAdmin):
    """
    Base Admin Model
    """

    # FormView: List of excluded fields from view
    exclude = ('created_at', 'author_fk',)


# -------------------------
# >>>  Attendance Admin <<<
# -------------------------

class AttendanceAdmin(BaseAdmin):
    
    # Display Save button at top
    save_on_top = True


# ------------------------
# >>>  Classroom Admin <<<
# ------------------------

class ClassroomAdmin(BaseAdmin):
    
    # Display Save button at top
    save_on_top = True


# ----------------------
# >>>  Journal Admin <<<
# ----------------------

class JournalAdmin(BaseAdmin):
    
    # Display Save button at top
    save_on_top = True


# ---------------------
# >>>  School Admin <<<
# ---------------------

class SchoolAdmin(BaseAdmin):
    
    # Display Save button at top
    save_on_top = True


# ----------------------
# >>>  Session Admin <<<
# ----------------------

class SessionAdmin(BaseAdmin):
    
    # Display Save button at top
    save_on_top = True


# ----------------------
# >>>  Subject Admin <<<
# ----------------------

class SubjectAdmin(BaseAdmin):
    
    # Display Save button at top
    save_on_top = True


# -------------------
# >>>  Term Admin <<<
# -------------------

class TermAdmin(BaseAdmin):
    
    # Display Save button at top
    save_on_top = True


# -----------------------
# >>>  Transfer Admin <<<
# -----------------------

class TransferAdmin(BaseAdmin):
    
    # Display Save button at top
    save_on_top = True


# Register Student model with Person Admin
admin.site.register(Attendance, AttendanceAdmin)

admin.site.register(Classroom, ClassroomAdmin)

admin.site.register(Journal, JournalAdmin)

admin.site.register(School, SchoolAdmin)

admin.site.register(Session, SessionAdmin)

admin.site.register(Subject, SubjectAdmin)

admin.site.register(Term, TermAdmin)

admin.site.register(Transfer, TransferAdmin)
