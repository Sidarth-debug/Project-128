from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import requests
import pandas as pd

website = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
op = requests.get(website)
#print(op)
soup = BeautifulSoup(op.text,'html.parser')
table1 = soup.find('table')

temp_list = []
table_rows = table1.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row1 = [i.text.rstrip() for i in td]
    temp_list.append(row1)
print(temp_list)
name = []
radius = []
distance = []
mass = []
for i in range(1,len(temp_list)):
    name.append(temp_list[i][0])
    radius.append(temp_list[i][8])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
new_csv = pd.DataFrame(list(zip(name,radius,distance,mass)),columns=['star_name','radius','distance','mass'])
new_csv.to_csv('star_data.csv')

