from app.daos import IndexDao, DocumentsDao
from app.models import Document


INDEX_DAO = IndexDao()
DOCUMENT_DAO = DocumentsDao()


class NalewkiService():

    def get_all_nalewki(self):
        return list(filter(lambda db_doc: "Nalewka" in [db_tag.name for db_tag in db_doc.tags] \
            , DOCUMENT_DAO.get_all()))

    
    def get_all_nalewki_test(self):
        nalewki = list(filter(lambda db_doc: "Nalewka" in [db_tag.name for db_tag in db_doc.tags] \
            , DOCUMENT_DAO.get_all()))
        
        return [{'name': nalewka.name} for nalewka in nalewki]

    
    def get_holiday_dates(self):
        return INDEX_DAO.get_holiday_dates()
    

    def get_oncoming_event_dates(self):
        return INDEX_DAO.get_oncoming_event_dates()
