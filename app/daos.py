from datetime import datetime
from datetime import date
from sqlalchemy import or_

from app import db
from app.models import Event, Tag, Thing

class TagsDao():
    def get_all(self):
        return [{'name': db_tag.name, 'id': db_tag.id} \
                for db_tag \
                in Tag.query.all()]


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
    def delete_one_by_id(self, id):
        if id:
            db_event = Event.query.filter_by(id = id).first()

            if db_event:
                db.session.delete(db_event)
                db.session.commit()


class ThingsDao():
    def delete_one_by_id(self, id):
        if id:
            db_thing = Thing.query.filter_by(id = id).first()
            
            if db_thing:
                db.session.delete(db_thing)
                db.session.commit()


class IndexDao():

    def get_todos(self):
        db_tag = Tag.query.filter_by(name = 'TODO').first()
        return [{'name': thing.name} for thing in db_tag.things]
    

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