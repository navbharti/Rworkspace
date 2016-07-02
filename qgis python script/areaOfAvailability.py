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
#Chennai = QgsPoint( 76.8105545, 28.6457559) 
pStart = QgsPoint( 76.8105545, 28.6457559 ) 
delta = qgis.utils.iface.mapCanvas().getCoordinateTransform().mapUnitsPerPixel() * 1
rb = QgsRubberBand( qgis.utils.iface.mapCanvas(), True ) 
rb.setColor( Qt.green ) 
rb.addPoint( QgsPoint( pStart.x() - delta, pStart.y() - delta ) ) 
rb.addPoint( QgsPoint( pStart.x() + delta, pStart.y() - delta ) ) 
rb.addPoint( QgsPoint( pStart.x() + delta, pStart.y() + delta ) ) 
rb.addPoint( QgsPoint( pStart.x() - delta, pStart.y() + delta ) )
tiedPoints = director.makeGraph( builder, [ pStart ] ) 
graph = builder.graph() 
tStart = tiedPoints[ 0 ]
idStart = graph.findVertex( tStart ) 
( tree, cost ) = QgsGraphAnalyzer.dijkstra( graph, idStart, 0 )
upperBound = [] 
r = 2000.0 
i = 0 
while i < len(cost): 
    if cost[ i ] > r and tree[ i ] != -1: 
        outVertexId = graph.arc( tree [ i ] ).outVertex() 
        if cost[ outVertexId ] < r: 
            upperBound.append( i )
    i = i + 1
    
for i in upperBound: 
    centerPoint = graph.vertex( i ).point() 
    rb = QgsRubberBand( qgis.utils.iface.mapCanvas(), True ) 
    rb.setColor( Qt.red ) 
    rb.addPoint( QgsPoint( centerPoint.x() - delta, centerPoint.y() - delta ) ) 
    rb.addPoint( QgsPoint( centerPoint.x() + delta, centerPoint.y() - delta ) ) 
    rb.addPoint( QgsPoint( centerPoint.x() + delta, centerPoint.y() + delta ) ) 
    rb.addPoint( QgsPoint( centerPoint.x() - delta, centerPoint.y() + delta ) )