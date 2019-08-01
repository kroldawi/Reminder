from datetime import datetime
from datetime import date
from sqlalchemy import or_, and_

from app import db
from app.models import Thing, Tag, Event


class TagsDao():

    def get_db_tags_by_names(self, tag_names):
        return [Tag.query.filter_by(name = name).first() for name in tag_names]
    

    def get_tag_name_tuples(self):
        return [(db_tag.name, db_tag.name) for db_tag in Tag.query.all()]
    
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


class ThingsDao():

    TAGS_DAO = TagsDao()

    def get_all_things(self):
        things = []
        for db_thing in Thing.query.all():
            tags = ' '.join(tag.name for tag in db_thing.tags)

            things.append(
                {'name': db_thing.name
                , 'id': db_thing.id
                , 'tags': tags})
        
        return things
    
    
    def add_thing(self, thing):
        db_thing = Thing.query.filter_by(name = thing['name']).first()

        if not db_thing:
            db_thing = Thing(name = thing['name'] \
                , tags = self.TAGS_DAO.get_db_tags_by_names(thing['tags']))

            db.session.add(db_thing)
            db.session.commit()


    def delete_thing(self, id):
        if id:
            db_thing = Thing.query.filter_by(id = id).first()
            
            if db_thing:
                db.session.delete(db_thing)
                db.session.commit()
