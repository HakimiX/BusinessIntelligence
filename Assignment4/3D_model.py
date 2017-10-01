import warnings
warnings.filterwarnings('ignore')
from mpl_toolkits.basemap import Basemap
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium
from contextlib import suppress
from mpl_toolkits.mplot3d import Axes3D
import datahandler as dh
import readCSV as read

def histogram_3d(zipcode_sales):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = []
    y = []
    for zip, no_of_sales in zipcode_sales.items():
        x.append(zip)
        y.append(no_of_sales)
    
    hist, xedges, yedges = np.histogram2d(x, y, bins=(7,7))
    xpos, ypos = np.meshgrid(xedges[:-1] + xedges[1:], yedges[:-1] + yedges[1:])
    
    xpos = xpos.flatten()/2
    ypos = ypos.flatten()/2
    zpos = np.zeros_like(xpos)
    
    dx = xedges [1] - xedges [0]
    dy = yedges [1] - yedges [0]
    dz = hist.flatten()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
    
    fig.savefig('zipcode_sales_3D.png')


def zipcode_trade(dataframe):
    
    unique_zips = dataframe['zip_int'].unique()
    unique_zips.sort()
    # Sorted by order of insertion, so we sort the zips first.
    zipcode_sales = collections.OrderedDict()
    
    for zip in unique_zips:
        no_of_sales = len(dataframe[dataframe['zip_int'] == zip])
        zipcode_sales[zip] = no_of_sales
        
    return zipcode_sales


def create_histogram_3d(dataframe):

    zipcode_sales = zipcode_trade(dataframe)
    histogram_3d(zipcode_sales)


def run():

    print ('Generate dataframe ')
    boliga_dataframe = read.read_csv_to_dataframe("boliga_all_loc.csv")
    boliga_dataframe = dh.createZipLabel(boliga_dataframe)

    create_histogram_3d(boliga_dataframe)
    

run()


