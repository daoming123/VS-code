"""make_shirt."""


def make_shirt(one_size, pattern='I love Python'):
    """一个尺码以及要印到 T 恤上的字样."""
    print(f"\nThis T-shirt is {one_size} and has the pattern {pattern}.")

    make_shirt('size L')
    make_shirt('size M')
    make_shirt('size S', pattern='hello China')
    make_shirt('size L', 'hello World')
    make_shirt(one_size='size M', pattern='hello kitty')
