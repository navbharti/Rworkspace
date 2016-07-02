#This code is applicable for Pont dataset
#First it loaded active point vector layer from canvas

#The QgsDistanceArea object accepts different types of geometry as input. In this case, we use two points. The map units for this layer are in decimal degrees, which isn't meaningful for a distance measurement. So, we use the QgsDistanceArea.convertMeasurement() method to covert the output to meters. The parameters for the method are the measurement output, the input units (in decimal degrees), the output units (meters), and a boolean to denote whether this conversion is an area calculation verses a linear measurement.

#The returned tuple is the measurement value and the units. The value 0 tells us that the output is in meters.
layer = iface.activeLayer()
#Ceated distanceAres object
d = QgsDistanceArea()
#Outer Loop through all the points
for feat1 in layer.getFeatures():
    #Inner Loop through all the points
    for feat2 in layer.getFeatures():
        #Measure the distance betweent two points
        m = d.measureLine(feat1.geometry().asPoint(), feat2.geometry().asPoint())
        #convert decimal distane to meter distance as explained above
        print d.convertMeasurement(m, 2, 0, False), feat1.id(), feat2.id()

    
    