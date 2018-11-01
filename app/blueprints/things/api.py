from flask import render_template, redirect, url_for
from app import db

from app.blueprints.things import bp
from app.blueprints.things.daos import ThingsDao
from app.blueprints.things.forms import AddThingForm, DeleteThingForm


DAO = ThingsDao()

@bp.route('/add_thing', methods = ['GET', 'POST'])
def add_thing():
    add_form = AddThingForm()
    delete_form = DeleteThingForm()

    if add_form.validate_on_submit():
        DAO.add_thing({'name': add_form.name.data})
    
    return render_template('things.html' \
        , add_form = add_form \
        , delete_form = delete_form \
        , things = DAO.get_all_things())


@bp.route('/delete_thing/<int:id>', methods = ['POST'])
def delete_thing(id):
    DAO.delete_thing(id)

    return redirect(url_for('.add_thing'))