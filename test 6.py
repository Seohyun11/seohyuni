""" star="*"
for A in range(1,6):
    print(star*(6-A)) """

""" star="*"
for A in range(1,6):
    print(star*A)
 """

""" star="*"
blank=" "
for A in range(1,6):
    print((blank*(5-A))+(star)+(star)*((A-1)*2)) """

""" star="*"
blank=" "
for A in range(1,6):
    print((blank*(6-A))+(star)+(star)*((A-1)*2))
print(star*11)
for A in range(1,6):
    print((blank*A)+(star)+(star)*((5-A)*2)) """
    
""" 
#직각삼각형
for i in range(1,6):
    print("*"*i)

 """
"""  #역직각삼각형
for i in range(5,0,-1):
    print("*"*i) """

""" #이등변삼각형
for i in range(1,6):
    spaces=" "*(6-i)
    stars="*"*(2*i-1)
    print(spaces+stars)
 """
""" #n=5 #삼각형의 높이를 설정
for i in range(1,6):
    spaces=" "*(6-i)
    stars="*"*(2*i-1)
    print(spaces+stars)
for i in range(6,0,-1):
    spaces=" "*(6-i)
    stars="*"*(2*i-1)
    print(spaces+stars)
     """
""" 
line=[]
num=0
for i in range(5):
    for j in range(5):
        num+=1
        line.append(num)
    print(line)
    line=[]
     """
""" line=[]
num=1
num2=num
line.append(num)
for i in range(5):
    for j in range(5):
        num2+=5
        line.append(num2)
    print(line)
    line=[]
    num+=1
    num2=num
    line.append(num) """
    
""" line=[]
num=0
for i in range(5):
    for j in range(5):
        num+=1
        line.append(26-num)
    print(line)
    line=[] """


""" #세로로출력
line=[]
for i in range(1,6):
    for j in range(1,6):
        num=((j-1)*5)+i
        line.append(num)
    print(line)
    line=[] """

""" A=input()
import random  
def get_computer_choice():
    choices=['1','2','3']
    return random.choice(choices)
def determine_winner(user_choice):
    pcnum=get_computer_choice()
    print(user_choice,pcnum)
    if user_choice==pcnum:
        print("무승부")
        return
    elif(
        (user_choice=='1' and pcnum=='3')or
        (user_choice=='2' and pcnum=='1') or
        (user_choice=='3' and pcnum=='2')
    ):
        print('승')
        return
    else:
        print("패")
        return
print("1:가위")
print("2:바위")
print("3:보")
print("1~3 숫자를 입력하세요!")
chnum=input()
pcnum=get_computer_choice()
"""

""" file = open("C:\\Users\\Catholic\\temp.txt", "w")
file.close()
 """
""" file = open("temp.txt","w")

for i in range(100):
    file.write("{i}\n")

file.close()  """

""" file = open("C:\\Users\\Catholic\\temp.txt", "w")
for i in range(100):
    file.write("({i}\n")
    
file.close() """

""" file=open("temp.txt","a")

file.write("hello\n")
file.write("world")

file.close
 """
 
""" file=open("temp.txt",'r')
res=file.read()
print(res)
file.close """
""" 
file=open("temp.txt",'r')
for i in range(110):
    res=file.readline()
    print(res)
file.close
 """
 
""" f=open("temp.txt","r")
line=f.readlines()
for l in line:
    print(l)
f.close()

 """
 
f=open("temp.txt","r")
for line in f:
    print(line)
f.close()
