num= int(input("введите количество чисел: "))
s= 0

for i in range (1, num+1):
    ch= int(input("введите число"))
    if abs (ch) > 10 :
        s= s+ch 
print (s)         