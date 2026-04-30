from collections import namedtuple,Counter,deque

# Student = namedtuple('Student',['id','name','age'])
# s1 = Student(101,"harry",23)

# print(s1.id)
# print(s1.name)
# print(s1.age)


# print(Counter(['A','B','A','C','B','C','B']))
# print(Counter({'A':5,'B':10,'C':11}))
# print(Counter(a=5,b=4))

# dq = deque([9,2,3,4,5])

# dq.append(6)
# dq.appendleft(0)

# dq.pop()
# dq.popleft()

# print(dq)

# from collections import defaultdict


# dd = defaultdict(int)

# dd['apple'] += 1
# dd['banana' ] += 2
# dd['apple'] +=3

# print(dd)


# from collections import OrderedDict

# od = OrderedDict()

# od['name'] = "harry"
# od['age'] = 24
# od['address'] = 'ktm'


# print(od)


# od.move_to_end('name')

# print(od)

# od.move_to_end('address', last=False)

# print(od)


# from collections import defaultdict

# d = defaultdict(int)

# data = [1,2,3,2,1,2,3,4,1,2,9]

# for i in data:
#     d[i]+=1
    
# print(d)


# Iterator example

# class SelfRange:
#     def __init__(self,s,e):
#         self.s = s
#         self.e = e
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.s < self.e:
#             s = self.s
#             self.s+=1
#             return s
#         else:
#             raise StopIteration
        
        
# for i in SelfRange(1,10):
#     print(i)
    
    
# difference between iterabale and iterator

# iterable --> we can looped over iterable, eg:list,tuple,__iter__ only
# iterator --> it is an object that allows programmer to traverse sequence of data without having store entire data in memeory, eg:iterator, it uses __iter__ and __next__ both 




# def generators():
#     yield 'first'
#     yield 'second'
#     yield 'third'
    
    
# c = generators()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))


# def decorators(func):
#     def wrapper():
#         print("Before actual function ")
#         func()
#         print("After actual function exectution")
#     return wrapper
    
    
# @decorators

# def greet():
#     print("hello world")
    
# greet()


# def display(*args,**kwargs):
#     print("positional arguments:",args)
#     print("keyword arguments:",kwargs)
    
    
# display('ram','shyam','kathmandu',20,age=30,city="pokhara")


# def factorial(x):
#     if x==0:
#         return 1
#     else:
#         return x * factorial(x-1)
    
    
# print(factorial(5))


# def fact(x):
#     f = 1
#     for i in range(1,x+1):
#         f*=i
#     return f
        
# print(fact(5))

# sq =lambda x:x**2
# print(sq(5))

my_list = [1,2,3,4,5,6,8]

# even = list(filter(lambda x:x%2==0,my_list))
# print(even)

# sq = map(lambda x:x**2, my_list)
# print(list(sq))

# from functools import reduce

# sum = reduce(lambda x,y:x+y,my_list)
# print(sum)


# class Teacher:
#     def __init__(self,id,name,salary):
#         self.__id = id
#         self.__name = name
#         self.__salary = salary
        
        
#     # Setter method
#     def get_details(self):
#         return self.__id,self.__name
    
#     # def set_salary(self,salary):
#     #     if salary>0:
#     #         self.__salary = salary
#     #     else:
#     #         print("Salary must be posivive")
    
#     # Getter method
#     def get_salary(self):
#         return self.__salary
    
# class Student(Teacher):
#     def __init__(self, id,name,salary,subject):
#         super().__init__(id,name,salary)
        
#         self.subject = subject
        
#     def display(self):
#         print("ID:", self.get_details()[0])
#         print("Name:", self.get_details()[1])
#         print("Salary:", self.get_salary())
#         print("Subject:", self.subject)

    
    

# obj = Student(12,"Alice",5000,"Math")

# obj.display()

# class Animal:
#     def speaks(self):
#         print("Animal makes sound")
        
# class Dog(Animal):
#     def speaks(self):
#         print("Dogs barks")
        
# class Cat(Animal):
#     def speaks(self):
#         print("Cate meows")
        
# animals = [Animal(),Dog(),Cat()]

# for i in animals:
#     i.speaks()
 
 
# class Math:
#     def add(self,a,b=0,c=0):
#         return a+b+c
# obj = Math()
# print(obj.add(3,5))

# protected variable and methods are not accessible outside the class but accessed through base class that inherits the parent class and defined by _ in the beginning of the variable or method name
# class Parent:
#     def __init__(self):
#         self._protected_var = 20
        
#     def _protected_method(self):
#         print("this is protected method")
     
# class Base(Parent):
#     def __init__(self):
#         super().__init__()
        
#     def access_protected(self):
#         print(self._protected_var)
        
# obj = Base()


# try:
#     # file = open('file.txt','r')
#     # data = file.read()
#     x = int(input("Enter a number"))
#     y = 20/x

# except ZeroDivisionError:
#     print("Divisible by zero is not allowed")
    
# except ValueError:
#     print("value must be an integer")
    
# except FileNotFoundError:
#     print("file doesn't exists")

# else:
#     print("Division successful:",y)
    
# finally:
#     print("This runs always")
    
# age = -23
# if age<0:
#     raise ValueError("age must be positive")
    
data = [
    ["name","age","city"],
    ["harry",23,"kathmandu"]
]

# import csv

# with open('output.csv','w',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
    
# with open('output.csv','r') as file:
#     r = csv.reader(file)
#     for row in r:
#         print(row)
        
data1 = {
    "name":"harry",
    "age":23
}
import json
with open('hello.json','w') as file:
    json.dump(data1,file)
    
    
