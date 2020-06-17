import sqlite3
from django.shortcuts import render, redirect, reverse
from binder.models import Season
from ..connection import Connection


def new_note(request):
    if request.method == 'GET':
        template = 'notes/new_note_form.html'
        context = {}
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        user_id = request.user.id
        print(user_id)

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO binder_season
            (
                name, user_id
            )
            VALUES (?, ?)
            """,
            (form_data['season'], user_id))

        return redirect(reverse('binder:login'))