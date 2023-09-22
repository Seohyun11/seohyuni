"""
def prt_func():
    print("hello")
def callfunc(fx):
    fx()
callfunc(prt_func)

def prt_func(n):
    print("hello",n)


def callfunc(fx):
    for i in range(1,6):
        fx(i)
callfunc(prt_func)



def update_msg(name:str)->list:
    msg=[]
    msg.append("hello"+name)


def greeting(in_name):
    gt_msg=None
    gt_msg=update_msg(in_name)
    return gt_msg


def fun(n):
    if n==5:
        return
    print(1,n)
    fun(n+1)
    
fun(1)


def ploop(n):
    if n==0:
        print("end")
        return 1
    else:
        print(n,n-1,"=",n+n-1)
        return n*ploop(n-1)
print(ploop(5))


import mod.calc.py

print(calc.add(8,4))
print(calc.sub(8,4))
print(calc.mul(8,4))
print(calc.div(8,4))


import mod.circle_mod as cm
print(cm.pi)
print(cm.cc_area(5))
print(cm.cc_len(5))

import mod.str_utill as smod
url="https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res=smod.cutword(url,"/",3)
print(res)

import math
sq_res=math.sqrt(6)
print(sq_res)
sp_res=math.sin(math.pi/2)
print(sp_res)
math.log
e_res=math.log(math.e)
print(e_res)

exp_res= math.exp(3)
print(exp_res)
pi_res=math.pi
print(pi_res)
print(pi)


import mod.utills as mu
res=mu.st_sqrt(7)
print(res)

sin=mu.st_sinpi()
print(sin)

el=mu.st_elog()
print(el)

ep=mu.st_exp(3)
print(ep)

pi=mu.st_pi()

import random as rd
res=rd.randint(1,100)
print(res)
my_list=["apple","banana","cherries"]
lres=rd.choice(my_list)
print(lres)

fres=rd.random()
print(fres)

nvres=rd.normalvariate()
print(nvres)
"""

import mod.utills as mu
res=mu.res()
print(res)

lres=mu.lres()
print(lres)

fres=mu.fres()
print(fres)

nvres=mu.mvres()
print(mvres)