#In this recipe, we'll create a spatial index for a point layer and then we'll use it to perform a spatial query, as follows:

#Function Name: idToGeom()
#Arguments: list of  feature ids
#Return: list of point features
#This function prints point features of the given list of feature ids
def idToGeom(ids):
    points = []
    fts = lyr.getFeatures()
    i = 0
    print "Hood : ",hood
    for feature in fts:
        for id in ids:
            if feature.id() == id:
                points.append(feature.geometry().asPoint())
                #print feature.id(), feature.geometry().asPoint()
        
    #print distPoints(points)
    #print "------------------------------------------------------------------------", points
    return points

   
#Function Name: distPoints()
#Arguments: list of  point features
#Return: Total distance among points
#This function prints point features of the given list of feature ids
def distPoints(points):
    totPoints = len(points)
    totDist = 0.0
    #Ceated distanceAres object
    d = QgsDistanceArea()
    #Outer Loop through all the points
    for point in points:
        #Measure the distance betweent two points
        m = d.measureLine(points[0], point)
        #convert decimal distane to meter distance as explained above
        dist = d.convertMeasurement(m, 2, 0, False)
        #print dist
        totDist = totDist + dist[0]
    #print "Total Distance Among Point Set : ", totDist
    #print "Average Distance : ", (totDist / totPoints)
    return (totDist/totPoints -1) / 1000
        





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
featureCount = 0
for f in fts:
  index.insertFeature(f)
  featureCount = featureCount + 1

#Now, select the IDs of 3 points nearest to the first point. We use the number 4 because the starting point is included in the output:
print "Loop for neighbors"
hoods = []
pointSet = []
fts = lyr.getFeatures()
for feature in fts:
    #hood = index.nearestNeighbor(first.geometry().asPoint(), 4)
    hood = index.nearestNeighbor(feature.geometry().asPoint(), 5)
    hoods.append(hood)
    #print "==================================================", hood
    pointSet = idToGeom(hood)
    #print pointSet
    print distPoints(pointSet)
    #print hood
    
#print hood
#print "Loop through all neighbors"
#for h in hoods:
    #print h
#How it works...





#The index speeds up spatial operations. However, you must add each feature one by one. Also, note that the nearestNeighbor() method returns the ID of the starting point as part of the output. So, if you want 4 points, you must specify 5.