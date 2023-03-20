import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_data(str):
    #Parsing data
    response=requests.get(str)
    soup=BeautifulSoup(response.content,"html.parser")
    Scrape=soup.find_all(class_="form_school_record_wrap")

    #Scraping data from website
    for district in Scrape:
        dict={}
        dict['DISTRICT']=district.find_all("select",class_="form-control", id="district_code", name="district_code",onchange="district_load(this.value)")
    for Block in Scrape:
        dict1={}
        dict1['BLOCK']=Block.find_all("select",id="block_code" ,name="block_code", class_="form-control")
    for School in Scrape:
        dict2={}
        dict2['SCHOOL']=School.find
    Phase=
    Class=

