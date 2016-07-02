layer = iface.addVectorLayer("C:/Users/rajni/Downloads/data/india-latest.shp_3/places.shp", "India_places", "ogr")

# The expression will filter the features where the field "location_name" contains
# the word "Lake" (case insensitive)
exp = QgsExpression('name ILIKE \'%pur%\'')
request = QgsFeatureRequest(exp)
request.setFilterRect(areaOfInterest)
for feature in layer.getFeatures(request):
    # do whatever you need with the feature
        #geom = feature.geometry()
        print "Feature ID %d: " % feature.id()