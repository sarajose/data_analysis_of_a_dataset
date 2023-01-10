import os 
import sys
from rasterio.merge import merge
import rasterio
from pathlib import Path
from zipfile import ZipFile


#--------------------------------------
# From multiple small raster images (such as SRTM, https://srtm.csi.cgiar.org/srtmdata/) merge them in a single coherent mosaic image, for later usage in a data integration process. 
#
# Source data: raster_data.zip. Contains multiple tif images with a DEM of Spain (including the Canary islands), Andorra and South of France, regions of the dataset. 
# Output data: single tif file as a DEM of these regions
#--------------------------------------


# Set paths
script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
project_root_path = os.path.dirname(os.path.dirname(script_path))
data_path = os.path.join(project_root_path, "data/")
zip_path = os.path.join(project_root_path, "data/raster_data.zip")
raster_data_path = os.path.join(project_root_path, "data/raster_data/")
output_path = os.path.join(project_root_path, "data/custom_dem.tif")

# Unzip raster files, previously downloaded and zipped from https://srtm.csi.cgiar.org/srtmdata/
ZipFile(zip_path).extractall(data_path)

# Read individual raster files and merge them in a single raster image
raster_files = list(Path(raster_data_path).iterdir())
raster_to_mosiac = []

for p in raster_files:
    raster = rasterio.open(p)
    raster_to_mosiac.append(raster)

mosaic, output = merge(raster_to_mosiac)

output_meta = raster.meta.copy()
output_meta.update(
    {"driver": "GTiff",
        "height": mosaic.shape[1],
        "width": mosaic.shape[2],
        "transform": output,
    }
)

with rasterio.open(output_path, "w", **output_meta) as m:
    m.write(mosaic)

# The final elevations image is saved in the 'data' directory as 'custom_dem.tif'
    
