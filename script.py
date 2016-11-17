#!/usr/bin/python3

import overpass
import geojson
import urllib.request
import zipfile
import kml2geojson.kml2geojson
import os
from click.testing import CliRunner

api = overpass.API()

# Coastline data
with open('data/singkep-coastline.geojson', 'w') as f:
    overpass_query_singkep_coastline = """
    way(160688580)
    """
    res = api.Get(overpass_query_singkep_coastline)
    f.write(geojson.dumps(res, sort_keys=True))

# Village data
with open('data/singkep-village.geojson', 'w') as f:
    overpass_singkep_village = """
        node[place=village]["is_in:country"="Indonesia"]["is_in:county"="Singkep"];
    """
    res = api.Get(overpass_singkep_village)
    f.write(geojson.dumps(res, sort_keys=True))

# Mountain data
with open('data/singkep-mountain.geojson', 'w') as f:
    overpass_singkep_mountain = """
    node(1070184408)
    """
    res = api.Get(overpass_singkep_mountain)
    f.write(geojson.dumps(res, sort_keys=True))

# Lahan kritis data
dephut_lahan_kritis_url = "http://appgis.dephut.go.id/appgis/kml.aspx?status=view&filename=Sumatera_kml.zip&fileFullName=e:\webgis1\Peta%20Tematik%20Kehutanan1\KML\Lahan%20Kritis\Sumatera_kml.zip"
urllib.request.urlretrieve(dephut_lahan_kritis_url, "data/Sumatera.kml.zip")
zipfile.ZipFile("data/Sumatera.kml.zip").extract("data/Sumatera.kml")
runner = CliRunner()
runner.invoke(kml2geojson.kml2geojson.main, ["data/Sumatera.kml", "./data"])

# Filter only singkep island lahan kritis data
with open('data/Sumatera.geojson', 'r') as f:
    data = geojson.loads(f.read())
    relevant_lahan_kritis = [7571, 9477, 9190, 9089, 9155, 10102, 9358, 7145, 7085, 912, 3439, 7144, 9014, 3438, 9013, 43, 6246, 15, 3452, 9215, 6249, 48, 47, 9029, 46, 103, 6244, 6245, 6263, 3419, 3420, 50, 6248, 3451, 9028, 6178, 897, 9024, 49, 9027, 9354, 104, 6250, 898, 6179, 896, 14, 6232, 12296, 7439, 26, 3434, 3429, 7443, 9129, 3422, 3456, 6181, 3421, 12294, 9276, 7570, 11875, 99, 98, 84, 9361, 3693, 10106, 9249, 12137, 7406, 7451, 6214, 38, 89, 7459, 7455, 9214, 13, 6224, 6225, 19, 9133, 12286, 12285, 9212, 10118, 3418, 20, 9213, 3428, 16, 12300, 6239, 3391, 9039, 9, 6256, 6255, 7454, 6254, 3390, 7437, 95, 7514, 7256, 3392, 6257, 93, 7447, 7424, 100, 3609, 12299, 7444, 92, 7141, 12139, 7407, 97, 12302, 7392, 9211, 3558, 7567, 9269, 9149, 94, 9150, 9121, 7314, 9357, 7402, 12179, 91, 9357, 9210, 7405]
    # The id in geojson file is in string format
    relevant_lahan_kritis = [str(s) for s in relevant_lahan_kritis]
    lahan_kritis = []
    for feature in data["features"]:
        if feature["properties"]["name"] in relevant_lahan_kritis:
            relevant_lahan_kritis.remove(feature["properties"]["name"])
            lahan_kritis.append(feature)
    geojson_lahan_kritis = geojson.FeatureCollection(lahan_kritis)

    with open('data/singkep-lahan-kritis.geojson', 'w') as f:
        f.write(geojson.dumps(geojson_lahan_kritis))


# Clean unused file
os.remove('data/Sumatera.kml')
os.remove('data/Sumatera.kml.zip')
os.remove('data/Sumatera.geojson')
