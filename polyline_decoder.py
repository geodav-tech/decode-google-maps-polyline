# This function is free of any dependencies.
def decode_polyline(polyline_str):
    '''Pass a Google Maps encoded polyline string; returns list of lat/lon pairs'''
    index, lat, lng = 0, 0, 0
    coordinates = []
    changes = {'latitude': 0, 'longitude': 0}

    # Coordinates have variable length when encoded, so just keep
    # track of whether we've hit the end of the string. In each
    # while loop iteration, a single coordinate is decoded.
    while index < len(polyline_str):
        # Gather lat/lon changes, store them in a dictionary to apply them later
        for unit in ['latitude', 'longitude']: 
            shift, result = 0, 0

            while True:
                byte = ord(polyline_str[index]) - 63
                index+=1
                result |= (byte & 0x1f) << shift
                shift += 5
                if not byte >= 0x20:
                    break

            if (result & 1):
                changes[unit] = ~(result >> 1)
            else:
                changes[unit] = (result >> 1)

        lat += changes['latitude']
        lng += changes['longitude']

        coordinates.append((lat / 100000.0, lng / 100000.0))

    return coordinates

# This function requires Esri's arcpy module.
def convert_to_shapefile(steps, output_shapefile):
    '''Pass the steps object returned by the Maps API (should be response['routes'][0]['legs'][0]['steps'])
    and an output shapefile path; outputs a detailed shapefile of that route'''
    
    import arcpy, os

    # Decode each step of the route; add those coordinate pairs to a list
    total_route = []
    for step in steps:
        total_route += decode_polyline(step['polyline']['points'])

    # Create empty WGS84 shapefile.
    sr = arcpy.SpatialReference(4326)
    arcpy.CreateFeatureclass_management(os.path.dirname(output_shapefile), os.path.basename(output_shapefile), 
        "POLYLINE", spatial_reference=sr)

    # Add points to array, write array to shapefile as a polyline
    arr = arcpy.Array()
    for coord_pair in total_route:
        arr.add(arcpy.Point(coord_pair[1], coord_pair[0]))
    with arcpy.da.InsertCursor(output_shapefile, ['SHAPE@']) as rows:
        rows.insertRow([arcpy.Polyline(arr)])
    del rows

    return output_shapefile
