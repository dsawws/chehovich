def print_valid_cities(all_cities,used_cities): 
    valid_cities=all_cities-used_cities
    print("все города",all_cities)
    print('использованные города',used_cities)
    print("доступные города",valid_cities)


 
all_cities = { 
    'Абакан', 
    'Астрахань',  
    'Бобруйск',  
    'Калуга', 
    'Караганда', 
    'Кострома', 
    'Липецк',  
    'Новосибирск' 
} 
 
used_cities = {'Калуга', 'Абакан' , 'Новосибирск'} 
print_valid_cities(all_cities, used_cities)