<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('dashboard', views.dashboard, name='dashboard'),
]
=======
from django.urls import path, include

from .import views

urlpatterns = [
    path('', views.base, name='base'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('patientinfo/', views.patientinfo, name='patientinfo'),
    path('guardianinfo/',views.guardianinfo, name='guardianinfo'),
    path('doctorinfo/',views.doctorinfo, name='doctorinfo'),
    path('studentinfo/',views.studentinfo, name='studentinfo'),
    path('success/',views.success_page, name='success_page'),
    path('login/',views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('fund_raising', views.fund_raising, name='fund_raising'),
    path('fund_raising_form', views.fund_raising_form_view, name='fund_raising_form'),
    path('fundraising/', views.select_form_category, name='fundraising_category'),
    path('fundraising/medical/', views.medical_form, name='medical_form'),
    path('fundraising/ngo/', views.ngo_form, name='ngo_form'),
    path('fundraising/other/', views.other_form, name='other_form'),
    
]
>>>>>>> 8ae871f (Track untracked files)
