
num1= int(input('введите чило 1 '))
num2= int(input('введите чило 2 '))
num3= int(input('введите чило 3 '))

if num1 == 0 or num2 == 0 or num3 == 0:
    print ("ошибка ввода")

else:
    i= (num1+num2+num3)/3
    print ('среднее арефмитиеское ',i)