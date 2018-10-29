from flask import render_template, url_for, redirect

from app import app
from app.daos import ItemsDao
from app.forms import AddItemForm


@app.route('/')
@app.route('/index')
def index():
    dao = ItemsDao()

    return render_template('index.html', items = dao.get_for_this_year(), items1 = dao.get_all())


@app.route('/add_item', methods = ['GET', 'POST'])
def add_item():
    dao = ItemsDao()
    form = AddItemForm()

    if form.validate_on_submit():
        dao.add_item({'name': form.name.data \
            , 'when': form.when.data \
            , 'recurring': form.recurring.data})
        return redirect(url_for('index'))

    return render_template('add_item.html', form = form)