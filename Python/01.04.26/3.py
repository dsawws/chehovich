def print_valid_cities(all_cities,used_cities):
    valid_cities=all_cities-used_cities
    print("все города",all_cities)
    print('использованные города',used_cities)
    print("доступные города",valid_cities)

def add_cities(all_cities, new_cities):
    all_cities.update(new_cities)
new_cities = [
    'Екатеринбург',
    'Выборг' ,
    'Владивосток',
    'Казань',
    'Why',
    'Йезд'
]
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
used_cities = { 'Калуга',  'Абакан' , 'Новосибирск'}
add_cities(all_cities, new_cities)
print_valid_cities(all_cities, used_cities)