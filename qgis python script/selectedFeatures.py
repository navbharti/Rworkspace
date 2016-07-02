#Date: 31-05-2016
#Naveen Kumar
#Pondicherry University
#Department of Computer Science

#This code is for iterating through selected features of a layer from the QGIS canvas
layer = iface.activeLayer()
features = layer.selectedFeatures()
for f in features:
    print f.id()