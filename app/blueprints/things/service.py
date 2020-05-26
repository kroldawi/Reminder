from app.daos import TagsDao, ThingsDao, IndexDao
from app.models import Thing

TAGS_DAO = TagsDao()
THINGS_DAO = ThingsDao()
INDEX_DAO = IndexDao()

class ThingsService():

    def get_tag_name_tuples(self):
        return ((tag.name, tag.name) for tag in TAGS_DAO.get_all())
    

    def get_all_things(self):
        things = []
        for db_thing in THINGS_DAO.get_all():
            #if not db_thing.deleted or db_thing.deleted == False:
                tags = ' '.join(tag.name for tag in db_thing.tags)
            
                things.append(
                    {'name': db_thing.name
                    , 'id': db_thing.id
                    , 'created': db_thing.ts
                    , 'tags': tags
                    , 'deleted': db_thing.deleted})
        
        return things
    

    def add_thing(self, thing):
        if thing['name'] :
            db_tags = list(filter(lambda tag: tag.name in thing['tags'] \
                , TAGS_DAO.get_all()))
            
            THINGS_DAO.add_one(Thing(name = thing['name'], tags = db_tags))


    def soft_delete_thing(self, id):
        db_thing = THINGS_DAO.get_one_by_id(id)
        if db_thing:
            db_thing.deleted = True
            THINGS_DAO.update_one(db_thing)
    

    def get_holiday_dates(self):
        return INDEX_DAO.get_holiday_dates()


    def get_oncoming_event_dates(self):
        return INDEX_DAO.get_oncoming_event_dates()