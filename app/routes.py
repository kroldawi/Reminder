from flask import render_template, url_for, redirect

from app import app
from app.daos import IndexDao


@app.route('/')
@app.route('/index')
def index():
    index_dao = IndexDao()

    return render_template('index.html' \
        , events = index_dao.get_for_this_year())

