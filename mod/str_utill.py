def cutword(st,wd,idx):
    tmp=st.split(wd)
    res=tmp[idx]
    return res



import random as rd
res=rd.randint(1,100)
print(res)
my_list=["apple","banana","cherries"]
lres=rd.choice(my_list)
print(lres)

fres=rd.random()
print(fres)

nves=rd.normalvariate()
print(nves)
