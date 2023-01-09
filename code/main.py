# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09, 2023
@author: Sara Jose, Joan Peracaula

"""

import os
import sys
import pandas as pd

def load_data():
    
    # Create path for the dataset
    script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    project_root_path = os.path.dirname(script_path)
    dataset_path = os.path.join(project_root_path, "data/shelters_and_campsites.csv")    
    print("Loading dataset from: " + dataset_path) 
    
    # Load data
    df = pd.read_csv(dataset_path)
    return df

def main():
    
    df = load_data()

if __name__ == "__main__":
    main()