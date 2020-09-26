albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

while True:
    print('Please select the album')
    for album_nbr, album in enumerate(albums):
        print('{}: {}'.format(album_nbr + 1, album[0]))
    album_choice = int(input())
    if 0 < album_choice < 5:

        if album_choice == 1:
            print('Please select the song you want')
            for song_nbr, songs in albums[album_choice - 1][3]:
                print('{}: {}'.format(song_nbr, songs))
            song_choice = int(input())
            nbr, song = albums[album_choice - 1][3][song_choice - 1]
            print('Playing the song {}: {}'.format(nbr, song))
            print('=====================================')

        if album_choice == 2:
            print('Please select the song you want')
            for song_nbr, songs in albums[album_choice - 1][3]:
                print('{}: {}'.format(song_nbr, songs))
            song_choice = int(input())
            nbr, song = albums[album_choice - 1][3][song_choice - 1]
            print('Playing the song {}: {}'.format(nbr, song))
            print('=====================================')

        if album_choice == 3:
            print('Please select the song you want')
            for song_nbr, songs in albums[album_choice - 1][3]:
                print('{}: {}'.format(song_nbr, songs))
            song_choice = int(input())
            nbr, song = albums[album_choice - 1][3][song_choice - 1]
            print('Playing the song {}: {}'.format(nbr, song))
            print('=====================================')

        if album_choice == 4:
            print('Please select the song you want')
            for song_nbr, songs in albums[album_choice - 1][3]:
                print('{}: {}'.format(song_nbr, songs))
            song_choice = int(input())
            nbr, song = albums[album_choice - 1][3][song_choice - 1]
            print('Playing the song {}: {}'.format(nbr, song))
            print('=====================================')

    else:
        break




