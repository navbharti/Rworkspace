from PyQt4.QtCore import QVariant

layer = iface.addVectorLayer("C:/Users/rajni/Downloads/data/IND_adm_shp/IND_adm0.shp", "India", "ogr")
if not layer:
  print "Layer failed to load!"
  
  # "layer" is a QgsVectorLayer instance
  #Retrieving information about attributes
for field in layer.pendingFields():
    print field.name(), field.typeName()
    
iface.mapCanvas().setSelectionColor( QColor("red") )

# Get the active layer (must be a vector layer)
layer1 = iface.activeLayer()
# Get the first feature from the layer
feature = layer1.getFeatures().next()
# Add this features to the selected list
layer1.setSelectedFeatures([feature.id()])


