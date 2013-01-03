__author__ = """Four Digits <Ralph Jacobs>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from collective.classifieds.config import *
from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import document
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.lib.constraintypes \
import ConstrainTypesMixinSchema

OrderedClassifieds_schema = document.ATDocumentSchema.copy()
OrderedClassifieds_schema += ConstrainTypesMixinSchema.copy()
OrderedClassifieds_schema += schemata.NextPreviousAwareSchema.copy()
OrderedClassifieds_schema += atapi.Schema((

))

schemata.finalizeATCTSchema(OrderedClassifieds_schema,
                            folderish=True,
                            moveDiscussion=False)


class OrderedClassifieds(folder.ATFolder):
    """
        Container which can contain Categories and Classifieds (Ordered)
    """
    security = ClassSecurityInfo()

    implements(interfaces.IOrderedClassifieds)

    meta_type = 'OrderedClassifieds'
    _at_rename_after_creation = True

    schema = OrderedClassifieds_schema

    def getPath(self):
        """Gets the path of the object"""
        path = '/'.join(self.getPhysicalPath())
        return path

registerType(OrderedClassifieds, PROJECTNAME)
# end of class Classifieds
