layer = iface.activeLayer()
for f in layer.getFeatures():
  print f.geometry()
  print f["NAME_LOCAL"]