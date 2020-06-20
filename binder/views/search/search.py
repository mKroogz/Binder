import sqlite3
from django.shortcuts import render, redirect, reverse
from binder.models import Note, SchoolClass, model_factory
from ..connection import Connection

def get_notes(user):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Note)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            n.id,
            n.name
        from binder_note n
        WHERE n.user_id = ?
        """, (user,))

        return db_cursor.fetchall()

def get_classes(user):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(SchoolClass)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            s.id,
            s.name
        from binder_schoolclass s
        WHERE s.user_id = ?
        """, (user,))

        return db_cursor.fetchall()

def get_matches(dataset, search):
    all_matches = []
    for match in dataset:
        if search.upper() in match.name.upper():
            all_matches.append(match)
        elif search == "showall":
            all_matches.append(match)
    
    return all_matches

def get_search(request):
    if request.method == 'GET':
        template = 'search/search.html'
        context = {
        }
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        search = form_data['searchfield']
        if search == "":
            search = "showall"

        return redirect(reverse('binder:handle_search', kwargs={'search': search}))

def handle_search(request, search):
    if request.method == 'GET':
        user_id = request.user.id
        classes = get_classes(user_id)
        matched_classes = get_matches(classes, search)
        notes = get_notes(user_id)
        matched_notes = get_matches(notes, search)
        template = 'search/search.html'
        context = {
            'all_classes': matched_classes,
            'all_notes': matched_notes
        }
        return render(request, template, context)
