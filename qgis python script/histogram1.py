#If you run this, you will see a list of heights (in meters) and how many pixels there are at that height:
# histogram.py
import sys, struct 
from osgeo import gdal 
from osgeo import gdalconst

minLat = -48 
maxLat = -33
minLong = 165 
maxLong = 179

dataset = gdal.Open("F:/backup from laptop/data/raster datasets/l10g") 
band = dataset.GetRasterBand(1)
t = dataset.GetGeoTransform()
success,tInverse = gdal.InvGeoTransform(t) 
if not success: 
    print "Failed!" 
    sys.exit(1)
    
x1,y1 = gdal.ApplyGeoTransform(tInverse, minLong, minLat) 
x2,y2 = gdal.ApplyGeoTransform(tInverse, maxLong, maxLat)

minX = int(min(x1, x2)) 
maxX = int(max(x1, x2)) 
minY = int(min(y1, y2)) 
maxY = int(max(y1, y2))

width = (maxX - minX) + 1 
fmt = "<" + ("h" * width)
histogram = {} # Maps height to # pixels with that height.

for y in range(minY, maxY+1):
    scanline = band.ReadRaster(minX, y,width, 1, width, 1,gdalconst.GDT_Int16)
    values = struct.unpack(fmt, scanline) 
    for value in values:
        if value != band.GetNoDataValue():
            try:
                histogram[value] += 1 
            except KeyError:
                histogram[value] = 1 
 
#"Every tile contains values of -500 for oceans, with no values between -500 and the minimum value for land noted here." 
for height in sorted(histogram.keys()): 
    print height,histogram[height]