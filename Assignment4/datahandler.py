
import pandas as pd
import math
import collections

def createZipLabel(dataframe):
    
    zip_df = pd.DataFrame(dataframe['zip_code'].str.split(' ',1).tolist(), columns = ['zip','city'])

    dataframe = dataframe.assign(zip_int=zip_df['zip'])
    dataframe['price_per_sq_m'] = pd.to_numeric(dataframe['price_per_sq_m'], errors='coerce')
    dataframe['zip_int'] = pd.to_numeric(dataframe['zip_int'], errors='coerce')
    
    return dataframe

def getFreqOfZip(dataframe):
    
    zips = dataframe['zip_int'].unique()
    zips.sort()
    sales = collections.OrderedDict()
    
    for zip in zips:
        nOfSales = len(dataframe[dataframe['zip_int'] == zip])
        sales[zip] = nOfSales
    return sales


def getFreqWithRoom(dataframe):
    
    zips = dataframe['zip_int'].unique()
    zips.sort()
    sales = collections.OrderedDict()
    
    roomRange = range(1,20)
    roomRange = [str(i) for i in roomRange]
    
    for zip in zips:
        zip_df = dataframe[dataframe['zip_int'] == zip]
        roomsD = {}
        for room_amount in roomRange:
            occurences = len(zip_df[zip_df['no_rooms'] == room_amount])
            roomsD[room_amount] = occurences
        sales[zip] = roomsD

    return sales