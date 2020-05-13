from flask import render_template
from datetime import datetime
from datetime import date, timedelta

from app.blueprints.nalewki import bp


def get_cal(current_date):
    first_day = date(current_date.year, current_date.month, 1)
    first_day -= timedelta(days=first_day.isoweekday())
    
    return [[first_day + timedelta(days = i + j * 7) for i in range(7)] for j in range(6)]

@bp.route('/nalewki', methods = ['GET'])
def nalewki():
    current_date = datetime.today()

    return render_template('nalewki.html' \
        , events = [] \
        , cal = get_cal(current_date) \
        , current_date = current_date \
        , holidays = [] \
        , events_this_month = [])
