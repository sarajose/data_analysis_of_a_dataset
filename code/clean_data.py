# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:48:40 2023

@author: sara-
"""

import sys
import os
import pandas as pd
import numpy as np
    
def load_data():
    
    # Create path for the dataset
    script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    project_root_path = os.path.dirname(script_path)
    dataset_path = os.path.join(project_root_path, "data/shelters_and_campsites.csv")    
    print("Loading dataset from: " + dataset_path) 
    
    # Load data
    df = pd.read_csv(dataset_path)
    return df

def clean_data(df):
    # Dataset information
    df.info()
    
    # Check for null values
    # Mirar si hi ha valors nuls
    df.isna().sum()
    df.isnull().any()


