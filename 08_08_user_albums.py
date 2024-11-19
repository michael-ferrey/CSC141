def make_album(artist, title, number_of_songs=None):
    album = {'artist': artist,'title': title,}
    return album

while True:
    print("\nPlease enter the album details (or type 'quit' to exit):")
    
    artist = input("Artist: ")
    if artist.lower() == 'quit':
        break
    
    title = input("Title: ")
    if title.lower() == 'quit':
        break
    
    
    album = make_album(artist, title)
    
    print(album)
