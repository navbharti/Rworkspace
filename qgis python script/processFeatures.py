#layer = iface.addVectorLayer("F:/backup from laptop/data/india-latest.shp_3/places.shp", "India_places", "ogr")

iface.mapCanvas().mapRenderer().setDestinationCrs(QgsCoordinateReferenceSystem(4269 ))
layer1 = iface.activeLayer()
layer2 = iface.activeLayer()
import processing
features1 = processing.features(layer1)
features2 = processing.features(layer2)
print "Starting Before For Loop"
for geom1 in features1:
    # do whatever you need with the feature
    print "-------------------------Loop-----------------------------------"
    for geom2 in features2:
        #if geom1.geometry().nearestPoint(geom2.geometry()):
            print geom1.id(), geom2.id(), geom1.geometry().distance(geom2.geometry())
            #print geom1.geometry().within(geom2.geometry())
            #print 
    


print "End After For Loop"