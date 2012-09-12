from setuptools import setup, find_packages
import os

version = '1.6'

setup(name='collective.classifieds',
      version=version,
      description="Add classifieds to your Plone intranet or website.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='classifieds sales intranet',
      author='Four Digits (ralph@fourdigits.nl)',
      author_email='ralph@fourdigits.nl',
      url='http://www.plone.org/products/classifieds',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
