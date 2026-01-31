S=0
P=1
k_p=0
k_o=0
n=int(input("введите число"))
while n != 1000:
    if n > 0:
        S=S+n
        k_p+=1
    else:
        P=P*n
        k_o+=1
    n=int(input("введите число"))
print (S,P,k_p,k_o)        