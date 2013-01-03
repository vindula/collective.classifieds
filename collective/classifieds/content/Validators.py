import re
from Products.validation.interfaces import ivalidator
from Products.validation.interfaces.IValidator import IValidator
from zope.interface import implements
from zope.i18n import translate

try:
    # Plone 4 and higher
    import plone.app.upgrade
    USE_BBB_VALIDATORS = False
except ImportError:
    # BBB Plone 3
    USE_BBB_VALIDATORS = True


class FloatValidator:
    """
       Class which provides us a simple validation check on a float
    """
    #__implements__ = (ivalidator,)
    if USE_BBB_VALIDATORS:
        __implements__ = (ivalidator,)
    else:
        implements(IValidator)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        """
            Validates the given value
        """
        FLOAT_RE = "^([+-]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$"

        if value:
            if re.match(FLOAT_RE, value):
                return 1
        else:
            return 1

        return translate('classifieds_invalid_float',
                         'classifieds')
