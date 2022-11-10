import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title= []
company_names=[]
descriptions=[]
locations=[]


result = requests.get("https://wuzzuf.net/search/jobs/?q=python+developer&a=hpb")

src = result.content
soup = BeautifulSoup( src, "lxml")

job_title = soup.find_all("h2",{"class":"css-m604qf"})
company_names = soup.find_all("a",{"class":"css-17s97q8"})
descriptions = soup.find_all("div",{"class":"css-y4udm8"})
locations = soup.find_all("span",{"class":"css-5wys0k"})
