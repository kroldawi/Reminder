from app.daos import IndexDao, DocumentsDao
from app.models import Document


INDEX_DAO = IndexDao()
DOCUMENT_DAO = DocumentsDao()


class NalewkiService():

    def get_all_nalewki(self):
        return list(filter(lambda db_doc: "Nalewka" in [db_tag.name for db_tag in db_doc.tags] \
            , DOCUMENT_DAO.get_all()))

    
    def get_all_nalewki_basics(self):
        return [{'name': nalewka.name, 'id': nalewka.id} for nalewka in self.get_all_nalewki()]
    

    def get_nalewka_by_id(self, id):
        for nalewka in self.get_all_nalewki():
            if nalewka.id == id:
                ingredients = list(filter(lambda child: child.name == 'Ingredients', nalewka.children))[0].children
                timeline = list(filter(lambda child: child.name == 'Timeline', nalewka.children))[0].children
                notes = list(filter(lambda child: child.name == 'Notes', nalewka.children))[0].children
                recipe = []
                return {'name': nalewka.name
                    , 'timeline': [{'name': entry.name, 'value': entry.value} for entry in timeline]
                    , 'ingredients': [{'name': entry.name, 'value': entry.value} for entry in ingredients]
                    , 'notes': [{'name': entry.name, 'value': entry.value} for entry in notes]
                    , 'recipe': [{'name': entry.name, 'value': entry.value} for entry in recipe]}
        
        return

    
    def get_holiday_dates(self):
        return INDEX_DAO.get_holiday_dates()
    

    def get_oncoming_event_dates(self):
        return INDEX_DAO.get_oncoming_event_dates()
