# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09, 2023
@author: Sara Jose, Joan Peracaula

"""
import os 
import sys
import pandas as pd
import clean_data
from data_integration import create_custom_DEM, integrate_elevations


# Set constant paths
SCRIPT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
PROJECT_ROOT_PATH = os.path.dirname(SCRIPT_PATH)
INITIAL_DATASET_PATH = os.path.join(PROJECT_ROOT_PATH, "data/initial_shelters_and_campsites.csv")
FINAL_DATASET_PATH = os.path.join(PROJECT_ROOT_PATH, "data/final_shelters_and_campsites.csv")


def main():  

    # Load initial dataset
    df = pd.read_csv(INITIAL_DATASET_PATH)
    
    # Select and clean data
    df = clean_data.clean_data(df)

    # Data integration
    create_custom_DEM() # Create a custom DEM of the geographical area of the dataset
    final_df = integrate_elevations(df) # Fill empty altitudes using the DEM and the data coords
    
    # Save the cleaned and preprocessed dataset, ready to analyse
    final_df.to_csv(FINAL_DATASET_PATH)


if __name__ == "__main__":
    main()
    