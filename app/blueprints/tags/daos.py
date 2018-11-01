from app import db
from app.models import Tag


class TagsDao():

    def get_all_tags(self):
        tags = []
        for db_tag in Tag.query.all():
            tags.append({'name': db_tag.name \
                , 'id': db_tag.id})
        
        return tags
    
    
    def add_tag(self, tag):
        db_tag = Tag.query.filter_by(name = tag['name']).first()

        if not db_tag:
            db_tag = Tag(name = tag['name'])
            db.session.add(db_tag)
            db.session.commit()


    def delete_tag(self, id):
        if id:
            db_tag = Tag.query.filter_by(id = id).first()
            
            if db_tag:
                db.session.delete(db_tag)
                db.session.commit()
