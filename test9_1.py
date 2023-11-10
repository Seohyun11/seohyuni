""" import multiprocessing as mp
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name: {str_name}|n")
        
if __name__=="__main__":
    process1=mp.Process(target=counter, args("1num",))
    process2=mp.Process(target=counter, args("2num",))
    process3=mp.Process(target=counter, args("3num",))

    start=time.time()
    process1.start()
    process2.start()
    process3.start() """
"""     
import random as rd

async def tester(name):
    snum=rd.randint(10,20)
    print(f"{name}-{snum}")
    for i in range(snum):
        await asyncio.sleep(1)
        print(f"{name}-{snum}-{i}")
    print(f"end of {name})")

async def main():
    task1=asyncio.create_task(tester("1test"))
    task2=asyncio.create_task(tester("2test"))
    task3=asyncio.create_task(tester("3test"))
    
    print("start")
    await task1
    await task2
    await task3
    
    print("end")
if __name__=='__name__':
    asycio.run(main()) """
    
""" def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name:{str_ame}\n")
        
async def main():
    task1=asyncio.create_task(worker1())
    task2=asyncio.create_task(worker2())
    
    print("start")
    await task1
    await task2"""
    
""" async def worker2():
    for i in range(1,4):
        print(f"Task 2: Step {i}")
        await asyncio.sleep(2)
        
    async def main():
        process1=mp.Process(target=counter,args("1num",))
        process2=mp.Process(target=counter,args("2num",))
        process3=mp.Process(target=counter,args("3num",))
        
        start=time.time()
        
        process1.start()
        process2.start()
        process3.start() """
        
""" #스케쥴처리
import time
import sched
start =time.time()

def tester(name):
    print(f"start-time {time.time()-start}")
    for i in range(3):
        print(f"{name}-{i}")
    print(f"end of {name}")
          
s=sched.scheduler()
s.enter(5,1,tester,('1num',))
s.enter(3,1,tester,('2num',))
s.enter(7,1,tester,('3num',))
s.run() """

""" import time
import sched
start=time.time()
def tester(name):
    print(f"start-time {time.time()-start}")
    for i in range(3):
        print(f"{name}-{i}")
    def run():
        s=sched.scheduler()
        s.enter(5,1,tester,('1num',))
        s.enter(3,1,tester,('2num',))
        s.enter(7,1,tester,('3num',))
        s.run()
    if __name__=="__main__":
        run()
        #main()
        print("end") """
        
""" origin="To be or not to be, That is a question!"

dmp=dm()
diff=dmp.diff_main(origin.copyed)
dmp diff_cleanuoSemantic(diff)
for d in diff:
    print(d)
    
 """
""" temp=Faker()
temp.name
temp=Faker("ko.KR")
"""  """
from faker import Faker as fk
#temp=fk()
temp=fk("ko-RK")
print(temp.name())

with open("fktemp.csv","w",newline=' ') as f:
    for i in range(30):
        f.write(temp.name()+","+
                temp.address()+","+
                temp.postcode()+","+
                temp.company()+","+
                temp.job()+","+
                temp.phone_number()+","+
                temp.email()+","+
                temp.user_name()+","+
                temp.ipv4_private()+","+
                temp.ipv4_public()+","+
                temp.catch_phrase()+","+
                temp.name()+","+"\n") """

""" import subprocess as sp
import pprint
import sp.run(["cmd","/c"dir"],capture_output=True)
    print(res) """
    
    
""" import traceback as tb
def tester():
    return 1/0
def caller():
    tester()
def main():
    try:
        caller()
    except ZeroDivisionError:
        print("zde error")
    except ValueError:
        print("ve error")
    except Exception as ex:
        print("ex error",ex)
    else:
        print("ok")
    finally:
        print("end") """
        
""" <!DOCTYPE html>
<html>
<title>Online HTML Editor</title>

<head>
</head>

<body>
    <h1>Online HTML Editor</h1>
    <h1>1단계</h1>
    <h2>2단계</h2>
    <h3>3단계</h3>
    <h4>4단계</h4>
    <h5>5단계</h5>
    <h6>6단계</h6>

    <p></p>
    <b>굵게 표시됩니다.</b>
    <p></p>
    <i>기울임꼴로 표시됩니다.</i>
    <p></p>
    <strong>강하게 강조합니다.</strong>
    <p></p>
    <em>약하게 강조합니다.</em>
    <p></p>
    <ins>밑줄이 표시됩니다.</ins>
    <p></p>
    <del>취소선이 표시됩니다.</del>
    <p></p>
    <s>나도 취소선</s>
    <p></p>
    밑줄이 <u>표시</u>됐습니다.
    <p></p>
    <small>그렇군요.</small>
    <ul>
    
        <li>순서가 없는 첫번째 항목입니다.</li>
    
        <li>순서가 없는 두번째 항목입니다.</li>
    </ul>
    <ol>
    
        <li>순서가 있는 첫번째 항목입니다.</li>
    
        <li>순서가 있는 두번째 항목입니다.</li>
    </ol>
    <ul>
    
        <li>첫 번째</li>
    
        <li>두 번째
            <ul>
            
                <li>두 번째 속 첫 번째</li>
            
                <li>두 번째 속 두 번째</li>
                </ul>
            </li>
    </ul>

    <ul>
    
        <li>가나다</li>
    
        <li>라마바
            <ol>
            
                <li>사아자</li>
            
                <li>차카타</li>
                </ol>
            </li>
    
        <li>파하</li>
    </ul>
    <table>
    
        <tr>
        
            <th>A</th>
        
            <th>B</th>
        
            <th>C</th>
            </tr>
    
        <tr>
        
            <td>A1</td>
        
            <td>B1</td>
        
            <td>C1</td>
            </tr>
    </table>
    <div>This is real time online HTML Editor</div>
</body>

</html> """

#태그 찾기
from bs4 import Beautifulsoup as bs
import requests as rq

url = "http://xkcd.com/2852/"
res=rq.get(url)

hmltxt=res.txt,'html.parser'
pres=res_html.find("hi")
pprint(pres)
print("\n1____________________________\n")
print(pres.get_text().strip())
print("\n2____________________________\n")
print(pres.next_element.get_text().strip())