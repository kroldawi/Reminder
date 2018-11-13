from app import db
from app.models import Thing, Tag


class TagsDao():

    def get_db_tags_by_names(self, tag_names):
        return [Tag.query.filter_by(name = name).first() for name in tag_names]
    

    def get_tag_name_tuples(self):
        return [(db_tag.name, db_tag.name) for db_tag in Tag.query.all()]


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
