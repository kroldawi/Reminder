from app import db
from app.models import Tag


class TagsDao():

    def get_all_tags(self):
        return [{'name': db_tag.name, 'id': db_tag.id} 
            for db_tag in Tag.query.all()]
    
    
    def add_tag(self, tag):
        db_tag = Tag.query.filter_by(name = tag['name']).first()

        if not db_tag:
            db_tag = Tag(name = tag['name'])
            db.session.add(db_tag)
            db.session.commit()


    def delete_tag(self, id):
        db_tag = Tag.query.filter_by(id = id).first()
            
        if db_tag:
            db.session.delete(db_tag)
            db.session.commit()
