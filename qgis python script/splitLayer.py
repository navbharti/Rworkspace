#Date: 27-05-2016
#This programm accesses active layer from the QGIS canvas and loaded to layer variable.
#all features are extracted in features object that is further processes and appended to points list as points.
#Then iterated all the points with distance calculation.

#loaded sqrt module from math package using import
from math import sqrt

#accesses active layer and loaded to layer object.  Note in our case we have assumed only one layer is acitve of Point Geometry type.
layer = iface.activeLayer()

#All features from layer object are extracted to features object.
features = layer.getFeatures()

#point object as list type
points = []

#here all geometries are extracted from features asPoint and appended to points-list.
#we can replace this loop with
#points = [feature.geometry().asPoint() for feature in features]
for feature in features:
    geom = feature.geometry().asPoint()
    points.append(geom)

#store the total number of points in point-list in n variable
n = len(points)

#Here we have looped nesting for calculationg distance of all the points.
for i in range(n-1):
    for j in range(n):
        #condition that first point index in greated in point-list
        if i < j:
            print i, j, sqrt(points[i].sqrDist(points[j]))