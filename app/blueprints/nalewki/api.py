from flask import render_template, redirect, url_for
from datetime import datetime
from datetime import date, timedelta

from app.blueprints.nalewki import bp
from app.blueprints.nalewki.service import NalewkiService


NALEWKI_SERVICE = NalewkiService()


def get_cal(current_date):
    first_day = date(current_date.year, current_date.month, 1)
    first_day -= timedelta(days=first_day.isoweekday())
    
    return [[first_day + timedelta(days = i + j * 7) for i in range(7)] for j in range(6)]

@bp.route('/nalewki', methods = ['GET'])
def nalewki():
    id = NALEWKI_SERVICE.get_all_nalewki_basics()[0]['id']
    return redirect(url_for('.nalewka', id = id))


@bp.route('/nalewki/<int:id>', methods = ['GET'])
def nalewka(id):
    current_date = datetime.today()

    return render_template('nalewki.html'
        , nalewki = NALEWKI_SERVICE.get_all_nalewki_basics()
        , nalewka = NALEWKI_SERVICE.get_nalewka_by_id(id)
        , cal = get_cal(current_date)
        , current_date = current_date
        , holidays = NALEWKI_SERVICE.get_holiday_dates()
        , events_this_month = NALEWKI_SERVICE.get_oncoming_event_dates())