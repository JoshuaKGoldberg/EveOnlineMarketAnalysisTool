import csv
import requests

d = {}

with open('dict.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        d[row[0]] = row[1]

def findName(ID):
    return d[ID]

def findVolume(mode, ID):
    r = requests.get("http://api.eve-central.com/api/marketstat/json?typeid="+ID)
    d = r.json()[0]
    return d[mode]['volume']
def findWAvg(mode, ID):
    r = requests.get("http://api.eve-central.com/api/marketstat/json?typeid="+ID)
    d = r.json()[0]    
    return d[mode]['wavg']
def findAvg(mode, ID):
    r = requests.get("http://api.eve-central.com/api/marketstat/json?typeid="+ID)
    d = r.json()[0]    
    return d[mode]['avg']
def findVariance(mode, ID):
    r = requests.get("http://api.eve-central.com/api/marketstat/json?typeid="+ID)
    d = r.json()[0]
    return d[mode]['variance']
def findStdDev(mode, ID):
    r = requests.get("http://api.eve-central.com/api/marketstat/json?typeid="+ID)
    d = r.json()[0]    
    return d[mode]['stdDev']
def findMedian(mode, ID):
    r = requests.get("http://api.eve-central.com/api/marketstat/json?typeid="+ID)
    d = r.json()[0]    
    return d[mode]['median']
def findMax(mode, ID):
    r = requests.get("http://api.eve-central.com/api/marketstat/json?typeid="+ID)
    d = r.json()[0]    
    return d[mode]['max']
def findMin(mode, ID):
    r = requests.get("http://api.eve-central.com/api/marketstat/json?typeid="+ID)
    d = r.json()[0]    
    return d[mode]['min']

def execute(mode, ID, l):
    r = requests.get("http://api.eve-central.com/api/marketstat/json?typeid="+ID)
    d = r.json()[0]
    data = {}
    for item in l:
        if int(item) > 8:
            print item, "is not a valid choice"
        #Volume
        if item == "1":
            print "Volume:", d[mode]['volume']
            data['Volume'] = d[mode]['volume']
        #Weighted Average
        if item == "2":
            print "Weighted Average:", d[mode]['wavg']  
            data["Weighted Average"] = d[mode]['wavg'] 
        #Unweighted Average
        if item == "3":
            print "Unweighted Average:", d[mode]['avg'] 
            data["Unweighted Average"] = d[mode]['avg'] 
        #Variance
        if item == "4":
            print "Variance:", d[mode]['variance']
            data["Variance"] = d[mode]['variance']
        #Standard Deviation
        if item == "5":
            print "Standard Deviation:", d[mode]['stdDev'] 
            data["Standard Deviation"] = d[mode]['stdDev'] 
        #Median
        if item == "6":
            print "Median:", d[mode]['median']  
            data["Median"] = d[mode]['median']  
        #Max Price
        if item == "7":
            print "Max Price:", d[mode]['max']    
            data["Max"] = d[mode]['max']   
        #Min Price    
        if item == "8":
            print "Min Price:", d[mode]['min']
            data["Min"] = d[mode]['min']
    return data