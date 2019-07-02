#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import re
import sys
import pickle
from decimal import *

dic={}
cost=0
base="Content-type: text/html; charset=UTF-8\r\n"
output_error="ERROR\n"

print ('Content-type: text/html; charset=UTF-8')
print("\r")

re_int = re.compile(r'\d+$')
re_deci = re.compile(r'\d+\.\d+$')
re_just = re.compile(r'\d+\.0+$')

def check_pat(pat,num):
    if(not pat.match(str(num))):
        print("ERROR")
        sys.exit()
    return


def check_key(dict,s):
    if s not in dict:
        dict[s]=0
    return
def add(dict,name,value):
    check_pat(re_int,value)
    check_key(dict,name)
    dict[name]+=int(value)
    return

def deleteall(dict):
    dic.clear()
    global cost
    cost=0
    return
def show_list(dict,s):
    print(str(s)+": "+str(dict[s]))
    return

def show_list_all(dict):
    for i in sorted(dict, key=lambda i:i[0]):
        if(int(dict[i]) > 0):
            print(str(i)+": "+str(dict[i]))
    return

def buy(dict,name,amount):
    check_pat(re_int,amount)
    if(int(dict[name])<int(amount)):
        print("ERROR")
        sys.exit()
    dict[name]-=int(amount)
    return
def buy_cost(dict,name,amount,price):
    global cost
    if(float(price) <= 0):
        print("ERROR")
        sys.exit()
    buy(dict,name,amount)
    cost+=float(price)*float(amount)
    return

def save(filename,dest):
    f=open(filename,"wb")
    pickle.dump(dest,f)
    f.close
    return
def load(filename):
    f=open(filename,"rb")
    return pickle.load(f)

seiki = re.compile(r'[\d\+\-\*\/() ]+$')
def check(s):
    return seiki.match(s) is not None

form = cgi.FieldStorage()
if ( form.has_key("function") ):
    func = form["function"].value
else:
    sys.exit()

dic=load("list.txt")
cost=load("cost.txt")
if(func=="add"):
    if(form.has_key("name")):
        if(form.has_key("amount")):
            amount = form["amount"].value
        else:
            amount=1
        add(dic,form["name"].value,amount)
    else:
        print(output_error)
        sys.exit()
elif(func=="show_list"):
    if(form.has_key("name")):
        show_list(dic,form["name"].value)
    else:
        show_list_all(dic)
elif(func=="buy"):
    if(form.has_key("name")):
        if(form.has_key("amount")):
            amount=form["amount"].value
        else:
            amount=1
        if(form.has_key("price")):
            buy_cost(dic,form["name"].value,amount,form["price"].value)
        else:
            buy(dic,form["name"].value,amount)
elif(func=="checkcost"):
    sale=Decimal(str(cost)).quantize(Decimal(".01"), rounding=ROUND_UP)
    if(re_just.match(str(sale))):
        sale=int(sale)
    print("cost: "+str(sale))
elif(func=="deleteall"):
    deleteall(dic)
else:
    print(output_error)
    sys.exit()


save("list.txt",dic)
save("cost.txt",cost)

