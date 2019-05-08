from flask import render_template, redirect, request, url_for
from datetime import datetime
from datetime import date, timedelta

from app.blueprints.tags import bp
from app.blueprints.tags.daos import TagsDao
from app.blueprints.tags.forms import AddTagForm, DeleteTagForm


DAO = TagsDao()

def get_cal(current_date):
    first_day = date(current_date.year, current_date.month, 1)
    first_day -= timedelta(days=first_day.isoweekday())
    
    return [[first_day + timedelta(days = i + j * 7) for i in range(7)] for j in range(6)]

@bp.route('/add_tag', methods = ['GET', 'POST'])
def add_tag():
    add_form = AddTagForm()
    delete_form = DeleteTagForm()

    if add_form.validate_on_submit():
        DAO.add_tag({'name': add_form.name.data})
        return redirect(url_for('tags.add_tag'))

    
    return render_template('tags.html' \
        , add_form = add_form \
        , delete_form = delete_form \
        , tags = DAO.get_all_tags() \
        , cal = get_cal(date(2019,4,2)))


@bp.route('/delete_tag/<int:id>', methods = ['POST'])
def delete_tag(id):
    DAO.delete_tag(id)

    return redirect(request.referrer)