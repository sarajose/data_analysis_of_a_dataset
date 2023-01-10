# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09, 2023
@author: Sara Jose, Joan Peracaula

"""

import clean_data

import sys
import os
import pandas as pd

def save_df(df):
    # Create path for the dataset
    script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    project_root_path = os.path.dirname(script_path)
    dataset_path = os.path.join(project_root_path, "data/cleaned_df.csv")
    print("Saving dataset to: " + dataset_path) 

    df.to_csv(dataset_path)

def main():  
    # Load dataser
    df = clean_data.load_data()
    
    # Select and clean data
    cleaned_df = clean_data.clean_data(df)
    #Save dataframe
    save_df(cleaned_df)
    
    # Data analysis
    
    # Graphs

if __name__ == "__main__":
    main()