Changelog
=========

1.6 - Release 1.6
----------------
* Tested with Plone 4.1.3
* Fixed i18n po files
* Added new and update translations, languages now in cs, en, es, fr, nl, pt-br, sv.

1.5.5 - Release 1.5.5
----------------
* Made add-on Plone 4.1 compatible
* Added Added Czech translations [naro]

1.5.4 - Release 1.5.4
----------------
* Fixed wrong price in classifieds by author view
* Minor template and CSS changes
* Code cleanup and PEP8/Pyflakes fixes

1.5.3 - Release 1.5.3
----------------
* Fixed deletion bug, owner could not delete their own classifieds

1.5.2 - Release 1.5.2
----------------
* Added spanish translations by David Torío Padrón

1.5.1 - Release 1.5.1
----------------
* Fixed broken template

1.5 - Release 1.5
----------------
* classified categories have body text, template changes
* classifieds container has body text, template changes
* cleaned up templates and code

1.5rc5 - Release candidate five
----------------
* fixed bug with float validator, issue #9

1.5rc4 - Release candidate four
----------------
* added french translation done by [nicolas_wicikowski]

1.5rc3 - Release candidate three
----------------
* fixed category tile image bug


1.5rc2 - Release candidate two
----------------
* allow normal categories to have images too
* url validation added to url field
* code cleanup


1.5rc1 - Release candidate one
----------------
* fixed permission bug
* release candidate one

1.5b4 - Bugfix and cleanup release
----------------
* fixed broken egg

1.5b3 - Bugfix and cleanup release
----------------
* collective.classifieds issue #7 fixed
* code cleanup, removed obsolete imports and general cleanup
* changed the way catalog indexes get created
* added external url to classified
* changed the way the deletion link works


1.5b2 - Plone 4 compatibilty and tests
----------------
* proper integration test added
* changed testbase
* update version information
* tested on plone 3.3 and plone 4




1.5b - Crossover release (beta)
----------------
* changed the validator to work in plone 3 and 4
  [maartenkling]
* upgr to work in plone 4
  [maartenkling]
* added global defines when needed to templates
  [maartenkling]
* changes folderish type definition of classifiedsCategory ( plone 4 )
  [maartenkling]
* changed the implements for validator ( plone 4 )
  [maartenkling]

* Fixed some issues regarding indexing of image urls, template calls
* Added view tab to Classified


1.5a - Crossover release (alpha)
----------------
* Crossover release which introduces two new contenttypes: OrderedClassifiedCategory and OrderedClassifieds (container)
* Custom order in Classifieds (container) and the Categories (read the INSTALL.txt)
* Multiple pictures for a classified
* 'E-mail the author' option
* Directlink to classified
* Picture and description added to Categories
* New templates / layout


1.0.1 - Release 1.0.1
----------------
* Added Brazilian Portugese translations [erico_andrei]


1.0 - Release 1.0
----------------
* Release 1.0 of the Classifieds plone addon product


1.0rc1 - Release candidate 2
----------------

* Changed workflow so anonymous users can view classifieds


1.0rc1 - Release candidate 1
----------------

* Cleaned up some code
* Added more documentationstrings
* Freeze of code
* Tested with Plone 3.3rc2


0.6.2 - Beta
----------------

* Cleaned up all pagetemplates
* Fixed bug when using multiple instances of Classifieds object (path bug)
* Fixed price formatting bug in 'by author view'
* Cleaned up python classes and added more documentation




0.6.1 - Beta
----------------

* Added custom workflow for a Classified, which allows users with the role member to add classifieds



0.6 - Beta
----------------

* Price field is not mandatory anymore
* Code cleanup
* Template fixes/formatting
* New validator added
* Translation files updates



0.5 - Beta
----------------

* Fixed translation files


0.4 - Alpha
----------------

* Fixed tiled images bug in templates
* Added formatting for the price values


0.3 - Alpha
----------------

* Fixed bug/issue skins.xml > skins directory


0.2 - Alpha
----------------

* Tested with plone 3.2
* Code cleanup and zcml cleanup
* Remove obsolete templates
* Added validation
* Fixed metadata information


0.1 - Alpha
----------------

* Initial release
