def make_album(Artist_name, Album_title, Number_of_songs=None):
    """返回包含专辑信息的字典"""
    album = {
            'artist': Artist_name.title(),
            'album': Album_title.title()
             }
    if Number_of_songs:
        album['Number_of_songs'] = Number_of_songs
    return album

album1 = make_album('Taylor Swift','1998', Number_of_songs=5)
album2 = make_album('Jay Chou','Fantasy')
album3 = make_album('Adele','say_Hello')
print(album1)
print(album2)
print(album3)