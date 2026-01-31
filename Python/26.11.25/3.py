s_p= 0
s_n= 0

num= int(input("введите количество чисел: "))

for i in range (1, num+1):
    ch= int(input("введите число"))
    if ch > 0:
        s_p=s_p+ch
    else:
        s_n=s_n+ch
print (s_p-s_n)

