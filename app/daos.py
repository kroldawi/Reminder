from datetime import datetime
from datetime import date

from app import db
from app.models import Event, Tag, Thing


class IndexDao():

    def get_all_tags(self):
        tags = []
        for db_tag in Tag.query.all():
            tags.append({'name': db_tag.name \
                , 'id': db_tag.id})
        
        return tags


    def get_all_events(self):
        events = []
        for db_event in Event.query.all():
            events.append({'name': db_event.name \
                , 'when': db_event.when \
                , 'recurring': db_event.recurring \
                , 'tags': db_event.tags \
                , 'id': db_event.id})
        
        return events
    

    def get_all_things(self):
        things = []
        for db_thing in Thing.query.all():
            tags = []
            for db_tag in db_thing.tags:
                tags.append({'name': db_tag.name})
                
            things.append({'name': db_thing.name \
                , 'id': db_thing.id \
                , 'tags': tags})
        
        return things


class ItemsDao():
    
    def get_all(self):
        items = []
        for db_item in Event.query.all():
            items.append({'name': db_item.name \
                , 'when': db_item.when \
                , 'recurring': db_item.recurring \
                , 'id': db_item.id})
        
        return items
    

    def get_for_this_year(self):
        items = self.get_all()
        temp_items = []

        for item in items:
            when_this_year = item['when'].replace(year = date.today().year) if item['recurring'] else item['when']
            
            if when_this_year < date.today() and item['recurring']:
                when_this_year = item['when'].replace(year = date.today().year + 1)

            if (when_this_year - date.today()).days < 200:
                temp_item = {'name': item['name'] \
                    , 'when': when_this_year \
                    , 'days_left': (when_this_year - date.today()).days \
                    , 'recurring': item['recurring']}
                
                temp_items.append(temp_item)
        
        return temp_items
    

    def add_item(self, item):
        db_item = Event(name = item['name'] \
            , when = item['when'] \
            , recurring = item['recurring'])
        
        db.session.add(db_item)
        db.session.commit()
    
    def delete_item(self, id):
        db_item = Event.query.filter_by(id = id).first()
        db.session.delete(db_item)
        db.session.commit()

