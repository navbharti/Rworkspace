layer = iface.addVectorLayer("C:/Users/rajni/Downloads/data/india-latest.shp_3/places.shp", "India_places", "ogr")
selection = layer.selectedFeatures()
print len(selection)
for feature in selection:
    # do whatever you need with the featfure