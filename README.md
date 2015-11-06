# Google Maps API Polyline String Decoder
This repo contains a Python function that will convert encoded polyline strings (as returned by the Google Maps API) into a list of lat/lon pairs.  If you have arcpy, you can pass the steps object (`APIresponse['routes'][0]['legs'][0]['steps']`) to convert_to_shapefile() and it will create a polyline shapefile based on your route. 

decode_polyline() is a direct port of Mapbox's [JavaScript decode function](https://github.com/mapbox/polyline/blob/master/src/polyline.js#L40-L87) which is in turn 
based on [the official Google document](https://developers.google.com/maps/documentation/utilities/polylinealgorithm).

##Usage
To decode a polyline string into a list of lat/lon pairs, use decode_polyline():
```python
decode_polyline('azljFjss{S?oA?kB')
>>> [(38.57329, -109.55078), (38.57329, -109.55038), (38.57329, -109.54984)]
```

To convert a Maps API response to a shapefile, use convert_to_shapefile():
```python
# Get directions as JSON from the Maps API
APIresponse = get_google_directions('grand junction, co', 'moab, ut')

# Create shapefile based off the returned route
convert_to_shapefile(APIresponse['routes'][0]['legs'][0]['steps'], r"C:\routes\route.shp")
>>> 'C:\\routes\\route.shp'
```

It's pretty straightforward.  I couldn't find an existing Python implementation when I looked so I decided to port one. 
