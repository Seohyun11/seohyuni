""" from bs4 import BeautifulSoup as bs
import requests as rq
url="https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt=res.text
res_html=bs(hmltxt,'html.parser') """


""" from bs4 import BeautifulSoup as bs
import requests as rq
import os
from urllib.request import urlretrive as rl
url="https://news.daum.net/"
res=rq.get(url)

hmltxt=res.text
res_html=bs(hmltxt,'html.parser')

imgs=res_html.select("img")
print(imgs)
print("\n''''''''''''''''''''''''''''''''''\n")
linkimgs=[]
for i in imgs:
    irs=i.attrs["src"]
    print(irs+"\n")
    linkimgs.append(irs)
    
folder="imgs/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
i=0
for ln in linkimgs:
    if str(ln).find("//t")==False:
        print(ln)
        continue
    else:
        pass
    i+=1
    rl(ln,folder+f"{i}.jpg")
    
     """
     
     
""" from pandas import Series as sr
data=[10,20,30,40]
sdata=sr(data)

print(sdata) """

""" from pandas import Series as sr
data=[10,20,30,40]
sdata=sr(data)

print(sdata.index)
print(sdata.index.to_list())

from pandas import Series as sr
data=[10,20,30,40]
sdata=sr(data)
print(sdata)
print("\n--------------------\n")
sdata.index=['a','b','c','d']
print(sdata) """

""" from pandas import Series as sr
dt=[10,20,30,40]
idx=['a','b','c','d']
sdata=sr(data=idx,index=dt)
print(sdata) """

""" from pandas import Series as sr
dt=[10,20,30,40]
idx=['a','b','c','d']
sdata=sr(data=dt,index=idx)

sd=sdata.reindex(['a','j','c'])

print(sdata['a'])
print(sdata.iloc[0])
print(sdata.loc['a'])
 """
 
""" from pandas import Series as sr
data=[10,20,30,40]
sdata=sr(data)
print(sdata)
 """
 
""" from pandas import Series as sr
dt=['alpha','beta','charlie','delta']
idx=['ab','bc','cd','de']
sdata=sr(data=dt,index=idx)
print(sdata.iloc[1:2])
print("\n---------------------\n")
print(sdata.iloc[2:])
print("\n---------------------\n")
print(sdata.iloc[:2])
print("\n---------------------\n")

from pandas import Series as sr
dt=['alpha','beta','charlie','delta']
idx=['ab','bc','cd','de']
sdata=sr(data=dt,index=idx)
sdata.loc['cd']='echo'
print(sdata) """

""" from pandas import Series as sr
s1=sr([100,200,300],index=['a','b','c'])
s2=sr([100,200,300],index=['b','c','a'])

sum_res=s1+s2
print(sum_res)
print(sum_res.max())
print(sum_res.mean())
print("\n---------------------\n")

sub_res=s1-s2
print(sub_res)
print(sub_res.max())
print(sub_res.mean())
print(sub_res.min())
print("\n---------------------\n")

mul_res=s2*10
print(mul_res)
dv_res=s1/10

from pandas import Series as sr
idx=['a','b','c','d','e']
s1=sr([1100,270,30,450,50],index=idx)
s2=sr([150,740,810,40,25],index=idx)

fil=s1>300
print(fil)

print("\n---------------------\n")
print(s1[fil])
print(s1[fil].index)

print("\n---------------------\n")
fill=s2>s1
print(fill)

print(s2[fill])
print(s2[fill].index)

print("\n---------------------\n")
print(s2[s2>s1].index) """

from pandas import Series as sr
idx=['a','b','c','d','e']
dt=[1100,270,30,450,50]
s1=sr(data=dt,index=idx)

sv=s1.sort_values()
print(sv)

print("\n---------------------\n")
sv1=s1.sort_values(ascending=False)
print(sv1)