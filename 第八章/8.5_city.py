"""make_album."""


def describe_city(city_name, the_country='China'):
    """一座城市的名字以及该城市所属的国家."""
    print(f"{city_name} is in {the_country}")

    describe_city('Jiang_Xi')
    describe_city('Bei_Jing')
    describe_city('Tokyo', the_country='Japan')
