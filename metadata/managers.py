from datetime import datetime

from django.db.models import Manager
from django.contrib.sites.managers import CurrentSiteManager

class PublicationManager(Manager):
    def get_query_set(self):
        qs = super(PublicationManager, self).get_query_set()
        return qs.filter(publish=True,
                         publish_date__lte=datetime.now(),   
                         publish_time__lte=datetime.now())

class CurrentSitePublicationManager(CurrentSiteManager):
    def get_query_set(self):
        qs = super(CurrentSitePublicationManager,  self).get_query_set()
        return qs.filter(publish=True,publish_date__lte=datetime.now())
