__author__ = """Four Digits <Ralph Jacobs>"""
__docformat__ = 'plaintext'

from Products.CMFCore.permissions import setDefaultRoles

PROJECTNAME = "collective.classifieds"

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner'))
ADD_CONTENT_PERMISSIONS = {
    'ClassifiedsCategory': 'Classifieds: Add ClassifiedsCategory',
    'Classifieds': 'Classifieds: Add Classifieds',
    'Classified': 'Classifieds: Add Classified',
    'OrderedClassifiedsCategory': 'Classifieds: Add OrderedClassifiedsCategory',
}

setDefaultRoles('Classifieds: Add ClassifiedsCategory', ('Manager', 'Owner'))
setDefaultRoles('Classifieds: Add Classifieds', ('Manager', 'Owner'))
setDefaultRoles('Classifieds: Add Classified', ('Manager', 'Owner'))
setDefaultRoles('Classifieds: Add OrderedClassifiedsCategory', ('Manager', 'Owner'))

product_globals = globals()

DEPENDENCIES = []
PRODUCT_DEPENDENCIES = []
