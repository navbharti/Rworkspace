import qgis.core
import qgis.gui

def TestWrite(iface):
    can = iface.mapCanvas()
    layer = can.currentLayer()
    geom = layer.selectedFeatures()[0].geometry()
    return geom.length()
    
print TestWrite(iface)