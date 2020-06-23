import sqlite3
from django.shortcuts import render, redirect, reverse
from binder.models import Season, model_factory
from ..connection import Connection

def add_season(request):
    if request.method == 'GET':
        template = 'manage_forms/seasons.html'
        context = {

        }
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        user = request.user.id
        season = form_data["name"]
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


        return redirect(reverse('binder:season_list'))