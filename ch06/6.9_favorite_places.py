favorite_places = {
        'mary': ['china', 'london'],
        'sarah': ['japan', 'korea', 'russia'],
        'yuki': ['india', 'russia', 'china'],
        }
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
