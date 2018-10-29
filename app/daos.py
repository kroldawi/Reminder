from datetime import datetime
from datetime import date

from app import db
from app.models import Item


class ItemsDao():
    
    def get_all(self):
        items = []
        for db_item in Item.query.all():
            items.append({'name': db_item.name \
                , 'when': db_item.when \
                , 'recurring': db_item.recurring})
        
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
        db_item = Item(name = item['name'] \
            , when = item['when'] \
            , recurring = item['recurring'])
        
        db.session.add(db_item)
        db.session.commit()
    
    def delete_item(self, item):
        db_item = Item.query.filter_by(name = item['name']).first()
        db.session.delete(db_item)
        db.session.commit()

