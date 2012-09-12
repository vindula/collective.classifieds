__author__ = """Four Digits <Ralph Jacobs>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from collective.classifieds.config import *

schema = Schema((

),
)

Classifieds_schema = BaseBTreeFolderSchema.copy() + schema.copy()


class Classifieds(BaseBTreeFolder, BrowserDefaultMixin):
    """
        Container which can contain Categories and Classifieds
    """
    security = ClassSecurityInfo()

    implements(interfaces.IClassifieds)

    meta_type = 'Classifieds'
    _at_rename_after_creation = True

    schema = Classifieds_schema

    def getPath(self):
        """Gets the path of the object"""
        path = '/'.join(self.getPhysicalPath())
        return path

registerType(Classifieds, PROJECTNAME)
# end of class Classifieds
