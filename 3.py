import random
b=10
a = [random.randint(1,100) for i in range(b)]
print(a)

max=max(a)
print(max)

max2=sorted(a)
print(max2)
print(max2[b-2])
