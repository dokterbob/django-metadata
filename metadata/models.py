from datetime import datetime, time

from django.conf import settings

from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.managers import CurrentSiteManager

from metadata.managers import *

PUBLISH_DEFAULT = getattr(settings, 'METADATA_PUBLISH_DEFAULT', True)

class DateAbstractBase(models.Model):
    """ Abstract base class with creation and modification date. """

    class Meta:
        abstract = True
        ordering = ['-create_date', '-modify_date']
        get_latest_by = 'create_date'

    create_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name=_('creation date'))
    modify_date = models.DateTimeField(auto_now=True,
                                       verbose_name=_('modification date'))


def default_publish_date():
    return datetime.now().date()


def default_publish_time():
    now = datetime.now()
    return time(hour=now.hour, minute=now.minute, second=now.second)


class PublicationAbstractBase(DateAbstractBase):
    """ Abstract base class with publish option, creation, modification and
        publication date. """

    class Meta:
        abstract = True
        ordering = ['-publish_date', '-publish_time'] + \
                        DateAbstractBase.Meta.ordering
        get_latest_by = 'publish_date'

    objects = models.Manager()
    published = PublicationManager()

    publish_date = models.DateField(verbose_name=_('publication date'),
                                    default=default_publish_date,
                                    null=True, blank=True, db_index=True)
    publish_time = models.TimeField(verbose_name=_('publication time'),
                                    default=default_publish_time,
                                    null=True, blank=True, db_index=True)
    publish = models.BooleanField(verbose_name=_('published'), 
                                  default=PUBLISH_DEFAULT, db_index=True)

    def get_next_by_published(self):
        qobject = Q(publish_date__gt=self.publish_date) | \
                   (Q(publish_date=self.publish_date) & \
                    Q(publish_time__gt=self.publish_time))

        qs = self.__class__.published.filter(qobject)

        if qs.count():
            return qs.order_by('publish_date', 'publish_time')[0]

        return None

    def get_previous_by_published(self):
        qobject = Q(publish_date__lt=self.publish_date) | \
                   (Q(publish_date=self.publish_date) & \
                    Q(publish_time__lt=self.publish_time))

        qs = self.__class__.published.filter(qobject)

        if qs.count():
            return qs.order_by('-publish_date', '-publish_time')[0]

        return None


def get_default_sites():
    return [site.id for site in Site.objects.all()]


class SitesAbstractBase(models.Model):
    """ Abstract base class with sites selection and site manager. """

    class Meta:
        abstract = True

    sites = models.ManyToManyField(Site, verbose_name=_('sites'),
                                   default=get_default_sites)

    objects = models.Manager()
    on_site = CurrentSiteManager(field_name='sites')


class SitesPublicationAbstractBase(PublicationAbstractBase,
                                   SitesAbstractBase):
    """ Abstract base class with sites selection and publication
        attributes. """

    class Meta:
        abstract = True

    objects = models.Manager()
    published_on_site = CurrentSitePublicationManager(field_name='sites')


class AuthorAbstractBase(models.Model):
    """ Abstract base class adding an author field and a change_author
        permission. """

    class Meta:
        abstract = True
        permissions = (("change_author", ugettext("Change author")), )

    def author_name(self):
        return self.author.get_full_name() or self.author

    author = models.ForeignKey(User, verbose_name=_('author'))


class DescriptionAbstractBase(models.Model):
    """ Abstract base class adding a description field. """

    class Meta:
        abstract = True

    description = models.TextField(verbose_name=_('description'),
                                   null=True, blank=True)


class TitleAbstractBase(models.Model):
    """ Abstract base class adding a title field. """

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=255, verbose_name=_('title'))


class SlugAbstractBase(models.Model):
    """ Abstract base class adding a slug field. """

    class Meta:
        abstract = True

    slug = models.SlugField(max_length=50, verbose_name=_('slug'),
                            db_index=True)


class CommentsAbstractBase(models.Model):
    """ Abstract base class adding an `allow_comments` boolean field. """

    class Meta:
        abstract = True

    allow_comments = models.BooleanField(default=True,
                                         verbose_name=_('allow comments'))

