from flask import render_template, redirect, request, url_for

from app.blueprints.tags import bp
from app.blueprints.tags.daos import TagsDao
from app.blueprints.tags.forms import AddTagForm, DeleteTagForm


DAO = TagsDao()

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
        , tags = DAO.get_all_tags())


@bp.route('/delete_tag/<int:id>', methods = ['POST'])
def delete_tag(id):
    DAO.delete_tag(id)

    return redirect(request.referrer)