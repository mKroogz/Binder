import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from datetime import datetime
from ..connection import Connection

def reg_form(request):
    if request.method == 'GET':
        template = 'registration/reg_form.html'
        return render(request, template)
    
    elif request.method == 'POST':
        form_data = request.POST
        user = User.objects.create_user(form_data['first_name'], form_data['email'], form_data['password'])

        user.first_name = form_data['first_name']
        user.last_name = form_data['last_name']
        user.username = form_data['username']
        user.save()

        return redirect(reverse('binder:login'))