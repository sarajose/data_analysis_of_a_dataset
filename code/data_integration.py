import os 
import sys
from rasterio.merge import merge
import rasterio
import numpy as np
from pathlib import Path


#--------------------------------------
# From multiple small raster images (such as SRTM, https://srtm.csi.cgiar.org/srtmdata/) merge them in a single coherent mosaic image, for later usage in a data integration process. 
#
# Source data: raster_data.zip. Contains multiple tif images with a DEM of Spain (including the Canary islands), Andorra and South of France, regions of the dataset. 
# Output data: single tif file as a DEM of these regions
#--------------------------------------


# Set constant paths
SCRIPT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
PROJECT_ROOT_PATH = os.path.dirname(SCRIPT_PATH)
RASTER_DATA_PATH = os.path.join(PROJECT_ROOT_PATH, "data/raster_data/")
DEM_PATH = os.path.join(PROJECT_ROOT_PATH, "data/custom_DEM.tif")


def create_custom_DEM():

    print("\n\n * * * START OF THE DATA INTEGRATION PROCESS * * * \n")
    print("As we have seen, there are many unknown altitude and capacity values in our data.\n")
    print("In this step we will fill empty altitude values integrating the data from a secondary realiable source:\n")
    
    print("\n- First, we will create a DEM image that covers our dataset geographical area")
    print("\nFrom multiple small regions DEM files downloaded from a realiable source, we merge them into a single DEM file\n")

    # Read individual raster files and merge them in a single raster image
    raster_files = list(Path(RASTER_DATA_PATH).iterdir())
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

    # The final elevations image is saved in the DEM_PATH
    with rasterio.open(DEM_PATH, "w", **output_meta) as m:
        m.write(mosaic)
    

def get_elevation(lat, lon, alt):

    # If the altitude is not NaN, keep the original value
    if not np.isnan(alt): 
        return alt
        
    # If it is 0, obtain and return the altitude value from the DEM
    coords = ((lon,lat), (lon,lat))
    with rasterio.open(DEM_PATH) as dem:
        vals = dem.sample(coords)
        elevation = next(vals)[0]

        if elevation == -32768: # For extreme values, set altitude as None (unknown)
            elevation = None

        return elevation
        

def integrate_elevations(df):

    print("\n- Then, for each NaN altitude value we get the (approximate) elevation from the DEM file")
    # Apply get_elevation function to all rows of the dataframe
    df["altitude"] = df.apply(lambda row : get_elevation(row["latitude"], row["longitude"], row["altitude"]), axis = 1)

    print("   ?? Number of rows with unknown altitude value after Data Integration: " + str(df['altitude'].isna().sum()) + "\n\n")

    return df
