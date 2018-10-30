from flask import render_template, url_for, redirect

from app import app
from app.daos import ItemsDao, IndexDao
from app.forms import AddItemForm, DeleteItemForm


@app.route('/')
@app.route('/index')
def index():
    dao = ItemsDao()
    form = DeleteItemForm()
    index_dao = IndexDao()

    return render_template('index.html' \
        , items = dao.get_for_this_year() \
        , all_items = dao.get_all() \
        , events = index_dao.get_all_events() \
        , tags = index_dao.get_all_tags() \
        , things = index_dao.get_all_things() \
        , form = form)


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


@app.route('/delete_item/<int:id>', methods=['POST'])
def delete_item(id):
    dao = ItemsDao()
    dao.delete_item(id)
    return redirect(url_for('index'))


@app.route('/item/<int:id>', methods=['DELETE'])
def api_delete_item(id):
    dao = ItemsDao()
    dao.delete_item(id)
