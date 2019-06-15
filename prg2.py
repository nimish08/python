#!/usr/bin/python3
from googlesearch import search
import time
w=input("enter the name you want to search")
url=[]

for i in search(w,stop=10):
	print(i)
	time.sleep(1)
	url.append(i)
	f=open("url.txt","a+")
	f.write("\n")
	f.write(i)
f.close()
print(i)
