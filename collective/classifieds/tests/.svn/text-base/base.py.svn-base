"""Test setup for integration and functional tests."""

from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
import os

@onsetup
def setup_product():
    """Set up the package and its dependencies."""
    fiveconfigure.debug_mode = True
    import collective.classifieds
    zcml.load_config('configure.zcml', collective.classifieds)
    fiveconfigure.debug_mode = False
    ztc.installPackage('collective.classifieds')
    
setup_product()
ptc.setupPloneSite(products=['collective.classifieds'])

class ClassifiedsTestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here. This applies to unit 
    test cases.
    """
    
