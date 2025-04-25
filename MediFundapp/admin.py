
from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from .models import Student
from .models import (
    Student, MedicalLead, User, Signup, raising_fund_info, patient_page_info, patient_story_info, fund_raising_form, Login
)
admin.site.register(Student)
admin.site.register(MedicalLead)
admin.site.register(User)
admin.site.register(Signup)
admin.site.register(raising_fund_info)
admin.site.register(patient_page_info)
admin.site.register(patient_story_info)
admin.site.register(fund_raising_form)
admin.site.register(Login)

