from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('myprojects', views.myprojects, name='myprojects'),
    path('apply-leave', views.eleave, name='eleave'),
    path('leave-status', views.leavestatus, name='leavestatus'),
    path('submit', views.submit, name='submit'),
    path('updateinfo', views.updateinfo, name='updateinfo'),
]
