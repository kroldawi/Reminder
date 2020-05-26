from datetime import datetime
from datetime import date
from sqlalchemy import or_

from app import db
from app.models import Event, Tag, Thing, Document

class TagsDao():
    def get_all(self):
        return Tag.query.all()


    def add_one(self, tag):
        db_tag = Tag.query.filter_by(name = tag['name']).first()

        if not db_tag:
            db_tag = Tag(name = tag['name'])
            db.session.add(db_tag)
            db.session.commit()


    def delete_one_by_id(self, id):
        if id:
            db_tag = Tag.query.filter_by(id = id).first()
            
            if db_tag:
                db.session.delete(db_tag)
                db.session.commit()


class EventsDao():
    def get_all(self):
        return Event.query.all()


    def get_one_by_name(self, name):
        return Event.query.filter_by(name = name).first()


    def add_one(self, db_event):
        db.session.add(db_event)
        db.session.commit()


    def delete_one_by_id(self, id):
        if id:
            db_event = Event.query.filter_by(id = id).first()

            if db_event:
                db.session.delete(db_event)
                db.session.commit()


class ThingsDao():
    def get_all(self):
        return Thing.query.all()

    
    def get_one_by_id(self, id):
        return Thing.query.filter_by(id = id).first()
    

    def get_one_by_name(self, name):
        return Thing.query.filter_by(name = name).first()


    def add_one(self, db_thing):
        db.session.add(db_thing)
        db.session.commit()


    def update_one(self, db_thing):
        if self.get_one_by_id(db_thing.id):
            self.add_one(db_thing)


    def delete_one_by_id(self, id):
        if id:
            db_thing = Thing.query.filter_by(id = id).first()
            
            if db_thing:
                db.session.delete(db_thing)
                db.session.commit()


class DocumentsDao():

    def get_all(self):
        return Document.query.all()
    

    def get_one_by_name(self, name):
        return Document.query.filter_by(name = name).first()
    

    def add_one(self, db_document):
        db.session.add(db_document)
        db.session.commit()

    
    def delete_one_by_id(self, id):
        if id:
            db_document = Document.query.filter_by(id = id).first()
            
            if db_document:
                db.session.delete(db_document)
                db.session.commit()


class IndexDao():

    def get_todos(self, current_date):
        db_tag = Tag.query.filter_by(name = 'TODO').first()
        #TODO: none for updated_ts
        db_todos = list(filter(lambda thing: not thing.deleted or not thing.updated_ts or thing.updated_ts.date() == date.today()
                , db_tag.things))
        return [{'name': thing.name
            , 'id': thing.id
            , 'deleted': thing.deleted} 
            for thing in db_todos]
    

    def get_holiday_dates(self):
        curr_year = date.today().year
        db_tag = Tag.query.filter_by(name = 'Holiday').first()

        event_dates = []
        for db_event in db_tag.events:
            if (db_event.recurring or db_event.when == curr_year):
                event_dates.append(db_event.when.replace(year = curr_year) \
                        if db_event.recurring \
                        else db_event.when)

        return event_dates


    def get_oncoming_events(self):
        events = []
        today = date.today()
        first_of_a_month = today.replace(day = 1)

        for db_event in Event.query \
                .filter(or_(Event.recurring == True, Event.when >= first_of_a_month)) \
                .all():
            
            when_this_year = db_event.when
            if (db_event.recurring):
                when_this_year = when_this_year.replace(year = first_of_a_month.year)
                if when_this_year < first_of_a_month:
                    when_this_year = when_this_year.replace(year = first_of_a_month.year + 1)
            
            if ((when_this_year - first_of_a_month).days < 200):
                events.append({'name': db_event.name \
                        , 'when': when_this_year \
                        , 'days_left': (when_this_year - today).days \
                        , 'id': db_event.id})

        return sorted(events, key = lambda event: event['days_left'])


    def get_oncoming_event_dates(self):
        return [event['when'] for event in self.get_oncoming_events()]
