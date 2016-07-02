#The following example program uses OGR to read through the contents of a shapefile, printing out the value of the NAME attribute for each feature along with the geometry type

from osgeo import ogr
shapefile = ogr.Open("F:/backup from laptop/data/data for geospatial python/TM_WORLD_BORDERS-0.3/TM_WORLD_BORDERS-0.3.shp") 
layer = shapefile.GetLayer(0)
for i in range(layer.GetFeatureCount()): 
    feature = layer.GetFeature(i) 
    name = feature.GetField("NAME") 
    geometry = feature.GetGeometryRef() 
    print i, name, geometry.GetGeometryName()