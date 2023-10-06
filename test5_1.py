"""
#특정 시간대의 현재 시간 출력
from datetime import datetime as dt
print(dt.now())

#문자열을 날짜로 변환
date_string='2021-07-08'
date_object=dt.strptime(date_string,'%Y-%m-%d')
print(date_object)

#날짜를 문자열로 변환
date_object=dt.now()
date_string=date_object.strftime('%y-%m-%d')
print(date_string)
 
import mod.utills as mu
dtnow=mu.get_now()
print(dtnow)

ret=mu.cvt_time2str("2023-09-25")
print(ret)

res=mu.cvt_str2time()
print(res)

"""
""""
 #os 모듈 확인
import os

#현재 작업 디렉토리 출력
print(os.getcwd())

#디렉토리 변경r
os.chdir('../')
print(os.getcwd())

#변경된 디렉토리 출력
print(os.getcwd())

#파일 목록 출력
print(os.listdir())

#디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())

#디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir())
 import mod.utills as mu
import os
print(mu.get_curdir())

pname="python"
mu.os_mkdir(pname)
print(os.listdir())
os.rmdir(pname)
print(os.listdir())

import sys
print(sys.version)
print(sys.argv) 

 #파이썬으로 스택 구성하기
list=[]
#스택에 값 쌓기
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
"""
"""
#스택의 상태 확인
print(list)

#스택에서 값 뺴기
top=list.pop()
print(top)
print(list)
print(len(list))

#빈 큐 ㅐㅇ성
queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

#큐의 상태 확인
print(queue)

#큐에서 값 빼기
front=queue.pop(0)
print(front)
print(queue)
print(len(queue))

qlist=[]
def enqueue(qlist,data):
    qlist.append(data)
    
    def dequeue(qlist):
        data=qlist[0]
        return data
    enqueue(qlist,1)
    print(qlist)
    enqueue(qlist,2)
    print(qlist)
    enqueue(qlist,3)
    print(qlist)
    dequeue(qlist)
    print(qlist)
    dequeue(qlist)
    print(qlist)
    
#0(1)
arr=[1.2.3.4.5]
def ret_01(idx):
    return arr[idx]

print(ret_01(2))

#0(1)tlrks
import time
arr=[1.2.3.4.5]
def ret_01(idx):
    return arr[idx]

start=time.time()
print(ret_01(2))
end=time.time()
print(f*{end-start:5f}sec")
      #print("spend time:",f"{end-start}) """
      
"""
import time
arr=[1,2,3,4,5]
def print_eliments(arr):
    for elem in arr:
        print(elem)
start=time.time()
print_elements(arr)
end=time.time() 

 #0  def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(left, right)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

my_list = [1, 2, 3, 4, 5]

result = binary_search(my_list, 4)
if result != -1:
    print(f"요소가 {result}번째 인덱스에 있습니다.")
else:
    print("요소를 찾을 수 없습니다.")
    
     
  #0(n2)
def mul_for():
    for
    
import time
def mul_for():
    for i in range(5):
        for j in range(5):
            print(i,j)
            
start-time.time()
mul_for()
end=time.time()
print(f"{end-start:5f}sec")


#버블정렬
def bubble_sort(arr):
    N=len(arr) #데이터의 갯수:5
    for i in range(N): #0,1,2,3,4
    #print(i,arr)
        for j in range(N-i-1): #4,3,2,1
            if arr[j]>arr[j+1]: #arr[4]
                arr[j], arr[j+1]=arr[j+1],arr[j]
                print(i,j,arr,arr[i],arr[j])
    return arr
    irr=[1,9,2,7,5]
    print(bubble_sort(irr))
    
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot=arr[len(arr)//2] #가운데 값을 피벗으로 선택
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    print("piv",pivot)
    print("left",left)
    print("mid",middle)
    print("rgt",right)
    
    return quick_sort(left)+middle+quick_sort(right)
my_list=[1,9,6,4,5,7,3,2]
print(len(my_list))
sorted_list=quick_sort(my_list)
print(sorted_list) 
"""
""" import requests

res = requests.get('<https://www.google.com>')
print(res.content)
 """

""" import numpy as np

np.array

np.zeros
np.ones

np.array([1, 2, 3])
np.array([4, 5, 6])
f = d + e
g = d - e
h = d * e
i = d / e
"""
""" #pandas
import pandas as pd

# Create a dataframe
data = {'Name': ['John', 'Jane', 'Mike', 'Sarah'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df=pd.DataFrame(data)
df['Age'].describe()

# Sort age

#age 관련 속성
print(df.sort_values{by='Age',ascending=False})
print("============")
print(df.sort_values(by='Age',ascending=True))
print("============")
print(df.sort_values(by='Name'.ascending=True)) """

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

plt.plot(x, y)

plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Example plot')

plt.show()