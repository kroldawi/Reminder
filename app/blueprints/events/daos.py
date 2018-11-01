from datetime import datetime
from datetime import date

from app import db
from app.models import Event


class EventsDao():
    
    def get_all_events(self):
        events = []
        for db_event in Event.query.all():
            events.append({'name': db_event.name \
                , 'when': db_event.when \
                , 'recurring': db_event.recurring \
                , 'id': db_event.id})
        
        return events


    def add_event(self, event):
        db_event = Event(name = event['name'] \
            , when = event['when'] \
            , recurring = event['recurring'])
        
        db.session.add(db_event)
        db.session.commit()
    
    def delete_event(self, id):
        db_event = Event.query.filter_by(id = id).first()
        db.session.delete(db_event)
        db.session.commit()