def make_album(name, title, tracks=None):
    """Return a dictionary of information about a music album."""
    if tracks:
        album = {'artist_name': name, 'album_title': title, 'tracks': tracks}
    else:
        album = {'artist_name': name, 'album_title': title}
    return album
album = make_album('lena raine', 'celeste ost')
print(album)
album = make_album('christopher larkin', 'silksong ost')
print(album)
album = make_album('daniel pemberton', 'across the spider-verse ost')
print(album)
album = make_album('Atsuko Asahi', 'mario kart world ost', tracks=237)
print(album)

while True:
    print("\nEnter album information (or 'q' to quit):")
    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break
    title = input("Album title: ")
    if title.lower() == 'q':
        break
    tracks_input = input("Number of tracks (press Enter to skip): ")
    if tracks_input.lower() == 'q':
        break
    if tracks_input.strip() == '':
        tracks = None
    else:
        try:
            tracks = int(tracks_input)
        except ValueError:
            print("Invalid number of tracks. Skipping tracks info.")
            tracks = None
    user_album = make_album(artist, title, tracks)
    print(user_album)