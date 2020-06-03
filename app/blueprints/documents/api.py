from flask import render_template, redirect, request, url_for
from datetime import datetime
from datetime import date, timedelta

from app.blueprints.documents import bp
from app.blueprints.documents.service import DocumentsService
from app.blueprints.documents.forms import AddDocumentForm, DeleteDocumentForm, FormFieldFactory


DOCUMENTS_SERVICE = DocumentsService()
FORM_FACTORY = FormFieldFactory()


def get_cal(current_date):
    first_day = date(current_date.year, current_date.month, 1)
    first_day -= timedelta(days=first_day.isoweekday())
    
    return [[first_day + timedelta(days = i + j * 7) for i in range(7)] for j in range(6)]


@bp.route('/add_document', methods = ['GET', 'POST'])
def add_document():
    delete_form = DeleteDocumentForm()
    current_date = datetime.today()
    add_form = FORM_FACTORY.create_add_document_form(DOCUMENTS_SERVICE.get_tag_name_tuples())

    if add_form.validate_on_submit():
        DOCUMENTS_SERVICE.add_document({
            'name': add_form.name.data
            , 'value': add_form.value.data
            , 'tags': add_form.tags.data
            , 'parent_id': None})
        return redirect(url_for('documents.add_document'))

    return render_template('documents.html' \
        , add_form = add_form \
        , delete_form = delete_form \
        , documents = DOCUMENTS_SERVICE.get_all_documents() \
        , cal = get_cal(current_date) \
        , current_date = current_date \
        , holidays = [] \
        , events_this_month = [])


@bp.route('/patch_document/<int:id>', methods = ['GET', 'POST'])
def patch_document(id):
    delete_form = DeleteDocumentForm()
    current_date = datetime.today()
    add_form = FORM_FACTORY.create_add_document_form(DOCUMENTS_SERVICE.get_tag_name_tuples())

    if add_form.validate_on_submit():
        DOCUMENTS_SERVICE.add_document(
            {'name': add_form.name.data
            , 'value': add_form.value.data
            , 'parent_id': id
            , 'tags': []})
        return redirect(request.referrer)

    return render_template('patch_document.html' \
        , parent_id = id
        , add_form = add_form \
        , delete_form = delete_form \
        , document = DOCUMENTS_SERVICE.get_document_by_id(id) \
        , cal = get_cal(current_date) \
        , current_date = current_date \
        , holidays = [] \
        , events_this_month = [])


@bp.route('/delete_document/<int:id>', methods=['POST'])
def delete_document(id):
    DOCUMENTS_SERVICE.delete_document(id)

    return redirect(request.referrer)
