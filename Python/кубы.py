
w=float(input('длина ребра: '))
P=float(input('плотность: '))

kub= w ** 3
mass= P*kub
total_mass= mass *6

print ('общая масса: ', total_mass)
print ('масса одного куба:', mass)
