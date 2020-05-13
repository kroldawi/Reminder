from flask import render_template, redirect, request, url_for
from datetime import datetime
from datetime import date, timedelta

from app.blueprints.events import bp
from app.blueprints.events.daos import EventsDao
from app.blueprints.events.service import EventsService
from app.blueprints.events.forms import AddEventForm, DeleteEventForm, FormFieldFactory


EVENTS_DAO = EventsDao()
EVENTS_SERVICE = EventsService()
FORM_FACTORY = FormFieldFactory()

def get_cal(current_date):
    first_day = date(current_date.year, current_date.month, 1)
    first_day -= timedelta(days=first_day.isoweekday())
    
    return [[first_day + timedelta(days = i + j * 7) for i in range(7)] for j in range(6)]

@bp.route('/add_event', methods = ['GET', 'POST'])
def add_event():
    delete_form = DeleteEventForm()
    current_date = datetime.today()
    add_form = FORM_FACTORY.create_add_event_form(EVENTS_SERVICE.get_tag_name_tuples())

    if add_form.validate_on_submit():
        EVENTS_DAO.add_event({'name': add_form.name.data \
            , 'when': add_form.when.data \
            , 'recurring': add_form.recurring.data \
            , 'tags': add_form.tags.data})
        return redirect(url_for('events.add_event'))

    return render_template('events.html' \
        , add_form = add_form \
        , delete_form = delete_form \
        , events = EVENTS_DAO.get_all_events() \
        , cal = get_cal(current_date) \
        , current_date = current_date \
        , holidays = EVENTS_DAO.get_this_month_holiday_dates() \
        , events_this_month = EVENTS_DAO.get_this_month_event_dates())


@bp.route('/delete_event/<int:id>', methods=['POST'])
def delete_event(id):
    EVENTS_SERVICE.delete_event(id)

    return redirect(request.referrer)
