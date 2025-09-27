def make_album(artist_name, album_title, number_of_songs=None):
    """返回包含专辑信息的字典"""
    album = {
            'artist': artist_name.title(),
            'album': album_title.title()
             }
    if number_of_songs:
        album['Number_of_songs'] = number_of_songs
    return album

album1 = make_album('Taylor Swift', '1998', number_of_songs=5)
album2 = make_album('Jay Chou', 'Fantasy')
album3 = make_album('Adele', 'say_Hello')

print(album1)
print(album2)
print(album3)
