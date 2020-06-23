import sqlite3
from datetime import datetime
from django.shortcuts import render, redirect, reverse
from binder.models import Note, model_factory
from ..connection import Connection

def add_note(request, school_class):
    if request.method == 'GET':
        template = 'manage_forms/notes.html'
        context = {
            'school_class': school_class
        }
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        user = request.user.id
        note = form_data["name"]
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO binder_note
            (
                name, user_id, school_class_id, date
            )
            VALUES (?, ?, ?, ?)
            """,
            (note, user, school_class, datetime.today()))


        return redirect(reverse('binder:note_list', kwargs={'school_class': school_class}))