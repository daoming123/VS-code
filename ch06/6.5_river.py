rivers = {'nile': 'egypt', 'Yangtze': 'China', 'Amazon': 'Brazil'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
for river in rivers:
    print(river.title())
for country in rivers.values():
    print(country.title())
