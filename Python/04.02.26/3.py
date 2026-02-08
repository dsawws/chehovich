n1=0
def f (n1):
    while True:
        n=int(input('ввод '))
        if n <0:
            n1=n1+n
            print (n1)
        else:
            n=n**2
            print (n)    

f(n1)