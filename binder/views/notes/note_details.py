import sqlite3
from django.shortcuts import render, redirect, reverse
from binder.models import Note
from ..connection import Connection

def get_note(note_id):
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            n.id,
            n.name,
            n.content,
            n.school_class_id
        FROM binder_note AS n
        WHERE n.id = ?
        """, (note_id,))

        response = db_cursor.fetchone()
        note = Note()
        note.id = response[0]
        note.name = response[1]
        note.content = response[2]
        note.school_class_id = response[3]

        return note

def note_details(request, note_id):
    if request.method == 'GET':
        note = get_note(note_id)
        template = 'notes/note_details.html'
        context = {
            'note': note
        }
        return render(request, template, context)