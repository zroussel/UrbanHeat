# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:25:26 2020

@author: rouss
"""


import time

T=time.localtime()
A = T.tm_year
B = T.tm_mon
C = T.tm_mday
D = T.tm_hour
E = T.tm_min

f = open("nametest{}-{}-{}-test-{}_{}".format(B,C,A,D,E),"w")
