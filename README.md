# Google Maps API Polyline String Decoder
This repo contains a Python function that will convert encoded polyline strings (as returned by the Google Maps API) into a list of lat/lon pairs.

It's a direct port of Mapbox's [JavaScript decode function](https://github.com/mapbox/polyline/blob/master/src/polyline.js#L40-L87) which is in turn 
based on [the official Google document](https://developers.google.com/maps/documentation/utilities/polylinealgorithm).

##Usage
```python
decode_polyline('azljFjss{S?oA?kB')
>>> [(38.57329, -109.55078), (38.57329, -109.55038), (38.57329, -109.54984)]
```

It's pretty straightforward.  I couldn't find an existing Python implementation when I looked so I decided to port one. 
