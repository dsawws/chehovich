while True:
    x=int(input('введите число '))
    if x>0:
        a=x**2
        print(a)
    elif x == 0:
        print('конец цикла')
        break
    else:
        b= x**0.5
        print(b)