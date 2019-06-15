#!/usr/bin/python3

import time
import png
from googlesearch import search
import pyqrcode
from pyqrcode import QRCode

web=input("enter the topic u want to search")  # to take input from user

#now time for search
url=[]
for i in search(web,stop=3):
	print(i)               #i will only print url
	time.sleep(1)           #to give time delay of 1 sec
	url.append(i)           #append the url into list

print(url)

#make a qrcode from it

for i,j in zip(url,[1,2,3]):           #for simultaneously running 2 loop
		qcode=pyqrcode.create(i)                    #for creating qrcode
		qcode.png("adhoc%d.png"%j,scale=8)

#create and save the png file naming "adhoc1,2,3.png"
'''
for i in qcode,j in [1,2,3]:
	i.svg("adhoc[j].svg",scale=8)
'''



