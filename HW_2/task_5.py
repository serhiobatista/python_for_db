violator_songs = [
    ['World in My Eyes', 4.86,],
    ['Sweetest Perfection', 4.43,],
    ['Personal Jesus', 4.56,],
    ['Halo', 4.9,],
    ['Waiting for the Night', 6.07,],
    ['Enjoy the Silence', 4.20,],
    ['Policy of Truth', 4.76,],
    ['Blue Dress', 4.29,],
    ['Clean', 5.83,],
]

cnt_song = int(input('Сколько песен выбрать? '))
playlist_songs = list()
for num_song in range(1, cnt_song + 1):
    song_name = input('Название {}-й песни: '.format(num_song))
    playlist_songs.append(song_name)
total_duration = 0
for idx in range(len(violator_songs)):
    if violator_songs[idx][0] in playlist_songs:
        total_duration += violator_songs[idx][1]
print('Общее время звучания песен: {} минуты'.format(round(total_duration, 2)))



