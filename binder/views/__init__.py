from .home import home
from .fail import fail
from .success import success
from .auth.logout import logout_user
from .auth.reg_form import reg_form
from .notes.new_note import new_note
from .notes.existing_note import existing_note, existing_note_pt2
from .notes.write_note import write_note
from .notes.note_details import note_details
from .lists.seasons import season_list
from .lists.classes import class_list
from .lists.notes import note_list
from .manage_forms.seasons import add_season
from .manage_forms.classes import add_class
from .manage_forms.notes import add_note
from .search.search import get_search, handle_search