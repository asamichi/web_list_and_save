#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import re
import sys
import pickle


def save(filename,dest):
    f=open(filename,"wb")
    pickle.dump(dest,f)
    f.close
    return
def load(filename):
    f=open(filename,"rb")
    return pickle.load(f)
data={}
num=0.0

save("list.txt",data)
save("cost.txt",num)
