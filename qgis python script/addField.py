#Add a Field to an Existing Shapefile
#http://geospatialpython.com/2013/04/add-field-to-existing-shapefile.html
import shapefile

# Read in our existing shapefile
r = shapefile.Reader("Mississippi")

# Create a new shapefile in memory
w = shapefile.Writer()

# Copy over the existing fields
w.fields = list(r.fields)

# Add our new field using the pyshp API
w.field("KINSELLA", "C", "40")

# We'll create a counter in this example
# to give us sample data to add to the records
# so we know the field is working correctly.
i=1

# Loop through each record, add a column.  We'll
# insert our sample data but you could also just
# insert a blank string or NULL DATA number
# as a place holder
for rec in r.records():
 rec.append(i)
 i+=1
 # Add the modified record to the new shapefile 
 w.records.append(rec)

# Copy over the geometry without any changes
w._shapes.extend(r.shapes())

# Save as a new shapefile (or write over the old one)
w.save("Miss") 