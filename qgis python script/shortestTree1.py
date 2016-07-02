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
tree = QgsGraphAnalyzer.shortestTree( graph, idStart, 0 )
idStart = tree.findVertex( tStart ) 
idStop = tree.findVertex( tStop )
if idStop == -1: 
    print "Path not found"
else: 
    p = [] 
    while ( idStart != idStop ): 
        l = tree.vertex( idStop ).inArc() 
        if len( l ) == 0: 
            break
        e = tree.arc( l[ 0 ] ) 
        p.insert( 0, tree.vertex( e.inVertex() ).point() ) 
        idStop = e.outVertex()
    p.insert( 0, tStart ) 
    rb = QgsRubberBand( qgis.utils.iface.mapCanvas() ) 
    rb.setColor( Qt.red )
    
    for pnt in p: 
        rb.addPoint(pnt)