# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:38:02 2022

@author: Core i5
"""
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

##Setting files path
shape_path = r"E:/Cindy/Ingeniería/Programming/RemoteSensing & GIS/Geopandas/2_Choropleths_project/Data/statistical-gis-boundaries-london/ESRI/London_Borough_Excluding_MHW.shp"         
csv_path = r'E:/Cindy/Ingeniería/Programming/RemoteSensing & GIS/Geopandas/2_Choropleths_project/Data/london-borough-profiles.csv'

##Reading files           
map_df = gpd.read_file(shape_path)
csv_df = pd.read_csv(csv_path, header=0, encoding='cp1252')

##Dataframes characteristics
csv_columns = list(csv_df.columns)


##Test dataframe without data
no_data_map = map_df.plot()


##Selecting a slice of the data
df_slice = csv_df[['Area_name',
                   'Happiness_score_2011-14_(out_of_10)',
                   'Anxiety_score_2011-14_(out_of_10)', 
                   'Population_density_(per_hectare)_2017', 
                   'Mortality_rate_from_causes_considered_preventable_2012/14']]

##Modifying column names
df_slice = df_slice.rename(columns={
    'Area_name':'borough', 
    'Happiness_score_2011-14_(out_of_10)':'happiness',
    'Anxiety_score_2011-14_(out_of_10)':'anxiety', 
    'Population_density_(per_hectare)_2017':'pop_density_per_hectare',
    'Mortality_rate_from_causes_considered_preventable_2012/14':'mortality'
    })

##Merge Geodataframe and csv_slice
merged_df = map_df.set_index('NAME').join(df_slice.set_index('borough'))
merged_df = df_slice.rename(columns={'NAME':'borough'})