#pip install lxml              Successfully installed lxml-4.9.2
#pip install requests          Successfully installed certifi-2022.12.7 charset-normalizer-3.0.1 idna-3.4 requests-2.28.2 urllib3-1.26.14
#pip install beautifulsoup4    Successfully installed beautifulsoup4-4.11.2 soupsieve-2.4

import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest

title = []
company = []
location = []

# get the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# get the content of the url
scr = result.content

soup = BeautifulSoup(scr, 'lxml')

job_titles = soup.find_all('h2', {'class': 'css-m604qf'})
companies = soup.find_all('a', {'class': 'css-17s97q8'})
locations = soup.find_all('span', {'class':'css-5wys0k'})

for i in range(len(job_titles)):
    title.append(job_titles[i].text)
    company.append(companies[i].text)
    location.append(locations[i].text)

list = [title, company, location]
export = zip_longest(*list)
with open('wuzzuf.csv', 'w', newline='') as wf:
    wr = csv.writer(wf)
    wr.writerow(['Job Title', 'Company Name', 'Location'])
    wr.writerows(export)