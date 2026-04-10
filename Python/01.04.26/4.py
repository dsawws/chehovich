def get_together_games(anfisa_games,alisa_games):
    together_games = set(anfisa_games) & set((alisa_games))
    print(together_games)
anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
get_together_games(anfisa_games,alisa_games)