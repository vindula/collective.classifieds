#!/bin/bash

echo "Syncing Collective.classifieds domain PO files..."
for PO in classifieds_??.po; do
  echo $PO
  i18ndude sync --pot classifieds.pot $PO
done
echo "done."
echo ""

echo "Syncing plone domain PO files..."
for PO in classifieds_plone_??.po; do
  echo $PO
  i18ndude sync --pot classifieds_plone.pot $PO
done
echo "done."
