__author__ = """Four Digits <Ralph Jacobs>"""
__docformat__ = 'plaintext'

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from collective.classifieds.content.Classifieds import Classifieds
from collective.classifieds.browser.search import CatalogSearch
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class classifieds_by_author_view(BrowserView):
    """BrowserView class to view classifieds by author"""

    def getClassifiedsByAuthor(self):
        """returns a list of Classified brains
        based on searchstring, using CatalogSearch Class"""
        sort_order = ""
        searchstring = ""
        sort_on = "sortable_title"
        author = ""

        if self.request.form.get('author'):
            author = self.request.form.get('author')

        if self.request.form.get('sort_on'):
            sort_on = self.request.form.get('sort_on')
        if self.request.form.get('sort_order'):
            sort_order = self.request.form.get('sort_order')
        author = self.request.form.get('author')

        if author:
            if len(author) > 0:
                results = []
                query = {'portal_type': ["Classified"],
                    "Creator": author,
                    'sort_on': sort_on,
                    'sort_order': sort_order}
                results = CatalogSearch(self.context, query)()

            if len(results) > 0:
                return results
        return False
