import warnings
warnings.filterwarnings('ignore')
from mpl_toolkits.basemap import Basemap
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium
import math
from contextlib import suppress
from mpl_toolkits.mplot3d import Axes3D
import datahandler as dh
import readCSV as read


def haversine_location(dataframe):

    print('in haversine_location')

    return dataframe.apply(lambda row: haversine_distance(row), axis=1)


def haversine_distance(row):

    print('in haversine distance')

    lat_orig, lon_orig = (55.676111,12.568333)
    lat_dest = row['lat']
    lon_dest = row['lon']
    
    radius = 6371

    dlat = math.radians(lat_dest-lat_orig)
    dlon = math.radians(lon_dest-lon_orig)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat_orig)) 
        * math.cos(math.radians(lat_dest)) * math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


def dataframe_year(dataframe, year):

    print('in dataframe_year')

    return dataframe[dataframe['sell_date'].dt.year == year]


def dataframe_zipcode(dataframe, zipcodes):

    print('in dataframe_zipcode')
    
    return dataframe[dataframe['zip_int'].isin(zipcodes)]


def extended_zipcodes():

    zipcodes = []
    zipcodes.extend(range(1000,3670))
    zipcodes.extend(range(4000,4793))

    return zipcodes

def defined_city_plot(dataframe):

    dataframe = dataframe.assign(kilometer_defined_city = haversine_location(dataframe))

    y = dataframe['kilometer_defined_city'].values
    x = dataframe['price_per_sq_m'].values
    
    create_plot(x,y,'defined_city_sales')


def create_plot(x, y, name):

    fig = plt.figure()
    
    y[::-1].sort()
    x.sort()
    
    plt.plot(x,y,'ro')
    plt.gca().invert_yaxis()
    
    fig.savefig(name + '.png')


def create_defined_city_plot(dataframe):

    defined_year = dataframe_year(dataframe, 2005)
    defined_city_dataframe = dataframe_zipcode(dataframe, extended_zipcodes())
    defined_city_dataframe = defined_city_dataframe[defined_city_dataframe['price_per_sq_m'] >= 80.000]

    defined_city_plot(defined_city_dataframe)


def run():

    print ('Generate dataframe ')
    boliga_dataframe = read.read_csv_to_dataframe("boliga_all_loc.csv",{'year_of_construction': str, 'no_rooms': str})
    boliga_dataframe = dh.createZipLabel(boliga_dataframe)

    create_defined_city_plot(boliga_dataframe)


run()