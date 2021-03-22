from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('about/', views.about_view, name = 'about'),
    path('contact/', views.contact_view, name= 'contact'),
    path('dates/', views.dates_view, name='dates'),
    path('call-for-paper/', views.callforpaper_view, name='callforpaper'),
    path('paper-submission/', views.papersubmission_view, name='papersubmission'),
    path('committee/', views.commitee_view, name='committee'),
    path('speakers/', views.speakers_view, name='speakers'),
    path('journal-publication/', views.journalPublication_view, name='journalPublication'),
]