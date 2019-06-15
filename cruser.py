#!/usr/bin/python3
import os

uname=input("enter input from user")
a=uname.isalpha()

if a ==True:
        passwd="hello"+uname
        os.system("sudo useradd -m -p "+passwd+" "+uname)
        print("user created!")
else:
        print("all charcter are not in string!")



