import sqlite3
from django.shortcuts import render, redirect, reverse
from binder.models import Season, model_factory
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

def season_list(request):
    if request.method == 'GET':
        user_id = request.user.id
        seasons = get_seasons(user_id)
        template = 'lists/seasons.html'
        context = {
            'all_seasons': seasons
        }
        return render(request, template, context)