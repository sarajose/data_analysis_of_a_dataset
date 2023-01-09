# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09, 2023
@author: Sara Jose, Joan Peracaula

"""

import clean_data

def main():  
    # Load dataser
    df = clean_data.load_data()
    
    # Select and clean data
    cleaned_df = clean_data.clean_data(df)
    
    # Data analysis
    
    # Graphs

if __name__ == "__main__":
    main()