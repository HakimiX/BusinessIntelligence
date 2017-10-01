import readCSV as read
import histogram as plt
import datahandler as dh
import os





def run():
    
    
    
    print ('Generate dataframe ')
    boliga_dataframe = read.read_csv_to_dataframe("boliga_all_loc.csv",{'year_of_construction': str, 'no_rooms': str})
    boliga_dataframe = dh.createZipLabel(boliga_dataframe)


    
    print('histogram by room nums')
    #hisramRoomNum(boliga_dataframe)
    #hisramByZip(boliga_dataframe)
    
    
    
    
    
def hisramRoomNum(df):
    histoData = dh.getFreqWithRoom(df)
    plt.createHistogramByRoomNum(histoData) 

def hisramByZip(df):
    sales = dh.getFreqOfZip(dataframe)
    histogram.creeateHistogramByZip(sales)




run()