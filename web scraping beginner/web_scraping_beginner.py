from urllib import request
import requests
from bs4 import BeautifulSoup

# Making a GET request 
# add user agent if restricted based on respective webs
#r = requests.get('https://vndb.org/v13188',headers={'User-Agent': 'vndb.org 36.94.8.168 python-requests/2.30.0'}) 

#r = requests.get('https://mangagun.net/gunchap-5-shmg-heavenly-sword-of-twin-stars.html',headers={'User-Agent': '*'}) 

def vndb():
    r = requests.get('https://vndb.org/v13188',headers={'User-Agent': '*'}) 
    # check status code for response received 
    # success code - 200 
    print(r)
    print(r.url)
    print(r.headers)
    print(r.reason)
    #print(r)
    print()
    #\n\nvndb.org 36.94.8.168 python-requests/2.30.0\n
    #BS=BeautifulSoup(request.urlopen("https://vndb.org/v13188",headers={'User-Agent': '*'}).read())
    BS=BeautifulSoup(r.content, 'html.parser')
    # print content of request
    #print(BS.prettify())
    res=BS.find_all('tr')
    for x in res:
        for y in x.find_all('td'):
            #print(y.find_all('p').getText())
            for z in y.find_all('p'):
                print(z.getText())
            #print()
            #print('_')
    #print(res)
    print('\n___')
    res=BS.find_all('img')
    links=[]
    for x in res:
        links.append(x['src'])
    print(*links, sep="\n")
def mangagun():
    #must use selenium
    r = requests.get('https://mangagun.net/gunchap-5-shmg-heavenly-sword-of-twin-stars.html',headers={'User-Agent': '*'})
    bs=BeautifulSoup(r.content, 'html.parser')
    #print(bs.prettify())
    for x in bs.find_all('img'):
        if(x['src']):
           print (x['src'])

def mangagunSelenium():
    print()

mangagunSelenium()