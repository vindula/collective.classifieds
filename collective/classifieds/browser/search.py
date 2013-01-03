__author__ = """Four Digits <Ralph Jacobs>"""
__docformat__ = 'plaintext'

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.CMFCore.utils import getToolByName


class CatalogSearch:
    """Searches the portal_catalog using given query"""

    def __init__(self, context, query):
        """
            Constructor
        """
        self.context = context
        self.query = query

    def __call__(self):
        """
            returns brains based on searchparameters
        """
        portal_catalog = getToolByName(self.context, "portal_catalog")
        try:
            results = portal_catalog(self.query)
        except:
            return ""
        return results
