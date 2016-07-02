layer = iface.activeLayer()
features = layer.selectedFeatures()
print "Looping Through"
for feature in features:
    print feature.geometry().boundingBox().toString()