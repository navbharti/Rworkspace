def analyzeGeometry(geometry, indent=0): 
    s = []
    s.append(" " * indent)
    s.append(geometry.GetGeometryName())
    if geometry.GetPointCount() > 0:
        s.append(" with %d data points" % geometry.GetPointCount()) 
        
    if geometry.GetGeometryCount() > 0: 
        s.append(" containing:")
        
    print "".join(s)
    for i in range(geometry.GetGeometryCount()): 
        analyzeGeometry(geometry.GetGeometryRef(i), indent+1)
        
#In Case of Polygon        
shapefile = osgeo.ogr.Open("F:/backup from laptop/data/tl_2012_us_state/tl_2012_us_state.shp") 
#In Case of Point
#shapefile = osgeo.ogr.Open("F:/backup from laptop/data/india-latest.shp_3/places.shp") 
#In Case of PolylineMode
#shapefile = osgeo.ogr.Open("F:/backup from laptop/data/india-latest.shp_3/roads.shp") 
layer = shapefile.GetLayer(0) 
feature = layer.GetFeature(2) 
geometry = feature.GetGeometryRef()

analyzeGeometry(geometry)
