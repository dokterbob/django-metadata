===============
django-metadata
===============
Generic metadata abstract base classes for Django models.

Abstract base classes
---------------------
DateAbstractBase
^^^^^^^^^^^^^^^^
:Description: Abstract base class with creation and modification date.

PublicationAbstractBase
^^^^^^^^^^^^^^^^^^^^^^^
:Description: Abstract base class with publish option, creation, modification and publication date.

:Name: SitesAbstractBase
:Description: Abstract base class with sites selection and site manager.

:Name: SitesPublicationAbstractBase
:Description: Abstract base class with sites selection and publication attributes.

:Name: AuthorAbstractBase
:Description: Abstract base class adding an author field and a change_author permission.

:Name: DescriptionAbstractBase
:Description: Abstract base class adding a description field.

:Name: TitleAbstractBase
:Description: Abstract base class adding a title field.

:Name: SlugAbstractBase
:Description: Abstract base class adding a slug field.

:Name: CommentsAbstractBase
:Description: Abstract base class adding an `allow_comments` boolean field.

:Name: MetaDataAbstractBase
:Description: Abstract base class containing all the above fields through subclassing.