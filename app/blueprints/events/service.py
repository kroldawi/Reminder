from app.daos import TagsDao, EventsDao
from app.models import Event

TAGS_DAO = TagsDao()
EVENTS_DAO = EventsDao()

class EventsService():

    def get_tag_name_tuples(self):
        return ((tag.name, tag.name) for tag in TAGS_DAO.get_all())
    

    def get_all_events(self):
        events = []

        for db_event in EVENTS_DAO.get_all():
            db_tags = ' '.join(tag.name for tag in db_event.tags)
            events.append(
                {'name': db_event.name
                , 'id': db_event.id
                , 'when': db_event.when
                , 'recurring': db_event.recurring
                , 'tags': db_tags})
        
        return events


    def add_event(self, event):
        if event['name'] and not EVENTS_DAO.get_one_by_name(event['name']):
            
            db_tags = list(filter(lambda tag: tag.name in event['tags'] \
                , TAGS_DAO.get_all()))
            
            EVENTS_DAO.add_one(Event(name = event['name'] \
                , when = event['when'] \
                , recurring = event['recurring'] \
                , tags = db_tags))


    def delete_event(self, id):
        EVENTS_DAO.delete_one_by_id(id)