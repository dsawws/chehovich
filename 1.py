try :
    a=int(input())
    c=int(input())
    b=a/c
                                                                                                                                                                                                                                    

except Exception:
    print('ошибка')
except ValueError:
    print('другая ошибка')
else:
    print(b)    