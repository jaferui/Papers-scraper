import requests
from bs4 import BeautifulSoup
import time
import pyperclip
import csv

#Definition of the function
def findmails():
    for item in all:
        table=item.find_all('div',{'id':'r'})
        for item in table: 
            section=item.find_all('div',{'id':'rr'})
            section2=section[0].find_all('div',{'id':'rrw'})
            for item in section2:
                general = item.find_all('div',{'class':'r_i'})
                for item in general:
                    title = item.find_all('div',{'class':'r_t'})
                    authors = item.find_all('div',{'class':'r_a'})
                    abstract = item.find_all('div',{'class':'r_d'})
                    #premail = item.find_all('td')
                    #prename = item.find_all('td')
                    try:
                        tit = title[0].text
                        aut = authors[0].text
                        abst = abstract[0].text
                        id = [tit,aut,abst]
                        #if 'Professor' in section[0].text or 'Lecturer' in section[0].text:
                        with open('ERIC1.csv', 'a+',newline='\n') as csvfile:
                            writer = csv.writer(csvfile, delimiter=';')
                            writer.writerow(id)
                        print(id)
                        time.sleep(0.5)
                        #else:
                            #pass
                    except:
                        pass


#Selector of main website and main object

r=requests.get('https://eric.ed.gov/?q=abstract%3a%22PA%22+AND+abstract%3a%22motivation%22&ff1=dtySince_2011&pg=5', headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,'html.parser')
all=soup.find_all('div',{'id':'main'})
findmails()
