import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
#Function for extracting data from the website
def get_data(str):
    data1=[]
    #Parsing data into HTML

    #try and catch block created for exception handling in case of connection timed out
    try:
        response=requests.get(str)
        soup=BeautifulSoup(response.content,"html.parser",'lxml')
        Scrape=soup.find_all("div",class_="form_school_record_wrap")
        for district in Scrape:
            data1["DISTRICT"]=district.find_all('option')
            
    #Scraping data from website
       # for district in Scrape:
        #    dict1={}
         #   dict1['DISTRICT']=district.find("div", class_="col-xs-15", id="district_div")
          #  data.append(dict1)
        #data1.append(data)
    except requests.exceptions.ConnectionError as e:
        r = "No response"
    
    
    return data1


#filename = 'district.csv'
#with open(filename, 'w', newline='') as f:
    #w = csv.DictWriter(f,['DISTRICT'])
    #w.writeheader()
    #str1=input()
    #data=get_data(str1)  
    #w.writerows(data)
    #df_new=pd.read_csv(filename)
    #excel = pd.ExcelWriter('district.xlsx')
    #df_new.to_excel(excel, index=False)
    #excel.save()

print(get_data("https://wbsaboojsathi.gov.in/v2/ss_search_student.php"))





