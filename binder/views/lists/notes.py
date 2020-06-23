import sqlite3
from django.shortcuts import render, redirect, reverse
from binder.models import Note, model_factory
from ..connection import Connection

def get_notes(school_class):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Note)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            n.id,
            n.name
        from binder_note n
        WHERE n.school_class_id = ?
        """, (school_class,))

        return db_cursor.fetchall()

def note_list(request, school_class):
    if request.method == 'GET':
        notes = get_notes(school_class)
        template = 'lists/notes.html'
        context = {
            'all_notes': notes,
            'school_class': school_class
        }
        return render(request, template, context)