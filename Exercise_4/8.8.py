def make_album(artist, album_title, num_tracks=None):
    album = {
        "artist": artist,
        "album_title": album_title
    }

    if num_tracks:
        album["tracks"] = num_tracks

    return album


while True:
    print("\nEnter album information (type 'q' to quit)")

    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break

    album_title = input("Album title: ")
    if album_title.lower() == 'q':
        break

    tracks = input("Number of tracks (press Enter to skip): ")

    if tracks:
        album = make_album(artist, album_title, int(tracks))
    else:
        album = make_album(artist, album_title)

    print("\nAlbum created:")
    print(album)
