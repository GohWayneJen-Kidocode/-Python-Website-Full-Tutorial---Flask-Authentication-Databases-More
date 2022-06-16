from . import db
from flask import render_template, Blueprint, request, flash, redirect,url_for
from flask_login import login_required, current_user
from .models import Note
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Your note is too short.', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Your note has been posted!', category='success')

    return render_template('home.html', user=current_user)

@views.route('/delete-note/<int:id>', methods=['GET'])
def delete_note(id):
    # note =  json.loads(request.data)
    # noteId = note['noteId']
    note = Note.query.get(id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            print('the record has been deleted ')

    return redirect(url_for('views.home'))