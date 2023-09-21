"""
add=lambda a,b,: a+b
print(add(2,3))

def add_numbers(x,y):
    return x+y
#함수 호출
result=add_numbers(4,5)
print(result)

def greet(name):
    print("Hello, " + name + ". How are you?")
greet(seohyun)
    

def add(a, b) : 
	print(a + b)

def sub(a, b) :
	return a - b

def mul() :
	return 2 * 4

def div() :
	print(4 / 2)

add(3, 5)
sub(3, 5)
mul()
div()

#매개변수와 인자1
def function(x):
    if x % 2 == 0:
        print("짝수입니다")
    else:
        print("홀수입니다")
y=input("숫자 입력하기")
function(int(y))


def function(x):
    return x[::-1]

y=input("문자 입력하기:")
function(str(y))
print(function(y))



def add(a,b):
    return int(a)+int(b)
def sub(a,b):
    return int(a)-int(b)
def mul(a,b):
    return int(a)*int(b)
def div(a,b):
    return int(a)/int(b)

a = input("a를 입력해주세요:")
b = input("b를 입력해주세요:")
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))

def prt_func() :
    print("hello")

def callfunc(fx) :
		fx()

callfunc(prt_func)

def prt_func() :
    for n in range(5):
        print("hello",+n)
        n+=1
        
        

def callfunc(fx) :
		fx()

callfunc(prt_func)


def add(a, b) :
	return a + b


def add(a : int, b : int) -> int :
	return a + b
"""