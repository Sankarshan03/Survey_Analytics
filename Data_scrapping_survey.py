import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
#Function for extracting data from the website
def get_data(str):
    #Parsing data into HTML
    response=requests.get(str)
    soup=BeautifulSoup(response.content,"html.parser")
    Scrape=soup.find_all("div",class_="form_school_record_wrap")
    data=[]
    #Scraping data from website
    for district in Scrape:
        dict1={}
        dict1['DISTRICT']=district.find("div", class_="col-xs-15", id="district_div")
        data.append(dict1)
    
    #for Block in Scrape:
        #dict2={}
        #dict2['BLOCK']=Block.find("select",id="block_code" ,name="block_code", class_="form-control")
        #data.append(dict2)
    #for School in Scrape:
        #dict3={}
        #dict3['SCHOOL']=School.find("select",id="school_code", name="school_code", class_="form-control")
        #data.append(dict3)
    #for Phase in Scrape:
        #dict4={}
        #dict4['PHASE']=Phase.find("select", id="phase", name="phase", class_="form-control", onchange="phase_load(this.value)")
        #data.append(dict4)
    #for Class in Scrape:
        #dict5={}
        #dict5['CLASS']=Class.find("select", id="class_code", name="class_code", class_="form-control")
        #data.append(dict5)
    return data
    ###

filename = 'district.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['DISTRICT'])
    w.writeheader()
    str1=input()
    data=get_data(str1)  
    w.writerows(data)


    







