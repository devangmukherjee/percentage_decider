#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 00:23:32 2020

@author: devang
"""

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("key", help='paste your api key inside here')
args = parser.parse_args()
##################
# Your key here
api_key = args.key
##################
ts = TimeSeries(api_key, output_format='pandas')
stock_name = input("Enter correct stock name: ") 
data, meta_data = ts.get_daily(symbol='NSE:'+stock_name,outputsize='full')

#change this date if you want the testing period to be longer, right now it's from 1st jan,2020 till today
data = data[:'2020-01-01']

data.rename(columns = {'1. open':'open','2. high':'high','3. low':'low','4. close':'close','5. volume':'volume'}, inplace = True) 
op=input("Enter opening price for the day: ") 
op=int(op)
cp=input("Enter current price for the day: ") 
cp=int(cp)

points=int(cp-op)


#for points which are greater than zero
closed_above_points=0
closed_between_opennpoints=0
closed_below_open=0

pos_trigerred=0
if(points>=0):
    pos_trigerred=1
    for i in range(int(len(data))):
        price=data.iloc[i]['open']+points
        if(data.iloc[i]['close']>=price):
            closed_above_points+=1
        if(data.iloc[i]['close']<price and data.iloc[i]['close']>=data.iloc[i]['open']):
            closed_between_opennpoints+=1
        if(data.iloc[i]['close']<data.iloc[i]['open']):
            closed_below_open+=1

if(pos_trigerred==1):
    total=closed_above_points+closed_between_opennpoints+closed_below_open
    print("closed above points: "+str(round((closed_above_points/total)*100,2))+"%")
    print("closed between open and points: "+str(round((closed_between_opennpoints/total)*100,2))+"%")
    print("closed below open: "+str(round((closed_below_open/total)*100,2))+"%") 
    
    fig = plt.figure()
    ax = fig.add_axes([0,0,0.75,0.75])
    x = ['Above points', 'Between Open & Points', 'Below Open']
    y = [round((closed_above_points/total)*100,2),round((closed_between_opennpoints/total)*100,2),round((closed_below_open/total)*100,2)]
    ax.bar(x,y)
    plt.show()  


#for points which are negative
closed_below_points=0
closed_between_opennpoints=0
closed_above_open=0 

neg_triggered=0
if(points<0):
    neg_triggered=1
    for i in range(int(len(data))):
        price=data.iloc[i]['open']+points
        if(data.iloc[i]['close']<=price):
            closed_below_points+=1
        if(data.iloc[i]['close']>price and data.iloc[i]['close']<=data.iloc[i]['open']):
            closed_between_opennpoints+=1
        if(data.iloc[i]['close']>data.iloc[i]['open']):
            closed_above_open+=1
            
if(neg_triggered==1):
    total=closed_below_points+closed_between_opennpoints+closed_above_open
    print("closed below points: "+str(round((closed_below_points/total)*100,2))+"%")
    print("closed between open and points: "+str(round((closed_between_opennpoints/total)*100,2))+"%")
    print("closed above open: "+str(round((closed_above_open/total)*100,2))+"%") 
    
    fig = plt.figure()
    ax = fig.add_axes([0,0,0.75,0.75])
    x = ['Below points', 'Between Open & Points', 'Above Open']
    y = [round((closed_below_points/total)*100,2),round((closed_between_opennpoints/total)*100,2),round((closed_above_open/total)*100,2)]
    ax.bar(x,y)
    plt.show()   
    


        
            
        
    
