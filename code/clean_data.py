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
    df_placelist = df['Place list'].str.split(",", n = 3, expand = True)

    placelist = 'country', 'region', 'place'

    for i, placelist in enumerate(placelist):
        df[placelist] = df_placelist[i]
        df[placelist] = df[placelist].str.replace('Shelter in ', '')
        df[placelist] = df[placelist].str.replace('Campsite in ', '')

    df.drop(columns =['Place list'], inplace = True)

    # Split coordinates in latitude and longitude
    df['Coordinates'] = df['Coordinates'].str.replace('Latitude: ', '')

    df_coordinates = df['Coordinates'].str.split("Longitude: ", n = 2, expand = True)
        
    df['latitude']= df_coordinates[0]
    df['latitude'] = df['latitude'].astype('float64') 

    df['longitude']= df_coordinates[1]
    df['longitude'] = df['longitude'].astype('float64') 

    df.drop(columns =['Coordinates'], inplace = True)

    # Check unique values for each variable
    for column in df.columns:
        print(column + ": ", df[column].nunique())

    # Place type and fee are binary variables, name is unique for each row
    # Capacity, altitude and coordinates numerical and the rest are cathegorical


    # Change binary variables for True or False (0, 1)
    # Fee 0 is free 1 is paid
    df['Fee'].replace(['Paid','Free to use'],[0,1],inplace=True)
    # Place type 0 for Shelter and 1 for Campsite
    df['Place type'].replace(['Shelter','Campsite'],[0,1],inplace=True)

    # Change name columns
    df.rename(columns = {'Place type': 'place_type','Name':'name', 'Capacity':'capacity', 'Fee':'is_free', 'Altitude':'altitude', 'Services':'num_services', 
                         'Nearby routes':'num_nearby_routes'}, inplace = True)



def main():    
    df = load_data()
    clean_data(df)

    
if __name__ == "__main__":
    main()
