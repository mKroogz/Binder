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
            n.content
        FROM binder_note AS n
        WHERE n.id = ?
        """, (note_id,))

        response = db_cursor.fetchone()
        note = Note()
        note.id = response[0]
        note.name = response[1]
        note.content = response[2]

        return note

def update_note(note_id, content):
    with sqlite3.connect(Connection.db_path) as conn:
                    db_cursor = conn.cursor()
                    db_cursor.execute("""
                    UPDATE binder_note
                    SET content = ?
                    WHERE id = ?
                    """,
                    (
                        content, note_id,
                    ))

def write_note(request, note_id):
    if request.method == 'GET':
        note = get_note(note_id)
        template = 'notes/write_note.html'
        context = {
            'note': note
        }
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        if(
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            school_class = form_data["class_id"]
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM binder_note
                WHERE id = ?
                """, (note_id,))

            return redirect(reverse('binder:note_list', kwargs={'school_class': school_class}))

        else:
            content = form_data['content']
            update_note(note_id, content)

        return redirect(reverse('binder:note_details', kwargs={'note_id': note_id}))
