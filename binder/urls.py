from django.urls import path
from django.conf.urls import include
from binder import views
from .views import *

app_name = 'binder'
urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('login/', include('django.contrib.auth.urls'), name='login')
]