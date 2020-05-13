from flask import render_template, redirect, request, url_for
from datetime import datetime
from datetime import date, timedelta

from app.blueprints.tags import bp
from app.blueprints.tags.service import TagsService
from app.blueprints.tags.forms import AddTagForm, DeleteTagForm


TAGS_SERVICE = TagsService()

def get_cal(current_date):
    first_day = date(current_date.year, current_date.month, 1)
    first_day -= timedelta(days=first_day.isoweekday())
    
    return [[first_day + timedelta(days = i + j * 7) for i in range(7)] for j in range(6)]

@bp.route('/add_tag', methods = ['GET', 'POST'])
def add_tag():
    add_form = AddTagForm()
    delete_form = DeleteTagForm()
    current_date = datetime.today()

    if add_form.validate_on_submit():
        TAGS_SERVICE.add_tag({'name': add_form.name.data})
        return redirect(url_for('tags.add_tag'))

    
    return render_template('tags.html' \
        , add_form = add_form \
        , delete_form = delete_form \
        , tags = TAGS_SERVICE.get_all_tags() \
        , cal = get_cal(current_date) \
        , current_date = current_date \
        , holidays = TAGS_SERVICE.get_this_month_holiday_dates() \
        , events_this_month = TAGS_SERVICE.get_this_month_event_dates())


@bp.route('/delete_tag/<int:id>', methods = ['POST'])
def delete_tag(id):
    TAGS_SERVICE.delete_tag(id)

    return redirect(request.referrer)