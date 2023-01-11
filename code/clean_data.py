# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:48:40 2023

@author: sara-
"""

import sys
import os
import pandas as pd
import numpy as np
    


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
        df[placelist] = df[placelist].str.replace('[', '')
        df[placelist] = df[placelist].str.replace(']', '')
        df[placelist] = df[placelist].str.replace('\'', '')

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
    df.rename(columns = {'Place type': 'place_type','Name':'name', 'Capacity':'capacity', 'Fee':'is_free', 'Altitude':'altitude'}, inplace = True)

    # Count the total number of routes of each place
    df['num_nearby_routes'] = df['Nearby routes'].str.split(",")
    df['num_nearby_routes']=[len(i) for i in df['num_nearby_routes']]

    # Change number of routes of empty values from 1 to 0 as they are incorreclty counted
    df.loc[df['Nearby routes'] == '[]', 'num_nearby_routes'] = 0

    # Count the total number of services of each place
    df['num_services'] = df['Services'].str.split(",")
    df['num_services']=[len(i) for i in df['num_services']]

    # Idem for number of services
    df.loc[df['Services'] == '[]', 'num_services'] = 0

    # Drop Services and Nearby routes columns
    df.drop(['Services', 'Nearby routes'], axis=1, inplace=True)

    # Delete unecessay characters and change columns to the right datatype for each column that hasn't been changed
    # capacity
    df['capacity'] = df['capacity'].str.replace('beds', '')
    df['capacity'] = df['capacity'].str.replace('?', '0')
    df['capacity'] = df['capacity'].astype('int64') 

    #altitude
    df['altitude'] = df['altitude'].str.replace('m', '')
    df['altitude'] = df['altitude'].str.replace('?', '0')
    df['altitude'] = df['altitude'].astype('int64') 
    
    return df