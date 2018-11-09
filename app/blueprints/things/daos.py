from app import db
from app.models import Thing, Tag


class TagsDao():

    def get_db_tags_by_names(self, tag_names):
        db_tags = []
        for name in tag_names:
            db_tags.append(Tag.query.filter_by(name = name).first())
        
        return db_tags
    

    def get_tag_name_tuples(self):
        names = []
        for db_tag in Tag.query.all():
            names.append((db_tag.name, db_tag.name))
        
        return names


class ThingsDao():

    TAGS_DAO = TagsDao()

    def get_all_things(self):
        things = []
        for db_thing in Thing.query.all():
            tags = ''
            if db_thing.tags:
                for tag in db_thing.tags:
                    tags += tag.name + ' '

            things.append({'name': db_thing.name \
                , 'id': db_thing.id \
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
