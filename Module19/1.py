violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
songs_input = int(input('Сколько песен выбрать? '))
continuity = 0
for x in range(1, songs_input + 1):
    song_choice = input(f'Название {x}-ой песни: ')
    continuity += violator_songs.get(song_choice)
print('Общее время звучания песен: {} минуты'.format(round(continuity, 2)))
