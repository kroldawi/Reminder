from flask import render_template, url_for, redirect

from app.blueprints.events import bp
from app.blueprints.events.daos import EventsDao
from app.blueprints.events.forms import AddEventForm, DeleteEventForm


DAO = EventsDao()

@bp.route('/add_event', methods = ['GET', 'POST'])
def add_event():
    add_form = AddEventForm()
    delete_form = DeleteEventForm()

    if add_form.validate_on_submit():
        DAO.add_event({'name': add_form.name.data \
            , 'when': add_form.when.data \
            , 'recurring': add_form.recurring.data})
        return redirect(url_for('index'))

    return render_template('events.html' \
        , add_form = add_form \
        , delete_form = delete_form \
        , events = DAO.get_all_events())


@bp.route('/delete_event/<int:id>', methods=['POST'])
def delete_event(id):
    DAO.delete_event(id)
    return redirect(url_for('add_event'))
