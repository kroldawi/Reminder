from flask import render_template, redirect, request, url_for

from app.blueprints.events import bp
from app.blueprints.events.daos import EventsDao, TagsDao
from app.blueprints.events.forms import AddEventForm, DeleteEventForm, FormFieldFactory


EVENTS_DAO = EventsDao()
TAGS_DAO = TagsDao()
FORM_FACTORY = FormFieldFactory()

@bp.route('/add_event', methods = ['GET', 'POST'])
def add_event():
    delete_form = DeleteEventForm()
    add_form = FORM_FACTORY.create_add_event_form(TAGS_DAO.get_tag_name_tuples())

    if add_form.validate_on_submit():
        EVENTS_DAO.add_event({'name': add_form.name.data \
            , 'when': add_form.when.data \
            , 'recurring': add_form.recurring.data \
            , 'tags': add_form.tags.data})
        return redirect(url_for('events.add_event'))

    return render_template('events.html' \
        , add_form = add_form \
        , delete_form = delete_form \
        , events = EVENTS_DAO.get_all_events())


@bp.route('/delete_event/<int:id>', methods=['POST'])
def delete_event(id):
    EVENTS_DAO.delete_event(id)

    return redirect(request.referrer)
