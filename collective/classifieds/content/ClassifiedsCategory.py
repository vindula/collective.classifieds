__author__ = """Four Digits <Ralph Jacobs>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.Archetypes.atapi import Schema
from Products.Archetypes.public import registerType
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.CMFCore.utils import getToolByName
from collective.classifieds.config import *

schema = Schema((
    ImageField(
        name='categoryimage',
        widget=ImageField._properties['widget'](
            label="Category image",
            description="Image which represents the category",
            label_msgid="classifieds_classifiedscategory_categoryimage",
            description_msgid="classifieds_classifiedscategory_categoryimage_description",
            i18n_domain='classifieds',
        ),
        storage=AttributeStorage(),
        max_size=(768, 768),
        sizes={'large': (768, 768),
                   'preview': (400, 400),
                   'mini': (200, 200),
                   'thumb': (128, 128),
                   'tile': (64, 64),
                   'icon': (32, 32),
                   'listing': (16, 16),
                  },
        ),
    ),
)

ClassifiedsCategory_schema = BaseBTreeFolderSchema.copy() + \
    schema.copy()


class ClassifiedsCategory(BaseBTreeFolder, BrowserDefaultMixin):
    """
        Category which can contain Classifieds (such as books)
    """
    security = ClassSecurityInfo()
    implements(interfaces.IClassifiedsCategory)
    meta_type = 'ClassifiedsCategory'
    _at_rename_after_creation = True

    schema = ClassifiedsCategory_schema

    def getPath(self):
        """Gets the path of the object"""
        path = '/'.join(self.getPhysicalPath())
        return path

    def hasImage(self):
        """checks if the category has a image"""
        if self.getCategoryimage():
            return True
        return False

    def getImageTile(self, **kwargs):
        """Get image tile url, relative to plone site."""
        if self.hasImage():
            portal_obj = getToolByName(self, 'portal_url').getPortalObject()
            imgtileurl = self.getCategoryimage().absolute_url(1) + '_tile'
            portal_url = portal_obj.absolute_url(1)
            imgtileurl = imgtileurl.replace(portal_url, '')
            if imgtileurl[0] == "/":
                imgtileurl = imgtileurl.replace('/', '', 1)
            return imgtileurl
        return ''

registerType(ClassifiedsCategory, PROJECTNAME)
# end of class ClassifiedsCategory
