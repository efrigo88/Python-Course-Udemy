albums = [('Welcome to my Nightmare', 'Alice Cooper', 1975),
          ('Bad Company', 'Bad Company', 1974),
          ('Nightflight', 'Budgie', 1981),
          ('More Mayhem', 'Emilda May', 2011),
          ('Ride the Lightning', 'Metallica', 1984),
          ]

print(len(albums))
print()

# solution 1
for name, artist, year in albums:
    print('Album: {}, Artist: {}, Year: {}'
          .format(name, artist, year))


print()
# solution I came up with
for album in enumerate(albums):
    index, (name, artist, year), = album
    print('Album Number: {}, Name: {}, Artist: {}, Year: {}'
          .format(index + 1, name, artist, year))
