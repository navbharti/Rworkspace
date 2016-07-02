layer = iface.addVectorLayer("C:/Users/rajni/Downloads/data/india-latest.shp_3/places.shp", "India_places", "ogr")
i = 0;
list = []
for feature in layer.getFeatures():
    # do whatever you need with the feature
        #geom = feature.geometry()
        #print "Feature ID %d: " % feature.id()
        list.append(feature.attribute("type"))
        i=i+1
print "Total Features: %d" %i
#print "Average Number of Features: %d" % i/len(set(list))
#print len(list)
set1 = set(list)
#print set1
type = int(len(set1))
avg = i / type
print "Average Number of Features: %d" % avg
print "Maximum number of type: %s" %max(list)
print "Minimum number of type: %s" %min(list)
print "Maximum number of type: %s" % list.count("yes")
#s = str(set1[1])
#print "type %s:" % s
#print "Maximum number of type: %s" % list.count(s)
for t in set1:
    print "%s : %d" %(t, list.count(t))