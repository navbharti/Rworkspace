#processing.runalg('qgis:creategrid', type, width, height, hspacing, vspacing, centerx, centery, crs, output)
import processing
processing.runalg('qgis:creategrid', 0, 360, 180, 10, 10, 0.0, 0.0, 4326, "output.shp")