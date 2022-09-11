# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:30:35 2022

@author: Core i5
"""
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

##Reading files
shp_path = r'E:/Cindy/Ingeniería/Programming/RemoteSensing & GIS/Geopandas/3. ANTIOQUIA_SUELOS_VF/ANTIOQUIA_SUELOS_VF/ANTIOQUIA_SUELOS_VF.shp'
ant_shp = gpd.read_file(shp_path)

##Droping duplicates
ant_shp_unique = ant_shp['COMPONENTE'].unique()
ant_shp_unique = ant_shp.drop_duplicates(subset='COMPONENTE')

##Plotting whole map
ant_shp.plot()
taxonomy = ant_shp['COMPONENTE']


##Plotting Choropleth
fig, ax = plt.subplots(1, figsize=(20,15))
ant_shp.plot(column='COMPONENTE', cmap='Blues', linewidth=0.8, ax=ax, \
             edgecolor='0.8', legend=True)
ax.axis('off')

#TODO it is necessary to discriminate for each polygon, according to soil taxonomy
#thus, it is possible to stablish a more accurate visualization of each taxonomy type



