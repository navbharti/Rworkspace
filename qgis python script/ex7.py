# project
project_crs = qgis.utils.iface.mapCanvas().mapRenderer().destinationCrs()
crs = QgsCoordinateReferenceSystem("3395")
qgis.utils.iface.mapCanvas().mapRenderer().setDestinationCrs(crs)