welcome = 'Welcome to my Nightmare', 'Alice Cooper', 1975
bad = 'Bad Company', 'Bad Company', 1974
budgie = 'Nightflight', 'Budgie', 1981
imelda = 'More Mayhem', 'Emilda May', 2011
metallica = 'Ride the Lightning', 'Metallica', 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
# tuples are immutable.
# tuples use less memory than lists due to the less methods they have.

print()
# we have to convert a tuple into a list to be able to change items
metallica2 = list(metallica)
print(metallica2)
metallica2[0] = 'Master of Puppets'
print(metallica2)
