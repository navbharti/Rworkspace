from osgeo import gdal,gdalconst 
import struct

#As you can see, this program obtains the single raster band from the DEM file, and then reads through it one scanline at a time. We then use the struct standard Python library module to read the individual height values out of the scanline. Because the GLOBE dataset uses a special height value of -500 to represent the ocean, we exclude these values from our calculations. Finally, we use the remaining height values to calculate the average height, in meters, over the entire DEM data file.

#data source : https://www.ngdc.noaa.gov/mgg/topo/gltiles.html
#F:\backup from laptop\data\raster datasets
dataset = gdal.Open("F:/backup from laptop/data/raster datasets/g10g") 
band = dataset.GetRasterBand(1)
fmt = "<" + ("h" * band.XSize) 
totHeight = 0
for y in range(band.YSize):
    scanline = band.ReadRaster(0, y, band.XSize, 1, band.XSize, 1, band.DataType)
    values = struct.unpack(fmt, scanline)
    for value in values: 
        if value == -500:
    # Special height value for the sea -> ignore. continue
            totHeight = totHeight + value
    
average = totHeight / (band.XSize * band.YSize) 
print "Average height =", average