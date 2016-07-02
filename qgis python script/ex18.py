#The following example starts with a location specified using UTM zone 17 coordinates. Using two Proj objects to define the UTM Zone 17 and lat/long projections, it translates this location's coordinates into latitude and longitude values:

import pyproj
UTM_X = 565718.5235 
UTM_Y = 3980998.9244
srcProj = pyproj.Proj(proj="utm", zone="11", ellps="clrk66", units="m")
dstProj = pyproj.Proj(proj="longlat", ellps="WGS84", datum="WGS84") 
long,lat = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)

print "UTM zone 11 coordinate (%0.4f, %0.4f) = %0.4f, %0.4f" % (UTM_X, UTM_Y, lat, long)

angle = 315 # 315 degrees = northeast. 
distance = 10000 
geod = pyproj.Geod(ellps="WGS84") 
long2,lat2,invAngle = geod.fwd(long, lat, angle, distance)
print "%0.4f, %0.4f is 10km northeast of %0.4f, %0.4f" \ % (lat2, long2, lat, long)