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




while True:
    a= int(input("число а "))
    b=int(input("число b "))
    c=input("оператор ")

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