#In this recipe, we'll create a spatial index for a point layer and then we'll use it to perform a spatial query, as follows:

#Load the layer:

#lyr = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
#Get the features:
lyr = iface.activeLayer()
fts = lyr.getFeatures()
#Get the first feature in the set:

first = fts.next()
#Now, create the spatial index:

index = QgsSpatialIndex()
#Begin loading the features:

index.insertFeature(first)
#Insert the remaining features:

for f in fts:
  index.insertFeature(f)
#Now, select the IDs of 3 points nearest to the first point. We use the number 4 because the starting point is included in the output:

hood = index.nearestNeighbor(first.geometry().asPoint(), 4)

print hood
for h in hood:
    print h
#How it works...

#The index speeds up spatial operations. However, you must add each feature one by one. Also, note that the nearestNeighbor() method returns the ID of the starting point as part of the output. So, if you want 4 points, you must specify 5.