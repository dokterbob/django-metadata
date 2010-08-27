===============
django-metadata
===============
Generic metadata abstract base classes for Django models.

Abstract base classes
=====================

DateAbstractBase
^^^^^^^^^^^^^^^^
Abstract base class with creation and modification date.

PublicationAbstractBase
^^^^^^^^^^^^^^^^^^^^^^^
Abstract base class with publish option, creation, modification and publication date.

SitesAbstractBase
^^^^^^^^^^^^^^^^^
Abstract base class with sites selection and site manager.

SitesPublicationAbstractBase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Abstract base class with sites selection and publication attributes.

AuthorAbstractBase
^^^^^^^^^^^^^^^^^^
Abstract base class adding an author field and a change_author permission.

DescriptionAbstractBase
^^^^^^^^^^^^^^^^^^^^^^^
Abstract base class adding a description field.

TitleAbstractBase
^^^^^^^^^^^^^^^^^
Abstract base class adding a title field.

SlugAbstractBase
^^^^^^^^^^^^^^^^
Abstract base class adding a slug field.

CommentsAbstractBase
^^^^^^^^^^^^^^^^^^^^
Abstract base class adding an `allow_comments` boolean field.

MetaDataAbstractBase
^^^^^^^^^^^^^^^^^^^^
Abstract base class containing all the above fields through subclassing.
