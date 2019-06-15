#!/usr/bin/python3

import os
import  
'''
string=input("enter a string")
print(string.isalpha())
 '''

useradd=input("selsect Username")
passwd=input("Select Password")
os.system("sudo useradd -m -p "+passwd+" "+useradd)



