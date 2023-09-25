""" #특정 시간대의 현재 시간 출력
from datetime import datetime as dt
print(dt.now())

#문자열을 날짜로 변환
date_string='2021-07-08'
date_object=dt.strptime(date_string,'%Y-%m-%d')
print(date_object)

#날짜를 문자열로 변환
date_object=dt.now()
date_string=date_object.strftime('%y-%m-%d')
print(date_string) """
""" 
import mod.utills as mu
dtnow=mu.get_now()
print(dtnow)

ret=mu.cvt_time2str("2023-09-25")
print(ret)

res=mu.cvt_str2time()
print(res)

 """
"""  #os 모듈 확인
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
 """
""" import mod.utills as mu
import os
print(mu.get_curdir())

pname="python"
mu.os_mkdir(pname)
print(os.listdir())
os.rmdir(pname)
print(os.listdir())

import sys
print(sys.version)
print(sys.argv) """\

#파이썬으로 스택 구성하기
list=[]
#스택에 값 쌓기
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

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