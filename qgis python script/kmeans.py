# Performs K-Means clustering. Updates vector layer field.
#layer = vectorLayer
#fieldNames = []
#
#for feature in layer.getFeatures():
#    fields = layer.pendingFields()
#    for (k, field) in fields.iteritems():
#         fieldNames.append(field.name())
#

#Executed crime data with k=1000, total points=192311
#Local current time : time.struct_time(tm_year=2016, tm_mon=6, tm_mday=6, tm_hour=12, tm_min=46, tm_sec=23, tm_wday=0, tm_yday=158, tm_isdst=0)
#Local current time : time.struct_time(tm_year=2016, tm_mon=6, tm_mday=6, tm_hour=13, tm_min=41, tm_sec=43, tm_wday=0, tm_yday=158, tm_isdst=0)

from PyQt4.QtCore import *
#!/usr/bin/python
import time;

localtime = time.localtime(time.time())
print "Local current time :", localtime

def kmeans_clustering (vectorLayer, attributesList, normalize, clusterNumber, outputFieldName):
    from scipy.cluster.vq import kmeans,vq
    from numpy import array
    fullObjectsList = []
    features = vectorLayer.getFeatures()

    for feature in features:
        fullObjectsList.append([])
        for attribute in attributesList:
            if feature[attribute[0]]:
                fullObjectsList[len(fullObjectsList)-1].append(feature[attribute[0]])
            else:
                fullObjectsList[len(fullObjectsList)-1].append(0)

    #NORMALIZING
    if normalize:
        i = 0
        maxValues = []
        while i < len(attributesList):

            maxValues.append(max(abs(item[i]) for item in fullObjectsList))
            i += 1

        j = 0
        while j < len(fullObjectsList):
            i = 0
            while i < len(fullObjectsList[j]):
                fullObjectsList[j][i] = (fullObjectsList[j][i] * 1.0) / (maxValues[i] * 1.0)
                i += 1
            j += 1

    data = array(fullObjectsList)

    centroids,_ = kmeans(data, clusterNumber, 25)
    idx,_ = vq(data,centroids)
    idx = idx.tolist()
    vectorLayerDataProvider = vectorLayer.dataProvider()

    # Create field of not exist
    if vectorLayer.fieldNameIndex(outputFieldName) == -1:
        vectorLayerDataProvider.addAttributes([QgsField(outputFieldName, QVariant.Int)])

    vectorLayer.updateFields()
    vectorLayer.startEditing()
    attrIdx = vectorLayer.fieldNameIndex(outputFieldName)
    features = vectorLayer.getFeatures()

    i = 0
    for feature in features:
        vectorLayer.changeAttributeValue(feature.id(), attrIdx, int(idx[i]))
        i += 1

    vectorLayer.updateFields()
    vectorLayer.commitChanges()
    
    
vectorLayer = iface.activeLayer()
attributesList = ['X','Y']
normalize =0
clusterNumber = 270
outputFieldName ='class270'
kmeans_clustering (vectorLayer, attributesList, normalize, clusterNumber, outputFieldName)
localtime = time.localtime(time.time())
print "Local current time :", localtime