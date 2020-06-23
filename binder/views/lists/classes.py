import sqlite3
from django.shortcuts import render, redirect, reverse
from binder.models import SchoolClass, model_factory
from ..connection import Connection

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

def class_list(request, season):
    if request.method == 'GET':
        classes = get_classes(season)
        template = 'lists/classes.html'
        context = {
            'all_classes': classes,
            'season': season
        }
        return render(request, template, context)