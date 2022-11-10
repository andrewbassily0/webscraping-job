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

