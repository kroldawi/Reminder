from datetime import datetime
from datetime import date
from sqlalchemy import or_, and_

from app import db
from app.models import Event, Tag

class TagsDao():

    def get_db_tags_by_names(self, tag_names):
        return [Tag.query.filter_by(name = name).first() \
            for name in tag_names]


class EventsDao():

    TAGS_DAO = TagsDao()
    
    def add_event(self, event):
        db_event = Event.query.filter_by(name = event['name']).first()
        
        if not db_event:
            db_event = Event(name = event['name'] \
                , when = event['when'] \
                , recurring = event['recurring']
                , tags = self.TAGS_DAO.get_db_tags_by_names(event['tags']))
        
            db.session.add(db_event)
            db.session.commit()


    def get_this_month_holiday_dates(self):
        curr_year = date.today().year
        db_tag = Tag.query.filter_by(name = 'Holiday').first()

        dates = []
        for db_event in db_tag.events:
            if (db_event.recurring or db_event.when == curr_year):
                dates.append(db_event.when.replace(year = curr_year) \
                        if db_event.recurring \
                        else db_event.when)

        return dates
    

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


    def get_this_month_event_dates(self):
        today = date.today()

        dates = []
        for db_event in Event.query.all():
            if ((db_event.when.year == today.year or db_event.recurring) \
                    and db_event.when.month == today.month):
                dates.append(db_event.when.replace(year = today.year) \
                        if db_event.recurring \
                        else db_event.when)

        return dates