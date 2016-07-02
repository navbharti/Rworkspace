#Date: 27-05-2016
#This programm accesses active layer from the QGIS canvas and loaded to layer variable.
#all features are extracted in features object that is further processes and appended to points list as points.
#Then iterated all the points with distance calculation.

#loaded sqrt module from math package using import
import math
import itertools

#accesses active layer and loaded to layer object.  Note in our case we have assumed only one layer is acitve of Point Geometry type.
layer = iface.activeLayer()
print "CRS: " + layer.crs().geographicCRSAuthId()

layer.setCrs(QgsCoordinateReferenceSystem(3395))
print "CRS: " + layer.crs().geographicCRSAuthId()
tr = QgsCoordinateTransform(4269, 3395)
print "CRS: " + layer.crs().geographicCRSAuthId()
#All features from layer object are extracted to features object.
features = layer.getFeatures()

#point object as list type
points = []

# points with list comprehension
points = [geom.geometry().asPoint() for geom in layer.getFeatures()]
# with itertools
for point1,point2 in itertools.combinations(points, 2):
    print point1, point2, QgsGeometry().fromPoint(point1).distance(QgsGeometry().fromPoint(point2))
    #print point1, point2, QgsGeometry().fromPoint(point1).distance(QgsGeometry().fromPoint(point2))