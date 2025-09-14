
def make_shirt(One_size, Pattern ='I love Python'):
    """一个尺码以及要印到 T 恤上的字样"""
    print(f"\nThis T-shirt is {One_size} and has the pattern {Pattern}.")

make_shirt('size L')
make_shirt('size M')
make_shirt('size S', Pattern ='hello China')
make_shirt('size L', 'hello World')
make_shirt(One_size = 'size M', Pattern ='hello kitty')