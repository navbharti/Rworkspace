#layer = iface.addVectorLayer("C:/Users/rajni/Downloads/data/IND_adm_shp/IND_adm3.shp", "India_places", "ogr")
layer = qgis.utils.iface.activeLayer()
import itertools
# with itertools permutations, length of the permutations(2) in this case.
for geom1,geom2 in itertools.permutations(layer.getFeatures(),r=2):
      if geom1.geometry().touches(geom2.geometry()):
            #print geom1.attributes(),geom2.attributes()
            print geom1.id(),geom2.id()
