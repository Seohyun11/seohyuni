""" class MyClass:
    count = 0

    def __init__(self, num):
        self.count = num

    @classmethod
    def clsMethod(cls):
        cls.count += 1 
        print(f"cls count = {cls.count}")

    def instMethod(self):
        self.count += 1 
        print(f"instance = {self.count}")

MyClass.clsMethod()

obj = MyClass(10)

obj.instMethod()
print(obj.count)

print(MyClass.count)
print(MyClass.count) """

""" class Champion:
    lv=1
    movSpd=0
    basicMovSpd=325
    atkSpd=0.658

    def __init__(self, champNam, speed):
        self.hp=100
        self.champNam=champNam
        self.level=1
        self.setSpeed(speed)
        self.setAtkSpd()
        slef.setMovSpd()

    def setAtkSpd(self)
        self.atkSpd=0.658*((1.0334)**(Champion.lv-1))

    def beAtk(self, dem):
        print("be attack",dem,1-100.0/(100.0+100))
        print(self.dem)
        self.hp=self.hp-self.dem

    def setSpeed(self,sp):
        if (sp==1):
            self.speed=50
        else:
            self.speed=0

    def setMovSpd(self):
        print("set Mov Spd")
        self.movSpd=(20+self.speed)*(1.00*(100))
    
    def printStatus(self):
        print("champNam:%s, hp:5f, lv:%d, mvSpd:%f, atkSpd:%f" %(self.champNam, self.hp, self.mvSpd, self.atkSpd)")
 """
""" 
class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1

class Yasuo(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level) """

""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1
    
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)


class Yasuo(Champion) :
    def attck(self, key):
        print(f"attack - {key} steel tempest")
        return


class Garen(Champion) :
    def attck(self, key):
        print(f"attack - {key} demacian justice")
        return """

""" class champion:
    def __init__(self,name):
        self.name=name
        self.level=1

    def attack(self,key):
        print(f"attack={key}")

    def levelup(self):
        self.level+=1
    
    def getLevel(self):
        print(self.level)
    
    class Yasuo(Champion):
        def attack(self,key):
            print(f"attack-{key} steel tempest")
            return
    class Garen(Champion):
        def attack(self,key):
            print(f"attack-{key} demacian justice")
            return """

""" circ = Circle(5)
rect=Rectangle(4,6)
print(circ.area())
print(rect.area())

sett=[circ, rect]
for st in sett:
    print(st.area()) """


""" from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circ = Circle(5)
rect = Rectangle(4, 6) """

""" #정보은닉
from enum import NAMED_FLAGS


class Person:
    def __init__ (self, name, age, num)
        self._name=name
        self.age=age
        self._number=num
        
@property
def name(self):
    return self._name

@property
def age(self):
    return self._age

def number(self):
    return self._number

@name.setter
def name(self, new):


@age.setter
def age(self,nAge):

user1= Person("Alice",30, "01011112222")
print(user1.age)
print(user1._age)
print(user1.name)
print(user1._name)
print(user1.number)
print(user1._number) """

""" class Person :
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num
    
    def getName(self) :
        return self.name
    
    def getAge(self) :
        return self.age
    
    def getNumber(self) :
        return self.number

class Student(Person) : ()

class Teacher(Person) : ()

def getPersonName(person) :
    return person.getName()

user1=Student("alice",23,"01011112222")
user2=Teacher("bob",25,"01033334444")

print(getPersonName(user1))
print(getPersonmane(user2)) """

#캡슐화
""" class Person : 
	def __init__(self, name, age, num) :
		self.name = name
		self.age = age
		self.number = num

	def getName(self) :

	def setName(self, new) :

	def getNumber(self) :

	def setNumber(self, newNum) :

p1.getNumber()
p2.getNumber()

p1.setNumber("11111111111")
p1.setNumber("22222222222")
 """