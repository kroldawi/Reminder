from flask import render_template, redirect, url_for
from app import db

from app.blueprints.things import bp
from app.blueprints.things.daos import ThingsDao, TagsDao
from app.blueprints.things.forms import DeleteThingForm, FormFieldFactory


THINGS_DAO = ThingsDao()
TAGS_DAO = TagsDao()
FORM_FACTORY = FormFieldFactory()

@bp.route('/add_thing', methods = ['GET', 'POST'])
def add_thing():
    delete_form = DeleteThingForm()
    add_form = FORM_FACTORY.create_add_thing_form(TAGS_DAO.get_tag_name_tuples())

    if add_form.validate_on_submit():
        THINGS_DAO.add_thing({'name': add_form.name.data, \
            'tags': add_form.tags.data})
    
    return render_template('things.html' \
        , add_form = add_form \
        , delete_form = delete_form \
        , things = THINGS_DAO.get_all_things())


@bp.route('/delete_thing/<int:id>', methods = ['POST'])
def delete_thing(id):
    THINGS_DAO.delete_thing(id)

    return redirect(url_for('.add_thing'))