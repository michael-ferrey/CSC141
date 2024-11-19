def make_album(artist, title, number_of_songs=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if number_of_songs is not None:
        album['number_of_songs'] = number_of_songs
    return album

album1 = make_album("Drake", "More Life")
album2 = make_album("Lil Uzi Vert", "Pink Tape")
album3 = make_album("Polo G", "Hall of Fame", 4)

print(album1)
print(album2)
print(album3)
