# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:06:55 2020

@author: pbtsa
This file will be for the methods relating to the web crawler
"""
# need to interact with HTTP reqs, crawler code, pandas
import requests
import pandas as pd
import bs4

def url_to_medal_dataframe(url, table_loc, debug=False):
    ''' url is location to scrape 
        table_loc is which table from the site we want to get
        We return a dataframe from the converted request
    '''
    # get page content
    bs = bs4.BeautifulSoup(requests.get(url).content, 'lxml')
    
    # get tables from the html
    tables = bs.find_all('table')
    
    # get our specified medal table and display if debugging
    medals = pd.read_html(str(tables[table_loc]))[0]
    
    if debug:
        print(medals.head(5))
        
    return medals
    

# now have a function for merging the dataframes and getting stats
def retrieve_statistics(df1, df2, debug=False):
    # get list of column names apart from nation
    cols = df1.columns
    cols = cols[cols != 'Nation']

    # merge the two dataframes
    df_merged = pd.merge(df1, df2, on='Nation')
    
    if debug:
        print(df_merged.head(5))
        
    # convert the relevant columns to int
    df_merged.loc[:, df_merged.columns != 'Nation'] = df_merged.loc[:, 
                 df_merged.columns != 'Nation'].astype(int)

    # iterate over the columns and get 2015 vs 2017 differences
    for i, x in enumerate(cols):
        df_merged[x+"_diff"] = df_merged.loc[:, x+"_y"] - df_merged.loc[:, x+"_x"]
        df_merged.drop([x+"_x",x+"_y"], axis=1, inplace=True)

    # return the sorted dataframe in HTML
    return df_merged.sort_values(by="Rank_diff").to_html()
    

# finally, write the function that we will import to run the others
def medals_comparison(debug=False):
    url_pre = "https://en.wikipedia.org/wiki/2015_World_Rowing_Championships"
    url_post = "https://en.wikipedia.org/wiki/2017_World_Rowing_Championships"
    loc_pre = 1
    loc_post = 2
    
    df_pre = url_to_medal_dataframe(url_pre, loc_pre, debug)
    df_post = url_to_medal_dataframe(url_post, loc_post, debug)
    
    return retrieve_statistics(df_pre, df_post, debug)
    
