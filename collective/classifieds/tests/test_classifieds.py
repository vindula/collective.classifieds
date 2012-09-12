from collective.classifieds.tests.base import ClassifiedsTestCase
from zope.testing import doctestunit
from Testing import ZopeTestCase as ztc
import doctest
import unittest

def test_suite():
    """This sets up a test suite that actually runs the tests in classifieds_integration.txt"""
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite(
            'tests/classifieds_integration.txt', package='collective.classifieds',
            test_class=ClassifiedsTestCase),
        ])
