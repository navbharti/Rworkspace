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
pStart = QgsPoint( -0.743804, 0.22954 ) 
tiedPoint = director.makeGraph( builder, [ pStart ] ) 
pStart = tiedPoint[ 0 ]
graph = builder.graph() 
idStart = graph.findVertex( pStart ) 
tree = QgsGraphAnalyzer.shortestTree( graph, idStart, 0 )
i = 0; 
while ( i < tree.arcCount() ): 
    rb = QgsRubberBand( qgis.utils.iface.mapCanvas() ) 
    rb.setColor ( Qt.red ) 
    rb.addPoint ( tree.vertex( tree.arc( i ).inVertex() ).point() ) 
    rb.addPoint ( tree.vertex( tree.arc( i ).outVertex() ).point() ) 
    i = i + 1