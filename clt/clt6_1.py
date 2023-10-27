""" import time

HOST = '127.0.0.1'
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)


#1 서버에 접속하기 위한 소켓을 생성한다.
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. 서버에 접속을 시도한다.
clientSocket.connect(ADDR)
print('connect is success')
 """
""" 
import socket
import sys

import time

HOST = '127.0.0.1'
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDR)

while True:
    message = input('client : ')
    clientSocket.send(message.encode('utf-8'))
    response = clientSocket.recv(1024)
    print ('server : ', response.decode('utf-8'))

clientSocket.close()
"""
""" import socket

HOST = "127.0.0.1"
PORT = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("msg: ", data)

    rsp = data.decode("utf-8").upper()
    sock.sendto(rsp.encode("utf-8"), addr)

sock.close() """







""" #객체지향프로그래밍
class Person :
	name = "python"
	age = 23
	number = "01012345678"
p=Person()
print(p.name)
print(p.age)
print(p.number)

p1=Person()
print(p.name)
print(p1.age)
print(p1.number) """

""" class Person :
	name = "python"
	age = 23
	number = "01012345678"

	def getIntroduce(self):
		return f"My name is {self.name}"
p=Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce()) """

class Person :
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number

#클래스초기화
class Person:
    def __int__ (self,name,age,number):
        self.name=name
        self.age=age
        self.number=number
p=Person("hello",24,"0107654321")
p1=Person("he",21,"0108")
p2=Person("hee",24,"928764321")

print(p.name)
print(p1.name)
print(p2.name)
