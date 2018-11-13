from datetime import datetime
from datetime import date

from app import db
from app.models import Event, Tag

class TagsDao():

    def get_db_tags_by_names(self, tag_names):
        return [Tag.query.filter_by(name = name).first() \
            for name in tag_names]
    

    def get_tag_name_tuples(self):
        return ((db_tag.name, db_tag.name) for db_tag in Tag.query.all())


class EventsDao():

    TAGS_DAO = TagsDao()
    
    def get_all_events(self):
        events = []
        for db_event in Event.query.all():
            tags = ' '.join([db_tag.name for db_tag in db_event.tags])

            events.append({'name': db_event.name \
                , 'when': db_event.when \
                , 'recurring': db_event.recurring \
                , 'id': db_event.id
                , 'tags': tags})
        
        return events


    def add_event(self, event):
        db_event = Event.query.filter_by(name = event['name']).first()
        
        if not db_event:
            db_event = Event(name = event['name'] \
                , when = event['when'] \
                , recurring = event['recurring']
                , tags = self.TAGS_DAO.get_db_tags_by_names(event['tags']))
        
            db.session.add(db_event)
            db.session.commit()
    
    def delete_event(self, id):
        if id:
            db_event = Event.query.filter_by(id = id).first()

            if db_event:
                db.session.delete(db_event)
                db.session.commit()
