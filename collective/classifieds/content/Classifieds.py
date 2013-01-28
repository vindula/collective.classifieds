__author__ = """Four Digits <Ralph Jacobs>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from collective.classifieds.content.interfaces import IClassifieds
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from plone.app.folder.folder import ATFolder

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from collective.classifieds.config import *

Classifieds_schema =  ATFolder.schema.copy() + Schema((
))

finalizeATCTSchema(Classifieds_schema, folderish=True)
invisivel = {'view':'invisible','edit':'invisible',}
Classifieds_schema["nextPreviousEnabled"].widget.visible = invisivel

class Classifieds(ATFolder):
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
