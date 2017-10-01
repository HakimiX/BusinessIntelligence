import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py  # tools to communicate with Plotly's server
import plotly 
import readCSV as read
import plotly.graph_objs as go
#plotly.tools.set_credentials_file(username='Aimhow', api_key='')

def createHistogrambyZip(sales):
    
    fig = plt.figure(figsize=(80,15))
    x = []
    y = []
    for zip, numOfSales in sales.items():
        x.append(zip)
        y.append(numOfSales)
    
    plt.bar(x,y,align='center')
    
    fig.savefig('./histoByZip.png')

def createHistogramByRoomNum(sales):
    
    fig = plt.figure()
    
    zipInts = []
    roomsD = {}
    roomsColl = []
    y = 0
    
    for zip, roomD in sales.items():
        
        roomsAmount = []

        for rooms, amount in roomD.items():
            if (amount > y) : 
                y = amount
            roomsAmount.append(amount)
        roomsColl.append(roomsAmount)
        zipInts.append(zip)        
    
    roomsColl = np.asarray(roomsColl)
    bins = len(roomsColl)
    
    n, bins, patches = plt.hist(roomsColl, bins, normed=1, cumulative=True, histtype='bar', stacked=True)
    
    fig.savefig('./histoByRoomsNum.png')