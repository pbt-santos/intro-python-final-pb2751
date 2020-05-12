# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:12:33 2020

@author: pbtsa
This file will be for displaying use of API requests
"""

# need to make http reqs
import requests
import pandas as pd

def drink_pairing(debug=False):
    # set the url and get a dataframe from it (for ease of converting to html
    # later)
    api_url = "https://api.punkapi.com/v2/beers/random"
    df = pd.read_json(requests.get(api_url).content)
    
    if debug:
        print(df)
        
    # return the list of columns we want without the index column
    return df.loc[:, ['name', 'description', 'food_pairing']].to_html(index=False)
    