#Function-Name: extractAttribute(attr)
#Return: featureType (Type List) This function returns a collection of values of a given attribute 
#Argument: attr (Type Number) is position of attribute 
def extractAttribute(attr):
    #shapefile = ogr.Open("F:/backup from laptop/data/data for geospatial python/Crime/Crime.shp")
    #layer = shapefile.GetLayer(0)
    layer = iface.activeLayer()
    features = layer.getFeatures()
    featureType = []
    for feature in features:
        #featureType.append( feature.attribute('OFFGEN'))
        featureType.append(feature[attr])
        
    return featureType
    #print len(featureType)

#Function-Name: list2Set(seq):
#Return: x (Type Set) This function returns a Set of values of a given attribute 
#Argument: seq (Type List)                  
def list2Set(seq): # Order preserving
  ''' Modified version of Dave Kirby solution '''
  seen = set()
  return [x for x in seq if x not in seen and not seen.add(x)]
  
#Function-Name: cluster2Transaction(classAttri)
#Return: transactions (Type Lists) This function returns a List of Lists of ids of a given attribute 
#Argument: classAttri (Type List) 
def cluster2Transaction(classAttri):
    #shapefile = ogr.Open("F:/backup from laptop/data/data for geospatial python/Crime/Crime.shp")
    #layer = shapefile.GetLayer(0)
    layer = iface.activeLayer()
    transactions = []
    transaction = []
    
    for classVal in range(len(classAttri)):
        for feature in layer.getFeatures():    
            if classAttri[classVal] == feature.attribute('class1000'):
                #print feature.id()
                transaction.append(feature.id())
    
        #print transaction
        transactions.append(transaction)
        transaction = []
        
    return transactions

#A function should be defined which will count the total Number of instances in a cluster
#A function should be defined which will calculate the participation ration of each feature in a cluster
#A function should be defined which will calculater the colocation on the basis of participation of features

offence = []  
#print 'Total:', len(extractAttribute())
offence= extractAttribute(8)
#print list2Set(offence)
classAttri = list2Set(offence)
classAttri= sorted(classAttri)
print classAttri
#data = cluster2Transaction(classAttri)
#print data[0]
#clustersSize = []
#cluster2Transaction(classAttri)

#This portion of code saves the output data of cluster2Transaction() in a text file
#target = open("F:/backup from laptop/data/data for geospatial python/Crime/CrimeTransaction.txt", 'w')
#for item in data:
#    clustersSize.append(len(item))
#    target.write("%s\n" % item)
#
#target.close()
#for l in clustersSize:
#    print l
                

