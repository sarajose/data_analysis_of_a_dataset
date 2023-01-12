# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def clean_data(df):

    print("\n * * * START OF THE CLEANING PROCESS * * * \n")

    # Drop columns with personal information and such, unecessary for data analysis
    df.drop(['Description', 'Telephone', 'Website', 'Email', 'Hiking association', 'Guard name(s)',
             'Acces', 'Zones', 'Emplacement'], axis=1, inplace=True)
    print("\n- Dropped unnecessary variables for the data analysis \n")

    # Dataset information
    print("\n- Initial dataset information for the main variables: \n")
    df.info()

    # Check for NA and null values
    na_values = df.isna().sum()
    null_values = df.isnull().sum()

    print("\n\n- Number of Not Available (NA) values per variable: \n")
    print(na_values)

    print("\n\n- Number of Null values per variable: \n")
    print(null_values)

    # There aren't any NA nor Null values, but after visually inspection we can see that there are unknown or empty values 
    # These are maked either with [] for arrays or '?' for strings
    
    # Next, we are cleaning or processing each variable individually
    
    # Split Place list into country, region and place variables
    df_placelist = df['Place list'].str.split(",", n = 3, expand = True)

    placelist = 'country', 'region', 'place'

    for i, placelist in enumerate(placelist):
        df[placelist] = df_placelist[i]
        df[placelist] = df[placelist].str.replace('Shelter in ', '', regex=False)
        df[placelist] = df[placelist].str.replace('Campsite in ', '', regex=False)
        df[placelist] = df[placelist].str.replace('[', '', regex=False)
        df[placelist] = df[placelist].str.replace(']', '', regex=False)
        df[placelist] = df[placelist].str.replace('\'', '', regex=False)

    # Copy region to place for Andorra, since 'Place list' vars in Andorra only have two values
    mask = df['country'] == 'Andorra'
    df.loc[mask, "place"] = df.loc[mask, "region"]

    df.drop(columns =['Place list'], inplace = True)
    print("\n\n- Extracted country, region and place from the original string 'Place list' variable\n")

    # Split coordinates in latitude and longitude
    df['Coordinates'] = df['Coordinates'].str.replace('Latitude: ', '', regex=False)

    df_coordinates = df['Coordinates'].str.split("Longitude: ", n = 2, expand = True)
        
    df['latitude']= df_coordinates[0]
    df['latitude'] = df['latitude'].astype('float64') 

    df['longitude']= df_coordinates[1]
    df['longitude'] = df['longitude'].astype('float64') 

    df.drop(columns =['Coordinates'], inplace = True)
    print("\n- Extracted latitude and longitude from the original string 'Coordinates' variable\n")


    # Check unique values for each variable
    print("\n- Number of unique values per variable: \n")
    for column in df.columns:
        print(column + ": ", df[column].nunique())

    # Place type and fee are binary variables, name is unique for each row
    # Capacity, altitude, latitude and longitude are numerical and the rest are categorical


    # Change binary variables for True or False (0, 1)
    # Fee 0 is free 1 is paid
    df['Fee'].replace(['Paid','Free to use'],[0,1],inplace=True, regex=False)
    # Place type 0 for Shelter and 1 for Campsite
    df['Place type'].replace(['Shelter','Campsite'],[0,1],inplace=True, regex=False)
    print("\n\n- Fee and Place type binary variables have now 0,1 values instead of categorical labels\n")

    # Change name columns
    df.rename(columns = {'Place type': 'place_type','Name':'name', 'Capacity':'capacity', 'Fee':'is_free', 'Altitude':'altitude'}, inplace = True)
    print("\n- Variables names have been converted to 'snake_case'\n")


    # Count the total number of routes of each place
    df['num_nearby_routes'] = df['Nearby routes'].str.split(",")
    df['num_nearby_routes']=[len(i) for i in df['num_nearby_routes']]

    # Set to 0 num of nearby routes for those rows that had an empty list of routes
    df.loc[df['Nearby routes'] == '[]', 'num_nearby_routes'] = 0

    # Count the total number of services of each place
    df['num_services'] = df['Services'].str.split(",")
    df['num_services']=[len(i) for i in df['num_services']]

    # Differently from before, there are a lot of rows with empty Services
    # This could mean that this information not 0, but unknown
    # So we think it is better to set empty values as None
    df.loc[df['Services'] == '[]', 'num_services'] = None

    # Drop Services and Nearby routes columns
    df.drop(['Services', 'Nearby routes'], axis=1, inplace=True)
    print("\n- Services and Nearby routes variables have been converted to numeric vars indicating cardinality\n")


    # Delete unecessay characters and change columns to the right datatype for each column that hasn't been changed
    # capacity
    df['capacity'] = df['capacity'].str.replace('beds', '', regex=False)
    df['capacity'] = df['capacity'].str.replace('?', '-1', regex=False)  # Set unknown '?' capacity to -1 for later converting it to None
    df['capacity'] = df['capacity'].astype('int64') 
    df.loc[df['capacity'] == -1, 'capacity'] = None

    # altitude
    df['altitude'] = df['altitude'].str.replace('m', '', regex=False)
    df['altitude'] = df['altitude'].str.replace('?', '-1', regex=False) # Set unknown '?' capacity to -1 for later converting it to None
    df['altitude'] = df['altitude'].astype('int64') 
    df.loc[df['altitude'] == -1, 'altitude'] = None

    print("\n- Capacity and Altitude variables have been cleaned and transformed into int type")

    print("   · Number of rows with unknown altitude value: " + str(df['altitude'].isna().sum()))
    print("   · Number of rows with unknown capacity value: " + str(df['capacity'].isna().sum()))

    return df
    