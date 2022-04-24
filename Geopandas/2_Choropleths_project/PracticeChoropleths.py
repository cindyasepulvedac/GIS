# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:38:02 2022

@author: Core i5
"""
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd


shape_path = 'E:\Cindy\Ingeniería\Programming\RemoteSensing & GIS\
            Geopandas\2. Choropleths project\Data\statistical-gis-boundaries-london\
            ESRI\London_Borough_Excluding_MHW.shp.xml'
            
csv_path = 'RemoteSensing & GIS\Geopandas\2_Choropleths project\Data\london-borough-profiles.csv'
            
map_df = gpd.read_file(csv_path)