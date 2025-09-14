def make_album(artist_name, album_title, number_of_songs=None):
    """返回包含专辑信息的字典"""
    album = {
            'artist': artist_name.title(),
            'album': album_title.title()
             }
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

while True:
    print("\nPlease enter the name of your favorite singer and Album name:")
    print("(enter 'q' at any time to quit)")
    favorite_singer = input("favorite_singer: ")
    if favorite_singer == 'q':
        break
    Album_name = input("Album name: ")
    if Album_name == 'q':
        break

    user_input = make_album(favorite_singer, Album_name)
    print(user_input)

