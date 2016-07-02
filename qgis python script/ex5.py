layer = iface.activeLayer()
# QgsFields() of QgsVectorLayer()
# fields = layer.fields()  # from QGIS 1.12+
fields = layer.pendingFields()  # and below...

# list QgsField() from QgsFields()
fieldlist = fields.toList()

# list of layer fieldnames
[f.name() for f in fieldlist]

# field attributes
fattr = ('name', 'type', 'typeName', 'length', 'precision', 'comment')

# print the field table of a layer
for f in fieldlist:
  print '; '.join(['{!r}'.format(getattr(f, a)()) for a in fattr])