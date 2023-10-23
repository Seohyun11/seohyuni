""" import socket
from select import select
import time
Host="127.0.0.1"

#HOST="localhost"
PORT=8080

BUFSIZE=1024
ADDR=(HOST,PORT)

#1 소켓 생성
srvSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2. 주소정보 할당
srvSock.bind(ADDR)
print('bind')

#3.수신 대기 상태
srvSock.listen(100) 
print('listen')

#4.연결수락
cltSocket, addr_info=srvSock.accept() 
print('accept')

time.sleep(10)

#연결 종료
cltSocket.close() 

#소켓 종료
srvSock.close()

print('close')

import time
HOST='127.0.0.1'
PORT=8080

BUFSIZE=1024
ADDR=(HOST,PORT)


#1 서버에 접속하기 위한 소켓을 생성한다.
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. 서버에 접속을 시도한다.
clientSocket.connect(ADDR)
print('connect is success') """

