import warnings
warnings.filterwarnings('ignore')
from mpl_toolkits.basemap import Basemap
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium
import pylab as P
from contextlib import suppress
from mpl_toolkits.mplot3d import Axes3D
import datahandler as dh
import readCSV as read


def folium_plot(dataframe):

    temp_map = folium.Map(location=[55.88207495748612, 10.636574309440173], zoom_start=6)
    
    for coords in zip(dataframe.lon.values, 
                        dataframe.lat.values):
        if not np.isnan(coords[0]):
            folium.CircleMarker(location=[coords[1], coords[0]], radius=2).add_to(temp_map)

    temp_map.save('folium_plot_2d.png')


def dataframe_zipcodes(dataframe, zipcodes):

    return dataframe[dataframe['zip_int'].isin(zipcodes)]


def create_folium_plot(dataframe):

    zipcodes = []
    zipcodes.extend(range(1050,1549))
    zipcodes.extend([5000,8000,9000])

    folium_temp = dataframe_zipcodes(dataframe, zipcodes)

    folium_plot(folium_temp)


def run():

    print ('Generate dataframe ')
    boliga_dataframe = read.read_csv_to_dataframe("boliga_all_loc.csv")
    boliga_dataframe = dh.createZipLabel(boliga_dataframe)

    create_folium_plot(boliga_dataframe)

run()
