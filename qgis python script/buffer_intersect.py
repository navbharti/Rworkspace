from qgis.core import *
from qgis.gui import *

canvas = qgis.utils.iface.mapCanvas()

layers = canvas.layers()
layer1 = canvas.layer(0)
layer2 = canvas.layer(3)

from qgis.analysis import *

#bool QgsOverlayAnalyzer::intersection	(	QgsVectorLayer * 	layerA,
#QgsVectorLayer * 	layerB,
#const QString & 	shapefileName,
#bool 	onlySelectedFeatures = false,
#QProgressDialog * 	p = nullptr 
#)		
#Perform an intersection on two input vector layers and write output to a new shape file.
#
#Parameters
#layerA	input vector layer
#layerB	input vector layer
#shapefileName	path to the output shp
#onlySelectedFeatures	if true, only selected features are considered, else all the features
#p	progress dialog (or 0 if no progress dialog is to be shown)
overlayAnalyzer = QgsOverlayAnalyzer()
overlayAnalyzer.intersection(layer1, layer2, "C:/Users/rajni/Desktop/Rworkspace/qgis python script/data/output.shp")

layer3 = canvas.layer(0)

#The QGis class provides vector geometry analysis functions.
#bool QgsGeometryAnalyzer::buffer	(	QgsVectorLayer * 	layer,
#const QString & 	shapefileName,
#double 	bufferDistance,
#bool 	onlySelectedFeatures = false,
#bool 	dissolve = false,
#int 	bufferDistanceField = -1,
#QProgressDialog * 	p = nullptr 
#)	

#Create buffers for a vector layer and write it to a new shape file.
#
#Parameters
#layer	input vector layer
#shapefileName	path to the output shp
#bufferDistance	distance for buffering (if no buffer field is specified)
#onlySelectedFeatures	if true, only selected features are considered, else all the features
#dissolve	if true, merge all the buffers to a big multipolygon
#bufferDistanceField	index of the attribute field that contains the buffer distance (or -1 if all features have the same buffer distance)
#p	progress dialog (or 0 if no progress dialog is to be shown)
geometryanalyzer = QgsGeometryAnalyzer()
geometryanalyzer.buffer(layer3, "C:/Users/rajni/Desktop/Rworkspace/qgis python script/data/bufferf.shp", .05, False, False, -1)
