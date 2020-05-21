from app.daos import TagsDao, DocumentsDao
from app.models import Document

TAGS_DAO = TagsDao()
DOCUMENTS_DAO = DocumentsDao()

class DocumentsService():

    def get_tag_name_tuples(self):
        return ((tag.name, tag.name) for tag in TAGS_DAO.get_all())
    

    def get_all_documents(self):
        documents = []
        for db_document in DOCUMENTS_DAO.get_all():
            tags = ' '.join(tag.name for tag in db_document.tags)

            documents.append(
                {'name': db_document.name
                , 'id': db_document.id
                , 'tags': tags})
        
        return documents
    

    def add_document(self, document):
        if document['name'] and not DOCUMENTS_DAO.get_one_by_name(document['name']):

            db_tags = list(filter(lambda tag: tag.name in document['tags'] \
                , TAGS_DAO.get_all()))
            
            DOCUMENTS_DAO.add_one(Document(name = document['name'], tags = db_tags))


    def delete_document(self, id):
        DOCUMENTS_DAO.delete_one_by_id(id)