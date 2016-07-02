#Perform the following steps to measure the area of a large polygon:

#First, import the QGIS constants library, as follows:

from qgis.core import QGis
#Load the layer:

lyr = QgsVectorLayer("/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")
#Access the layer's features:

fts = lyr.getFeatures()
#Get the boundary feature:

boundary = fts.next()
#Create the measurement object instance:

d = QgsDistanceArea()
#Pass the polygon list to the measureArea() method:

m = d.measurePolygon(boundary.geometry().asPolygon()[0])
#Convert the measurement from decimal degrees to miles:

d.convertMeasurement(m, QGis.Degrees, QGis.NauticalMiles, True) 
#Verify that your output looks similar to the following:

#(42955.47889640281, 7)
#How it works...

#PyQIS has no measureArea() method, but it has a measurePolygon() method in the QgsDistanceArea object. The method accepts a list of points. In this case, when we convert the measurement output from decimal degrees to miles, we also specify True in the convertMeasurement() method so that QGIS knows that it is an area calculation. Note that when we get the boundary geometry as a polygon, we use an index of 0, suggesting that there is more than one polygon. A polygon geometry can have inner rings, which are specified as additional polygons. The outermost ring, in this case the only ring, is the first polygon.