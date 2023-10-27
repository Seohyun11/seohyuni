""" import socket
from select import select
import time

HOST = "127.0.0.1"  #정해져있는IP번호-> 로컬ip
#HOST = "localhost" #127.0.0.1과 localhost는 동일함.
PORT = 8080 #시스템포트를 넣으면 안됨. 0~1024 보통 8080을 많이 씀

BUFSIZE = 1024
ADDR = (HOST,PORT)

#1.소켓 생성.
srvSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2.주소 정보 할당
srvSock.bind(ADDR) 
print('bind')

#3.수신 대기 상태
srvSock.listen(100) 
print('listen')

#4.연결수락
cltSocket, addr_info = srvSock.accept() 
print('accept')

time.sleep(10)

#연결 종료
cltSocket.close() 

#소켓 종료
srvSock.close()

print('close')

#기본적인 서버와 크라이언트는 이렇게 돌아감 """
""" 
import socket
from select import select
import time

HOST = "127.0.0.1"
#HOST = "localhost"
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)

srvSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvSock.bind(('', PORT))
srvSock.listen()

cltSocket, addr = srvSock.accept()

while True:
    response = cltSocket.recv(1024)
    print ('client : ', response.decode('utf-8'))

    message = input('server : ')
    cltSocket.send(message.encode('utf-8'))

cltSocket.close()
 """
import socket

HOST = "127.0.0.1"
PORT = 1234

ADDR = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("msg : ")

    sock.sendto(msg.encode('utf-8'), ADDR)
    rsp, srv = sock.recvfrom(1024)
    print("msg : ", rsp)

sock.close()