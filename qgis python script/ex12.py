import osgeo.ogr 
#shapefile = osgeo.ogr.Open("F:/backup from laptop/data/testPointData.shp")
shapefile = osgeo.ogr.Open("F:/backup from laptop/data/india-latest.shp_3/places.shp")
layer = shapefile.GetLayer(0) 
feature = layer.GetFeature(2)
print "Feature 2 has the following attributes:" 
print
attributes = feature.items()
for key,value in attributes.items(): 
    print " %s = %s" % (key, value)
    
geometry = feature.GetGeometryRef() 
geometryName = geometry.GetGeometryName() 

print
print "Feature's geometry data consists of a %s" % geometryName