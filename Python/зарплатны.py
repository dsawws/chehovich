zp= int(input('введите зарплату: '))
ry= int(input('сколько работал первый работник: '))
rz= int(input('сколько работал второй работник: '))

zp_total= ry+rz

de= zp/zp_total

zpy= de*ry
zpx= de*rz

print ('работник y заработал:', zpy)
print ('работник x заработал:', zpx)
