import requests
import webbrowser
import bs4


print("Press 1 if you want to generate link for movies,2 for TV series, 3 for games, 4 for softwares:")
num=int(input())
print("Enter name of the file you wanna get link of:")
bingsearch=input()

query = bingsearch.replace(' ', '+')

if(num==1):
    link='https://www.bing.com/search?q='+query+'+movie+torrent'
if(num==2):
    link='https://www.bing.com/search?q='+query+'+tv+series+torrent'
if(num==3):
    link='https://www.bing.com/search?q='+query+'+game+torrent'
if(num==4):
    link='https://www.bing.com/search?q='+query+'+software+torrent'
    
res=requests.get(link)

soup=bs4.BeautifulSoup(res.text, 'lxml')

for link in soup.find_all('a', href=True):
     if(link['href'][0]=='h') and (link['href'][12:16]!='bing') and (link['href'][7:0]!='go'):
        webbrowser.open(link['href'])
        print("Your torrent link is:", link['href'])
        break
        
