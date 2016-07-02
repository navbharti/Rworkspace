def getFeatures():
    if selectedOnly:
        return layer.selectedFeatures()
    else:
        return layer.getFeatures()
        
getFeatures()