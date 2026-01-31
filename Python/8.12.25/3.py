a=int(input("введите число"))
S=0

while a!=1000:
    if a<0:
        S=S+a   
    else:
        print (a**2)
    a=int(input("введите число"))


print(S)        