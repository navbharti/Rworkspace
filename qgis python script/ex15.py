#If you run the previous program, your computer will tell you the distance from the northernmost point to the southernmost point in California
import math
lat1 = 42.0095 
long1 = -122.3782
lat2 = 32.5288 
long2 = -117.2049
rLat1 = math.radians(lat1)
rLong1 = math.radians(long1) 
rLat2 = math.radians(lat2) 
rLong2 = math.radians(long2)
dLat = rLat2 - rLat1 
dLong = rLong2 - rLong1

#we are converting the latitude and longitude values to radians, calculating the difference in latitude/ longitude values between the two points, and then passing the results through some trigonometric functions to obtain the great circle distance. The value of 6371 is the radius of the earth, in kilometers.
a = math.sin(dLat/2)**2 + math.cos(rLat1) * math.cos(rLat2)  * math.sin(dLong/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) 
distance = 6371 * c
print "Great circle distance is %0.0f kilometres" % distance

#We can also do 
#• The easternmost and westernmost points in California.
#• The midpoint in California. Hint: you can calculate the midpoint's longitude by taking the average of the easternmost and westernmost longitude.
#• The midpoint in Arizona. • The distance between the middle of California and the middle of Arizona