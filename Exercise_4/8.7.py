def make_album(artist, album_title, num_tracks=None):
    album = {
        "artist": artist,
        "album_title": album_title
    }

    if num_tracks:
        album["tracks"] = num_tracks

    return album

album1 = make_album("Radiohead", "In Rainbows")
album2 = make_album("Dave Matthews Band", "Crash")
album3 = make_album("Deftones", "Koi No Yokan")

print(album1)
print(album2)
print(album3)

album4 = make_album("Aphex Twin", "Selected Ambient Works 85-92", 13)
print(album4)
