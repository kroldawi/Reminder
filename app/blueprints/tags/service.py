from datetime import datetime
from datetime import date
from sqlalchemy import or_, and_

from app import db
from app.models import Tag
from app.models import Event
from app.daos import TagsDao

TAGS_DAO = TagsDao()


class TagsService():
    def get_all_tags(self):
        return [{'name': db_tag.name, 'id': db_tag.id} \
                for db_tag \
                in TAGS_DAO.get_all()]
    
    
    def add_tag(self, tag):
        TAGS_DAO.add_one(tag)


    def delete_tag(self, id):
        TAGS_DAO.delete_one_by_id(id)


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