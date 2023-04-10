import os
import glob
from datetime import datetime
from xml.dom.minidom import Document

from osgeo import gdal, osr

def get_lat_lon_box(geotiff_file):
    ds = gdal.Open(geotiff_file)
    gt = ds.GetGeoTransform()
    srs = osr.SpatialReference()
    srs.ImportFromWkt(ds.GetProjection())

    srs_lat_lon = srs.CloneGeogCS()
    ct = osr.CoordinateTransformation(srs, srs_lat_lon)

    (ulx, uly, _) = ct.TransformPoint(gt[0], gt[3])
    (lrx, lry, _) = ct.TransformPoint(gt[0] + gt[1] * ds.RasterXSize, gt[3] + gt[5] * ds.RasterYSize)

    return uly, lry, lrx, ulx

input_directory = 'd02'
output_directory = 'kml'

# Check if the input and output directories exist
if not os.path.exists(input_directory):
    raise FileNotFoundError(f"Input directory not found: {input_directory}")

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

geotiff_files = glob.glob(os.path.join(input_directory, 'flood_depth_20170[8|9]*.tif'))

if not geotiff_files:
    raise FileNotFoundError(f"No GeoTIFF files found in the input directory: {input_directory}")

kml_files = []
color_rules_file = 'color_rules.txt'

for geotiff_file in geotiff_files:
    print(f"Processing: {geotiff_file}")

    base_name = os.path.basename(geotiff_file)
    date_time_str = base_name[len('flood_depth_'):-len('.tif')]
    date_time = datetime.strptime(date_time_str, '%Y%m%d_%H%U')
    
    png_file = os.path.join(output_directory, f'{base_name[:-len(".tif")]}.png')
    kml_file = os.path.join(output_directory, f'{base_name[:-len(".tif")]}.kml')

    min_value = 0
    max_value = 255 # Use 65535 for UInt16
    data_type = 'Byte' # Use 'UInt16' for 16-bit data

    color_relief_file = os.path.join(output_directory, f'{base_name[:-len(".tif")]}_color_relief.tif')
    png_file = os.path.join(output_directory, f'{base_name[:-len(".tif")]}_color_relief.png')
    
    os.system(f'gdaldem color-relief {geotiff_file} {color_rules_file} {color_relief_file} -alpha')
    os.system(f'gdal_translate -of PNG {color_relief_file} {png_file}')
    
    timestamp = datetime.strptime(base_name, 'flood_depth_%Y%m%d_%H%M.tif')
    kml_timestamp = timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')

    if not os.path.exists(png_file):
        raise FileNotFoundError(f"PNG file not created: {png_file}")
    
    north, south, east, west = get_lat_lon_box(geotiff_file)

    with open(kml_file, 'w') as file:
        file.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <GroundOverlay>
    <TimeStamp>
      <when>{kml_timestamp}</when>
    </TimeStamp>
    <Icon>
      <href>{os.path.basename(png_file)}</href>
    </Icon>
    <LatLonBox>
      <north>{north}</north>
      <south>{south}</south>
      <east>{east}</east>
      <west>{west}</west>
    </LatLonBox>
  </GroundOverlay>
</kml>
""")
    kml_files.append(kml_file)

kml_files= glob.glob('kml/flood_depth*.kml')
# print(kml_files)

merged_kml_file = os.path.join(output_directory, 'merged.kml')

import lxml.etree as ET

# ...

doc = ET.Element('kml')
doc.set('xmlns', 'http://www.opengis.net/kml/2.2')

document_element = ET.SubElement(doc, 'Document')

for kml_file in kml_files:
    with open(kml_file, 'r') as file:
        kml_content = file.read()

    kml_tree = ET.fromstring(kml_content.encode('utf-8'))
    ground_overlay_element = kml_tree.find('.//{http://www.opengis.net/kml/2.2}GroundOverlay')

    if ground_overlay_element is not None:
        document_element.append(ground_overlay_element)

with open(merged_kml_file, 'wb') as file:
    file.write(ET.tostring(doc, pretty_print=True))
