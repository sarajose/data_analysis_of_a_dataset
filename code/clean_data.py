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
    # Null values are maked either with [] for arrays and ? for strings therefore, there aren't any null values
    
    # Drop columns with personal information unecessary for data analysis
    df.drop(['Description', 'Telephone', 'Website', 'Email', 'Hiking association', 'Guard name(s)',
             'Acces', 'Zones', 'Emplacement'], axis=1, inplace=True)
    
    # Split place list in country, region, place
    df_new = df['Place list'].str.split(",", n = 3, expand = True)

    
    # Check unique values for each variable
    for column in df.columns:
        print(column + ": ", df[column].nunique())
    
    # Place type and fee are binary variables, name is unique for each row
    # Capacity, altitude and coordinates numerical and the rest are cathegorical
    

    


def main():    
    df = load_data()
    clean_data(df)

    
if __name__ == "__main__":
    main()
