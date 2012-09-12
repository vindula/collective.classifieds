__author__ = """Four Digits <Ralph Jacobs>"""
__docformat__ = 'plaintext'

from zope import interface
from zope import component

from Products.Five import BrowserView
from zope.interface import implements
from collective.classifieds.content.Classifieds import Classifieds
from collective.classifieds.browser.search import CatalogSearch
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime


class list_view(BrowserView):
    """BrowserView class, lists classifieds
       and categories within the Classifieds"""

    def quotestring(self, string):
        """Adds a quote to the given string"""
        return '"%s"' % string

    def quote_bad_chars(self, string):
        """quotes bad characters"""
        bad_chars = ["(", ")"]
        for char in bad_chars:
            string = string.replace(char, self.quotestring(char))
        return string

    def getLatestClassifieds(self, limit):
        """Returns 10 latest classifieds"""
        if limit == "":
            limit = 10
        query = {'portal_type': ["Classified"],
            'sort_on': 'created',
            'sort_order': 'reverse',
            'sort_limit': limit}
        query['path'] = {'query': '/'.join(self.context.getPhysicalPath())}
        results = CatalogSearch(self.context, query)()
        return results

    def search(self):
        """
            returns a list of Classified brains based on searchstring,
            using CatalogSearch Class
        """
        sort_order = ""
        searchstring = ""
        sort_on = "sortable_title"

        if self.request.form.get('sort_order'):
            sort_order = self.request.form.get('sort_order')
        if self.request.form.get('sort_on'):
            sort_on = self.request.form.get('sort_on')
        searchstring = self.request.form.get('frm_searchString')
        if searchstring:
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

            if tmpresults != '*':
                query = {'portal_type': ["Classified"],
                    'SearchableText': tmpresults,
                    'sort_on': sort_on, "sort_order": sort_order}
                query['path'] = {
                    'query': '/'.join(self.context.getPhysicalPath())}
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
