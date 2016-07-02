vl = QgsVectorLayer("Polygon?crs=epsg:27700", "Welwyn Extent", "memory")
pr = vl.dataProvider()

fet = QgsFeature()
fet.setGeometry(QgsGeometry.fromRect(QgsRectangle(523000,211000,526000,215000)))
pr.addFeatures([fet])

QgsMapLayerRegistry.instance().addMapLayer(vl)