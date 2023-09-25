import math
import random as rd
from datetime import datetime as dt
import os

def st_sqrt(n):
    return math.sqrt(n)

def st_sinpi():
    return math.sinpi(math.pi/2)
    
def st_elog():
    return math.elog(math.e)

def st_ep(n):
    return math.exp(n)

def st_pi():
    return math.pi


def res():
    return rd.randint(1,100)

def lres():
    my_list=["apple","banana","cherries"]
    return rd.choice(my_list)
def fres():
    return rd.random()

def nvres():
    return rd.normalvariate()

#특정 시간대의 현재 시간 출력
def get_now():
    return dt.now()
def cvt_time2str(objtime):
    return dt.strptime(objtime,'%Y-%m-%d')
def cvt_str2time(strtime):
    obj=dt.now()
    return dt.strftime("%Y-%m-%d")

def get_curdir():
    return os.getcwd()

def os_mkdir(pname):
    return os.mkdir('pname')

def os_rmdir(pname):
    return os.rmdir('pname')