from app.daos import TagsDao ,EventsDao

TAGS_DAO = TagsDao()
EVENTS_DAO = EventsDao()

class EventsService():

    def get_tag_name_tuples(self):
        return ((tag['name'], tag['name']) for tag in TAGS_DAO.get_all())


    def delete_event(self, id):
        EVENTS_DAO.delete_one_by_id(id)