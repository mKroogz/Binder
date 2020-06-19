import sqlite3
from datetime import datetime
from django.shortcuts import render, redirect, reverse
from binder.models import Season, SchoolClass, model_factory
from ..connection import Connection

def get_seasons(user):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Season)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            s.id,
            s.name
        from binder_season s
        WHERE s.user_id = ?
        """, (user,))

        return db_cursor.fetchall()

def get_classes(season):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(SchoolClass)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            s.id,
            s.name
        from binder_schoolclass s
        WHERE s.season_id = ?
        """, (season,))

        return db_cursor.fetchall()

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

def existing_note(request):
    if request.method == 'GET':
        user_id = request.user.id
        seasons = get_seasons(user_id)
        template = 'notes/existing_note_form.html'
        context = {
            'all_seasons': seasons
        }
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        season = form_data['season_id']

        return redirect(reverse('binder:existing_note_pt2', kwargs={'season': season}))

def existing_note_pt2(request, season):
    if request.method == 'GET':
        user_id = request.user.id
        classes = get_classes(season)
        template = 'notes/existing_note_form.html'
        context = {
            'all_classes': classes,
            'season': season
        }
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        user_id = request.user.id
        sclass = form_data['class_id']
        build_note(form_data['note'], user_id, sclass)

        return redirect(reverse('binder:success'))