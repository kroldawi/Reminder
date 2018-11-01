from app import db
from app.models import Thing


class ThingsDao():

    def get_all_things(self):
        things = []
        for db_thing in Thing.query.all():
            things.append({'name': db_thing.name \
                , 'id': db_thing.id})
        
        return things
    
    
    def add_thing(self, thing):
        db_thing = Thing.query.filter_by(name = thing['name']).first()

        if not db_thing:
            db_thing = Thing(name = thing['name'])
            db.session.add(db_thing)
            db.session.commit()


    def delete_thing(self, id):
        if id:
            db_thing = Thing.query.filter_by(id = id).first()
            
            if db_thing:
                db.session.delete(db_thing)
                db.session.commit()
