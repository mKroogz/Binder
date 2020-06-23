from django.urls import path
from django.conf.urls import include
from binder import views
from .views import *

app_name = 'binder'
urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('fail/', fail, name='fail'),
    path('success/', success, name='success'),
    path('newnote/', new_note, name='new_note'),
    path('existingnote/', existing_note, name='existing_note'),
    path('existingnote/<int:season>', existing_note_pt2, name='existing_note_pt2'),
    path('search/', get_search, name='search'),
    path('search/<str:search>', handle_search, name='handle_search'),
    path('seasons/', season_list, name='season_list'),
    path('classes/<int:season>', class_list, name='class_list'),
    path('notes/<int:school_class>', note_list, name='note_list'),
    path('note/<int:note_id>', note_details, name='note_details'),
    path('write/<int:note_id>', write_note, name='write_note'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('login/', include('django.contrib.auth.urls'), name='login'),
    path('register/', reg_form, name='reg_form')
]