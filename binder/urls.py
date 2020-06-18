from django.urls import path
from django.conf.urls import include
from binder import views
from .views import *

app_name = 'binder'
urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('newnote/', new_note, name='new_note'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('login/', include('django.contrib.auth.urls'), name='login'),
    path('register/', reg_form, name='reg_form')
]