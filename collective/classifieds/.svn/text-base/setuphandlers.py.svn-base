__author__ = """Four Digits <ralph@fourdigits.nl>"""
__docformat__ = 'plaintext'

import logging
logger = logging.getLogger('Classifieds: setuphandlers')
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import log


def isNotClassifiedsProfile(context):
    return context.readDataFile("Classifieds_marker.txt") is None


def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""

    # only for classifieds types
    if isNotClassifiedsProfile(context):
        return
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()


def addCatalogIndexes(context):
    """
        Adds catalog indexes to the portal catalog, instead of using
       catalog.xml which breaks the indexes on every reinstall
    """
    log('addCatalogIndexes called')
    site = context.getSite()
    catalog = getToolByName(site, 'portal_catalog')
    try:
        catalog.addIndex('price', 'FieldIndex')
        log("Added FieldIndex for %s." % 'price')
    except:
        log('Error adding catalog index: price, maybe it allready exists')

    try:
        catalog.addIndex('getImageTile', 'FieldIndex')
        log("Added FieldIndex for %s." % 'getImageTile')
    except:
        log('Error adding catalog index: getImageTile, \
            maybe it allready exists')

    try:
        catalog.addIndex('hasImage', 'FieldIndex')
        log("Added FieldIndex for %s." % 'hasImage')
    except:
        log('Error adding catalog index: hasImage, maybe it allready exists')


def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotClassifiedsProfile(context):
        return
