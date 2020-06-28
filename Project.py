# 
#importing library
from bs4 import BeautifulSoup as bs 
import urllib.request
import json
#reading the html code file
with open('New Lead.html') as html_file:
    soup=bs(html_file,'html.parser')
#scraping the Name
d=soup.find('font',{'style':'font-family: Arial, sans-serif; font-size: 14px; color: #333333;'})
name=d.strong.text

# #scraping the Email
ab=soup.find('a',{'style':'color: #d92228; text-decoration:none;'})
email=ab.text

# scraping the Number
bc=soup.find('a',{'style':'text-decoration:none;border:none;color:#fff;'})
num=bc.text

#Scraping the value of Bed and Bath
cd=soup.findAll('font',{'style':'font-family: Arial, sans-serif; font-size: 14px; color: #333333;line-height: 1.4;'})
m=[]
for i in cd:
    m.append(i.text)
bb=m[2]         #Strong value of Bed and Bath in list
bb=bb.split(" ")
bed=bb[1]       #Slicing list for a seprate value of Bed
bath=bb[3]      #Slicing list for a seprate value of Bath

#Scraping value of Address
ba=soup.findAll('a',{'style':'color: #d92228; text-decoration:none;'})
l=[]
for i in ba:
    l.append(i.text)
address=l[2]
# Creating a dictionary to store all the values
dic={'Name':name,'Email':email,'Number':num,'Bed':bed,'Bath':bath,'Address':address}
print(dic)
#Saving the dictionary in json file
js=json.dumps(dic)
fp = open('output.json','w')
fp.write(js)
fp.close()
