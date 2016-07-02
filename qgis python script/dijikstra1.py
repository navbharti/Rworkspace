from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import * 
from qgis.gui import * 
from qgis.networkanalysis import *
vl = qgis.utils.iface.mapCanvas().currentLayer() 
director = QgsLineVectorLayerDirector( vl, -1, '', '', '', 3 ) 
properter = QgsDistanceArcProperter() 
director.addProperter( properter ) 
crs = qgis.utils.iface.mapCanvas().mapRenderer().destinationCrs() 
builder = QgsGraphBuilder( crs )
#New Delhi (28.6457559,76.8105545)
#Chennia (13.0480788,79.9288037)
pStart = QgsPoint( 76.8105545, 28.6457559) 
pStop = QgsPoint(79.9288037, 13.0480788)
tiedPoints = director.makeGraph( builder, [ pStart, pStop ] ) 
graph = builder.graph()
tStart = tiedPoints[ 0 ] 
tStop = tiedPoints[ 1 ]
idStart = graph.findVertex( tStart ) 
idStop = graph.findVertex( tStop )
( tree, cost ) = QgsGraphAnalyzer.dijkstra( graph, idStart, 0 )
if tree[ idStop ] == -1: 
    print "Path not found"
else: 
    p = [] 
    curPos = idStop 
    while curPos != idStart: 
        p.append( graph.vertex( graph.arc( tree[ curPos ] ).inVertex() ).point() ) 
        curPos = graph.arc( tree[ curPos ] ).outVertex();
    p.append( tStart )
    rb = QgsRubberBand( qgis.utils.iface.mapCanvas() ) 
    rb.setColor( Qt.red )
    
    for pnt in p: 
        rb.addPoint(pnt)