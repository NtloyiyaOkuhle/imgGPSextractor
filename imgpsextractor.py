from __future__ import print_function
import argparse
import sys

from PIL import Image
from PIL.ExifTags import TAGS

import simplekml


parser = argparse.ArgumentParser(description='Metadata from images')
parser.add_argument('PICTURE_FILE', help="Path to picture")
args = parser.parse_args()

gmaps = "https://www.google.com/maps?q={},{}"
open_maps = "http://www.openstreetmap.org/?mlat={}&mlon={}"


def process_coords(coord):
    coord_deg = 0

    for count, values in enumerate(coord):
        coord_deg += (float(values[0]) / values[1]) / 60**count

    return coord_deg


img_file = Image.open(args.PICTURE_FILE)
exif_data = img_file._getexif()

if exif_data is None:
    print("No EXIF data found")
    sys.exit()

for name, value in exif_data.items():
    gps_tag = TAGS.get(name, name)

    if gps_tag != 'GPSInfo':
        continue

    lat_ref = value[1]
    lat = process_coords(value[2])

    if lat_ref == 'S':
        lat = -lat

    lon_ref = value[3]
    lon = process_coords(value[4])

    if lon_ref == 'W':
        lon = -lon

    kml = simplekml.Kml()
    kml.newpoint(name=args.PICTURE_FILE, coords=[(lon, lat)])
    kml.save(args.PICTURE_FILE + ".kml")

    print("GPS Coordinates: {}, {}".format(lat, lon))
    print("Google Maps URL: {}".format(gmaps.format(lat, lon)))
    print("OpenStreetMap URL: {}".format(open_maps.format(lat, lon)))
    print("KML File {} created".format(args.PICTURE_FILE + ".kml"))
