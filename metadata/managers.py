from datetime import datetime

from django.db.models import Manager, Q
from django.contrib.sites.managers import CurrentSiteManager

class PublicationManager(Manager):
    def get_query_set(self):
        qs = super(PublicationManager, self).get_query_set()
        qs = qs.filter(publish=True)
        
        # Either the date should be less than today or the date is today and the time should
        # be less than now.
        now = datetime.now()
        current_date = datetime.date(now)
        current_time = datetime.time(now)
        qs = qs.filter(Q(publish_date__lte=current_date) | \
                       (Q(publish_date__exact=current_date) & Q(publish_time__lte=current_time)))
        
        return qs

class CurrentSitePublicationManager(CurrentSiteManager):
    def get_query_set(self):
        qs = super(CurrentSitePublicationManager,  self).get_query_set()
        return qs.filter(publish=True,publish_date__lte=datetime.now())
