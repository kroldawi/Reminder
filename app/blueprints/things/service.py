from app.daos import TagsDao, ThingsDao

TAGS_DAO = TagsDao()
THINGS_DAO = ThingsDao()

class ThingsService():

    def get_tag_name_tuples(self):
        return ((tag['name'], tag['name']) for tag in TAGS_DAO.get_all())
    

    def delete_thing(self, id):
        THINGS_DAO.delete_one_by_id(id)