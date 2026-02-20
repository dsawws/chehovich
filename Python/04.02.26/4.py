import math
def plus (a,b):
    print (a+b)
def minus(a,b):
    print(a-b)
def f(a,b):
    print(a*b)
def f1(a,b):
    print(a/b)
def z (a,b):
    print(a**b)
def sin (a):
    a_rad= math.radians(a)
    print(math.sin(a_rad))
def cos (a):
    a_rad= math.radians(a)
    print(math.cos(a_rad))
def tan (a):
    a_rad= math.radians(a)
    print(math.tan(a_rad))

while True:
    try:
        c=input("оператор ")
        if c =="sin":
             a= int(input("число а "))
        elif c =="cos":
             a= int(input("число а "))
        elif c =="tan":
             a= int(input("число а "))
        else:
            a= int(input("число а "))
            b=int(input("число b "))

        if c=="+":
            plus(a,b)
        elif c == "-":
            minus(a,b)
        elif c == "*":
            f(a,b)
        elif c == "/":
            f1(a,b)
        elif c=="**":
            z(a,b)
        elif c =="sin":
            sin(a)
        elif c =="cos":
            cos(a)
        elif c =="tan":
            tan(a)
    except ValueError:
        print('отшибка ввода')
            
    except ZeroDivisionError:
        print('деление на нольdffgsdf')







