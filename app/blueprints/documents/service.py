from app.daos import TagsDao, DocumentsDao
from app.models import Document

TAGS_DAO = TagsDao()
DOCUMENTS_DAO = DocumentsDao()

class DocumentsService():

    def get_tag_name_tuples(self):
        return ((tag.name, tag.name) for tag in TAGS_DAO.get_all())
    

    def get_all_documents(self):
        return [
            {
                'name': db_document.name
                , 'value': db_document.value
                , 'id': db_document.id
                , 'tags': ' '.join(tag.name for tag in db_document.tags)
            }
            for db_document in DOCUMENTS_DAO.get_all()
        ]
    

    def get_document_by_id(self, id):
        for db_document in DOCUMENTS_DAO.get_all():
            if (db_document.id == id):
                return {
                    'name': db_document.name
                    , 'value': db_document.value
                    , 'parent_id': db_document.parent_id
                    , 'children': db_document.children
                }


        #TODO: Add actual return
        return
    

    def add_document(self, document):
        if document['name']:

            db_tags = list(filter(lambda tag: tag.name in document['tags'] \
                , TAGS_DAO.get_all()))
            
            DOCUMENTS_DAO.add_one(Document(
                name = document['name']
                , value = document['value']
                , parent_id = document['parent_id']
                , tags = db_tags))


    def delete_document(self, id):
        DOCUMENTS_DAO.delete_one_by_id(id)