#The steps for this recipe are fairly straightforward. We'll extract the geometry from the first line feature and pass it to the measurement object, as shown here:

#First, we must load the QGIS constants library:

from qgis.core import QGis
#Load the line layer:

lyr = QgsVectorLayer("/qgis_data/shapes/paths.shp", "Route", "ogr")
#Grab the features:

fts = lyr.getFeatures()
#Get the first feature:

route = fts.next()
#Create the measurement object instance:

d = QgsDistanceArea()
#Then, we must configure the QgsDistanceArea object to use the ellipsoidal mode for accurate measurements in meters:

d.setEllipsoidalMode(True)
#Pass the line's geometry to the measureLine method:

m = d.measureLine(route.geometry().asPolyline())
#Convert the measurement output to miles:

d.convertMeasurement(m, QGis.Meters, QGis.NauticalMiles, False)
#Ensure that your output looks similar to the following:

#(2314126.583384674, 7)
#How it works...

#The QgsDistanceArea object can perform any type of measurement, based on the method you call. When you convert the measurement from meters (represented by 0) to miles (identified by the number 7), you will get a tuple with the measurement in miles and the unit identifier. The QGIS API documentation shows the values for all the unit constants