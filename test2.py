"""
my_list=[9,4,3,7,8,'hi']
print(4 in my_list)
print(2 in my_list)
print(2 not in my_list)

my_dic={"key1":"v1","k2":"v2"}
print("k2" in my_dic)
x=[1,2,3]
y=[1,2,3]
z=x
print(x is y)
print(x is z)
print(x is not y)

a=5
b=5
print(a is b)
print(a is not b)

print(3==3.0)
print(3 is 3.0)

a=[3,5,1]
b=a
a[0]=2
print(a,b)
print(a is b)

print(2+3*4)
print(10/5/2)
print(2**3**2)
print(10%3%2)
print(1+2>3 and 4-1<2)
print(not False and True)
print(not True or False and True)

#조건문
x=10
if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x is zero")  
    
x=0
if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x is zero")  

x=-5
if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x is zero")  

x=2
if x%2==0:
    print("x is 짝수")
else:
    print("x is 홀수")  

x=1
if x%2==0:
    print("x is 짝수")
else:
    print("x is 홀수")  



a=10
b=10
if a==b:
    print("a=b")
elif a<b:
    print("a<b")
else:
    print("a>b")
    
char = a
if char==a:
    print("문자는 a입니다.")
else:
    print("문자는 b입니다.")
#for문
fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

#이중for문
my_list=[[1,2,3],[4,5,6],[7,8,9]]
for row in my_list:
    for num in row:
        print(num)

voca=str("lostark")
n=0
for x in voca:
    print(voca[n])
    n=n+1

my_list=[1,2,3,4,5,6,7,8,9]
my_list.reverse()
for num in my_list:
    print(num)
    
my_list=[1,2,3,4,5,6,7,8,9]
for num1 in my_list:
    for num2 in my_list:
        print(num1,"times",num2,"=",num1*num2)


#for else문
rang=[5,8,3,1,6]
for i in rang:
    print("element:",1)
    
else:
    print("end process")

for i in range(10):
    if i==7:
        break
    elif i==1:
        continue
    else:
        pass
    print (i)
    
i=1
while i<=5
    print(i)
    i+=1

i=0
while i<=9:
    print(i)
    i+=1
    
voca=str("lostark")
lenth=len(voca)
n=0
while n<=lenth-1:
    print(voca[n])
    n=n+1


i=0
a=0
while i<=9:
    a=a+i+1
    i+=1
    
print(a)

print("짝수 출력")
a=1
while a<=100:
    if a%2==0:
        print(a)
        a+=1
    else:
        pass
        a+=1
        
print("홀수 출력")
a=1
while a<=100:
    if a%2==1:
        print(a)
        a+=1
    else:
        pass
        a+=1
"""
a=1
while a<=100:
    if a%7==0:
        print(a)
        a+=1
    else:
        pass
        a+=1