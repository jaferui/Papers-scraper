import requests
from bs4 import BeautifulSoup
import time
import pyperclip
import csv

#Definition of the function
def findmails():
    for item in all:
        table=item.find_all('div',{'class':'resultListInner'})
        for item in table: 
            section=item.find_all('div',{'class':'resultList'})
            section2=section[0].find_all('div',{'class':'content-wrapper'})
            section3=section2[0].find_all('div',{'role':'main'})
            section4=section3[0].find_all('ul',{'class':'result-list has-icons'})
            for item in section4:
                general = item.find_all('li',{'class':'result-list-li'})
                for item in general:
                    title = item.find_all('div',{'class':'result-list-record'})
                    authors = item.find_all('div',{'class':'display-info'})
                    #abstract = item.find_all('div',{'class':'gs_rs'})
                    #premail = item.find_all('td')
                    #prename = item.find_all('td')
                    try:
                        tit = title[0].text
                        aut = authors[0].text
                        id = [tit,aut]
                        #if 'Professor' in section[0].text or 'Lecturer' in section[0].text:
                        with open('psycinfoemo.csv', 'a+',newline='\n') as csvfile:
                            writer = csv.writer(csvfile, delimiter=';')
                            writer.writerow(id)
                        print(id)
                        time.sleep(0.5)
                        #else:
                            #pass
                    except:
                        pass


#Selector of main website and main object

r=requests.get('http://web.b.ebscohost.com/ehost/resultsadvanced?vid=27&sid=912a05e5-ec93-4da9-8984-1243eac054c2%40sessionmgr103&bquery=AB+%22peer+assessment%22+AND+AB+emotion&bdata=JkF1dGhUeXBlPWlwLGNvb2tpZSx1cmwsdWlkJmRiPXBzeWgmY2xpMD1QWSZjbHYwPTIwMTQwMS0yMDIwMTImbGFuZz1lcyZ0eXBlPTEmc2VhcmNoTW9kZT1TdGFuZGFyZCZzaXRlPWVob3N0LWxpdmUmc2NvcGU9c2l0ZQ%3d%3d', headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,'html.parser')
all=soup.find_all('div',{'class':'resultListPanel'})
findmails()
