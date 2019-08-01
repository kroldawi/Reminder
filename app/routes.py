from flask import render_template, url_for, redirect
from datetime import datetime
from datetime import date, timedelta

from app import app
from app.daos import IndexDao
from app.forms import DeleteForm


DAO = IndexDao()


def get_cal(current_date):
    first_day = date(current_date.year, current_date.month, 1)
    first_day -= timedelta(days=first_day.isoweekday())
    
    return [[first_day + timedelta(days = i + j * 7) for i in range(7)] for j in range(6)]


@app.route('/')
@app.route('/index')
def index():
    delete_form = DeleteForm()
    current_date = datetime.today()

    return render_template('index.html' \
        , events = DAO.get_oncoming_events() \
        , todos = DAO.get_todos() \
        , cal = get_cal(current_date) \
        , current_date = current_date \
        , holidays = DAO.get_holiday_dates() \
        , events_this_month = DAO.get_oncoming_event_dates() \
        , delete_form = delete_form)