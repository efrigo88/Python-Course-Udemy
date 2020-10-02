""" TASK:
In this challenge I had to modify the code to repeat the list
of songs when the input is out of range
"""
# we import the list from another file
from jukebox_menu_source_list import albums

# we declare constants in capital letters and with under scores
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print('Please choose your album (invalid choice exits):')
    for index, (title, artist, year, songs) in enumerate(albums):
        print('{}: {}'.format(index + 1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
        keep_going = True
        real_song = True
    else:
        break

    while keep_going is True:
        print('Please choose your song:')
        for index, (track_number, song) in enumerate(songs_list):
            print('{}: {}'.format(index + 1, song))
        song_choice = int(input())

        if 1 <= song_choice <= len(songs_list):
            real_song = True
            while real_song is True:
                title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
                print('Playing: {}'.format(title))
                print('=' * 40)
                real_song = False
                keep_going = False
