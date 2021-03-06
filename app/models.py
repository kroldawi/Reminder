from datetime import datetime
from app import db


tag_event_assoc = db.Table('tag_event_assoc' \
    , db.Model.metadata \
    , db.Column('tag', db.Integer, db.ForeignKey('tag.id'), nullable = True) \
    , db.Column('event', db.Integer, db.ForeignKey('event.id'), nullable = True))


tag_thing_assoc = db.Table('tag_thing_assoc' \
    , db.Model.metadata \
    , db.Column('tag', db.Integer, db.ForeignKey('tag.id'), nullable = True) \
    , db.Column('thing', db.Integer, db.ForeignKey('thing.id'), nullable = True))


tag_document_assoc = db.Table('tag_document_assoc' \
    , db.Model.metadata \
    , db.Column('tag', db.Integer, db.ForeignKey('tag.id'), nullable = True) \
    , db.Column('document', db.Integer, db.ForeignKey('document.id'), nullable = True))


class Tag(db.Model):
    __tablename__ = 'tag'
    
    id = db.Column(db.Integer, primary_key = True)
    ts = db.Column(db.DateTime, default = datetime.utcnow)
    
    name = db.Column(db.String(32))

    events = db.relationship('Event' \
        , secondary = tag_event_assoc \
        , back_populates = 'tags')
    things = db.relationship('Thing' \
        , secondary = tag_thing_assoc \
        , back_populates = 'tags')
    documents = db.relationship('Document' \
        , secondary = tag_document_assoc \
        , back_populates = 'tags')


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key = True)
    ts = db.Column(db.DateTime, default = datetime.utcnow)
    
    name = db.Column(db.String(64))
    when = db.Column(db.Date)
    recurring = db.Column(db.Boolean)
    
    tags = db.relationship('Tag' \
        , secondary = tag_event_assoc \
        , back_populates = 'events')


class Thing(db.Model):
    __tablename__ = 'thing'
    id = db.Column(db.Integer, primary_key = True)
    ts = db.Column(db.DateTime, default = datetime.utcnow)
    updated_ts = db.Column(db.DateTime, default = datetime.utcnow, onupdate=datetime.utcnow)
    deleted = db.Column(db.Boolean, default = False)
    
    name = db.Column(db.String(64))
    
    tags = db.relationship('Tag' \
        , secondary = tag_thing_assoc \
        , back_populates = 'things')


class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key = True)
    ts = db.Column(db.DateTime, default = datetime.utcnow)
    
    name = db.Column(db.String(64))
    value = db.Column(db.String(512), nullable = True)
    parent_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable = True)
    
    children = db.relationship('Document')
    
    tags = db.relationship('Tag' \
        , secondary = tag_document_assoc \
        , back_populates = 'documents')
