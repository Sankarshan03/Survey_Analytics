
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_data(str):
    #Parsing data
    response=requests.get(str)
    soup=BeautifulSoup(response.content,"html.parser")
    Scrape=soup.find_all(class_="form_school_record_wrap")
    dict={}
    #Scraping data from website
    for district in Scrape:
        dict['DISTRICT']=district.find_all("select",class_="form-control", id="district_code", name="district_code",onchange="district_load(this.value)")
    for Block in Scrape:
        dict['BLOCK']=Block.find_all("select",id="block_code" ,name="block_code", class_="form-control")
    for School in Scrape:
        dict['SCHOOL']=School.find_all("select",id="school_code", name="school_code", class_="form-control")
    for Phase in Scrape:
        dict['PHASE']=Phase.find_all("select", id="phase", name="phase", class_="form-control", onchange="phase_load(this.value)")
    for Class in Scrape:
        dict['CLASS']=Class.find_all("select", id="class_code", name="class_code" class_="form-control")
        




