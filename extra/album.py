def make_album(artist, title, traks =None):
    album = {'artist': artist, 'title': title}
    if traks:
        album['traks'] = traks
    return album
print(make_album('Conner Price', 'Buddy System'))
print(make_album('I Dont Know', 'WHen the Game sys NO'))
print(make_album('Chumbawamba', 'The Boy Bands Have Won'))
while True:
    artist = input("enter an Artist or q to quit ")
    if artist.lower() == 'q':
        break

    title = input("Enter the album title: ")
    album = make_album(artist, title)
    print(album)
