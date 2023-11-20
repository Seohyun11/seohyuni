""" import pandas as pd
folder="data/"
target=folder+ "fktemp.csv"
df=pd.read_csv(target) """

from faker import Faker as fk
import os
#temp=fk()
temp=fk("ko-KR")
print(temp.name())

folder="data/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    with open(folder+"fktemp.csv"):

with open(folder+"fktemp.csv","w",encoding='utf8') as f:
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,")
with open(folder+"fktemp.csv","a",encoding='utf8') as f:
    for i in range(30):
        f.write(temp.name()+","+
                temp.address()+","+)
        
import pandas as pd
folder="data/"
target=folder+"fktemp,csv"
print(df.name=="김영수")
      
#print(df.name=="김영수")
#print(df.company=="박박정")
temp=df[df.postcode>70000]
print(temp)