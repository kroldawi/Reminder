from flask import render_template, redirect, request, url_for
from datetime import datetime
from datetime import date, timedelta

from app.blueprints.things import bp
from app.blueprints.things.daos import ThingsDao, TagsDao
from app.blueprints.things.forms import DeleteThingForm, FormFieldFactory


THINGS_DAO = ThingsDao()
TAGS_DAO = TagsDao()
FORM_FACTORY = FormFieldFactory()

def get_cal(current_date):
    first_day = date(current_date.year, current_date.month, 1)
    first_day -= timedelta(days=first_day.isoweekday())
    
    return [[first_day + timedelta(days = i + j * 7) for i in range(7)] for j in range(6)]

@bp.route('/add_thing', methods = ['GET', 'POST'])
def add_thing():
    delete_form = DeleteThingForm()
    current_date = datetime.today()
    add_form = FORM_FACTORY.create_add_thing_form(TAGS_DAO.get_tag_name_tuples())

    if add_form.validate_on_submit():
        THINGS_DAO.add_thing(
                {'name': add_form.name.data, 'tags': add_form.tags.data})
        return redirect(url_for('things.add_thing'))
    
    return render_template('things.html' \
        , add_form = add_form \
        , delete_form = delete_form 
        , things = THINGS_DAO.get_all_things() \
        , cal = get_cal(current_date) \
        , current_date = current_date \
        , holidays = TAGS_DAO.get_this_month_holiday_dates() \
        , events_this_month = TAGS_DAO.get_this_month_event_dates())


@bp.route('/delete_thing/<int:id>', methods = ['POST'])
def delete_thing(id):
    THINGS_DAO.delete_thing(id)
    
    return redirect(request.referrer)