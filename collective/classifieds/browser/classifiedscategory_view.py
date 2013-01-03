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
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime


class classifiedscategory_view(BrowserView):
    """BrowserView class for viewing a classifiedscategory"""
    def quotestring(self, string):
        """Adds a quote to the given string"""
        return '"%s"' % string

    def quote_bad_chars(self, string):
        """quotes bad characters"""
        bad_chars = ["(", ")"]
        for char in bad_chars:
            string = string.replace(char, self.quotestring(char))
        return string

    def search(self):
        """Returns a list of Classified brains based
        on searchstring, using CatalogSearch Class"""
        sort_order = ""
        searchstring = ""
        sort_on = "sortable_title"

        if self.request.form.get('sort_on'):
            sort_on = self.request.form.get('sort_on')
        if self.request.form.get('sort_order'):
            sort_order = self.request.form.get('sort_order')
        searchstring = self.request.form.get('frm_searchString')
        if searchstring:
            results = []
            # check if the searchstring is more then 2 characters
            # for 'like' style wildcard search
            if len(searchstring) > 2:
                for char in '?-+*':
                    searchstring = searchstring.replace(char, ' ')
                tmpresults = searchstring.split()
                tmpresults = " AND ".join(tmpresults)
                tmpresults = self.quote_bad_chars(tmpresults) + '*'
            else:
                tmpresults = searchstring

            query = {'portal_type': ["Classified"],
                'SearchableText': tmpresults,
                'sort_on': sort_on,
                'sort_order': sort_order}
            query['path'] = {'query': '/'.join(self.context.getPhysicalPath())}
            results = CatalogSearch(self.context, query)()

            if len(results) > 0:
                return results
        return False

    def getNumberOfClassifieds(self, item):
        """Returns number of classifieds in the category"""
        path = '/%s' % item.getPath()
        portal_catalog = getToolByName(self.context, "portal_catalog")
        query = {'portal_type': ["Classified"]}
        query['path'] = {'query': path}
        query['depth'] = 1
        now = DateTime()
        query['expires'] = {'query': (now), 'range': 'min'}
        results = portal_catalog(query)
        return len(results)
