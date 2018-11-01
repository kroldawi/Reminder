from datetime import datetime
from datetime import date

from app import db
from app.models import Event, Tag, Thing


class IndexDao():

    def get_for_this_year(self):
        events = []
        for db_event in Event.query.all():
            events.append({'name': db_event.name \
                , 'when': db_event.when \
                , 'recurring': db_event.recurring})
        temp_events = []

        for event in events:
            when_this_year = event['when'].replace(year = date.today().year) \
                if event['recurring'] \
                else event['when']
            
            if when_this_year < date.today() and event['recurring']:
                when_this_year = event['when'].replace(year = date.today().year + 1)

            if (when_this_year - date.today()).days < 200:
                temp_event = {'name': event['name'] \
                    , 'when': when_this_year \
                    , 'days_left': (when_this_year - date.today()).days \
                    , 'recurring': event['recurring']}
                
                temp_events.append(temp_event)
        
        return temp_events


