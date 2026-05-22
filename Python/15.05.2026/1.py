from tkinter import * 
window = Tk() #Создаем окно 
frame_top = Frame(window)#Фрейм для верхнего ряда 
frame_bot = Frame(window)#Фрейм для нижнего ряда 
# Создаем четыре метки с привязкой к конкретному 
lab_1= Label(frame_top, width=8, height=3, bg='yellow', text="1") 
lab_2 =Label(frame_top, width=8, height=3, bg='red', text="2") 
lab_3 =Label(frame_bot, width=8, height=3, bg='lightgreen', text="3") 
lab_4 = Label(frame_bot, width=8, height=3, bg='lightblue', text="4") 
# Располагаем фреймы вертикально один под другим 
frame_top.pack() 
frame_bot.pack() 
#Располагаем метки во фреймах слева направо 
10 
lab_1.pack(side = LEFT) 
lab_2.pack(side = LEFT) 
lab_3.pack(side = LEFT) 
lab_4.pack(side = LEFT) 
#Цикл обработки событий окна 
window.mainloop() 