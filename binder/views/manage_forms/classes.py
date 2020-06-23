import sqlite3
from django.shortcuts import render, redirect, reverse
from binder.models import SchoolClass, model_factory
from ..connection import Connection

def add_class(request, season):
    if request.method == 'GET':
        template = 'manage_forms/classes.html'
        context = {
            'season': season
        }
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        user = request.user.id
        school_class = form_data["name"]
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO binder_schoolclass
            (
                name, user_id, season_id
            )
            VALUES (?, ?, ?)
            """,
            (school_class, user, season))


        return redirect(reverse('binder:class_list', kwargs={'season': season}))