__author__ = """Four Digits <Ralph Jacobs>"""
__docformat__ = 'plaintext'

import interfaces
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import ImageField
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import AttributeStorage
from Products.Archetypes.public import registerType
from zope.interface import implements
from Products.CMFCore.utils import getToolByName
from collective.classifieds.config import *
from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import document
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.lib.constraintypes \
import ConstrainTypesMixinSchema


schema = Schema((
    ImageField(
        name='categoryimage',
        widget=ImageField._properties['widget'](
            label="Category image",
            description="Image which represents the category",
            label_msgid="classifieds_classifiedscategory_categoryimage",
            description_msgid=\
            "classifieds_classifiedscategory_categoryimage_description",
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

OrderedClassifiedsCategory_schema = document.ATDocumentSchema.copy()
OrderedClassifiedsCategory_schema += ConstrainTypesMixinSchema
OrderedClassifiedsCategory_schema += schemata.NextPreviousAwareSchema
OrderedClassifiedsCategory_schema += atapi.Schema((

)) + schema.copy()


schemata.finalizeATCTSchema(OrderedClassifiedsCategory_schema,
                            folderish=True,
                            moveDiscussion=False)


class OrderedClassifiedsCategory(folder.ATFolder):
    """
        Category which can contain Classifieds (such as books),
        Ordered version
    """
    security = ClassSecurityInfo()

    implements(interfaces.IOrderedClassifiedsCategory)

    meta_type = 'OrderedClassifiedsCategory'
    _at_rename_after_creation = True

    schema = OrderedClassifiedsCategory_schema

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
    # Methods

registerType(OrderedClassifiedsCategory, PROJECTNAME)
# end of class OrderedClassifiedsCategory
