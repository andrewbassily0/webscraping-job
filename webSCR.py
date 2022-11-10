import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title= []
company_names=[]
descriptions=[]
locations=[]
links=[]
salaries =[]


result = requests.get("https://wuzzuf.net/search/jobs/?q=python+developer&a=hpb")

src = result.content
soup = BeautifulSoup( src, "lxml")

job_title = soup.find_all("h2",{"class":"css-m604qf"})
company_names = soup.find_all("a",{"class":"css-17s97q8"})
descriptions = soup.find_all("div",{"class":"css-y4udm8"})
locations = soup.find_all("span",{"class":"css-5wys0k"})

for i in range(len(job_title)):
   job_title.append(job_title[i].text)
   links.append(links[i].find("a").attrs["href"])
   company_names.append(company_names[i].text)
   descriptions.append(descriptions[i].text)
   locations.append(locations[i].text)
   salaries.append(salaries.text)

for links in links:
    result = requests.get(links)
    src= result.content
    soup = BeautifulSoup(src, "lmxl")
    salaries = soup.find_all("div",{"class":"matching-requirment-icon-container"})

list =[job_title,company_names,descriptions,locations,links]
ex =zip_longest(*list)

with open("E:\Projects\project\web scrapping\ file.csv", "w") as webscrapingfile:
    wr = csv.writer(webscrapingfile)
    wr.writerow(["job_title","company_names","descriptions","locations","links"])
    wr.writerows(ex)