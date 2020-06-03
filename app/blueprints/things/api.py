from flask import render_template, redirect, request, url_for
from datetime import datetime
from datetime import date, timedelta

from app.blueprints.things import bp
from app.blueprints.things.service import ThingsService
from app.blueprints.things.forms import DeleteThingForm, PurgeThingForm, FormFieldFactory


THINGS_SERVICE = ThingsService()
FORM_FACTORY = FormFieldFactory()

def get_cal(current_date):
    first_day = date(current_date.year, current_date.month, 1)
    first_day -= timedelta(days=first_day.isoweekday())
    
    return [[first_day + timedelta(days = i + j * 7) for i in range(7)] for j in range(6)]

@bp.route('/add_thing', methods = ['GET', 'POST'])
def add_thing():
    delete_form = DeleteThingForm()
    current_date = datetime.today()
    add_form = FORM_FACTORY.create_add_thing_form(THINGS_SERVICE.get_tag_name_tuples())

    if add_form.validate_on_submit():
        THINGS_SERVICE.add_thing(
                {'name': add_form.name.data, 'tags': add_form.tags.data})
        return redirect(url_for('things.add_thing'))
    
    return render_template('things.html' \
        , add_form = add_form \
        , delete_form = delete_form 
        , things = THINGS_SERVICE.get_undeleted_things() \
        , cal = get_cal(current_date) \
        , current_date = current_date \
        , holidays = THINGS_SERVICE.get_holiday_dates() \
        , events_this_month = THINGS_SERVICE.get_oncoming_event_dates())


@bp.route('/manage_things', methods = ['GET'])
def manage_things():
    delete_form = DeleteThingForm()
    purge_form = PurgeThingForm()
    current_date = datetime.today()

    return render_template('things_dictionary.html' \
        , delete_form = delete_form 
        , purge_form = purge_form
        , things = THINGS_SERVICE.get_all_things() \
        , cal = get_cal(current_date) \
        , current_date = current_date \
        , holidays = THINGS_SERVICE.get_holiday_dates() \
        , events_this_month = THINGS_SERVICE.get_oncoming_event_dates())


@bp.route('/delete_thing/<int:id>', methods = ['POST'])
def soft_delete_thing(id):
    THINGS_SERVICE.soft_delete_thing(id)
    
    return redirect(request.referrer)


@bp.route('/purge_thing/<int:id>', methods = ['POST'])
def hard_delete_thing(id):
    THINGS_SERVICE.hard_delete_thing(id)
    
    return redirect(request.referrer)