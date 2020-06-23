import sqlite3
from datetime import datetime
from django.shortcuts import render, redirect, reverse
from binder.models import Season
from ..connection import Connection


def season_check(season, user):
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                s.name
            FROM binder_season AS s 
            WHERE s.user_id = ?
        """, (user,))

        dataset = db_cursor.fetchall()

        for row in dataset:
            name = row[0]
            if name.upper().replace(" ", "") == season.upper().replace(" ", ""):
                return True
        
        return False

def build_season(season, user):
    with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO binder_season
            (
                name, user_id
            )
            VALUES (?, ?)
            """,
            (season, user))

            return db_cursor.lastrowid

def build_class(sclass, user, season):
    with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO binder_schoolclass
            (
                name, user_id, season_id
            )
            VALUES (?, ?, ?)
            """,
            (sclass, user, season))

            return db_cursor.lastrowid

def build_note(note, user, sclass):
    with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO binder_note
            (
                name, user_id, school_class_id, date
            )
            VALUES (?, ?, ?, ?)
            """,
            (note, user, sclass, datetime.today()))

            return db_cursor.lastrowid
            

def new_note(request):
    if request.method == 'GET':
        template = 'notes/new_note_form.html'
        context = {}
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        user_id = request.user.id
        check = season_check(form_data['season'], user_id)

        if check:
            return redirect(reverse('binder:fail'))

        season_id = build_season(form_data['season'], user_id)
        class_id = build_class(form_data['class'], user_id, season_id)
        note_id = build_note(form_data['note'], user_id, class_id)

        return redirect(reverse('binder:write_note', kwargs={'note_id': note_id}))