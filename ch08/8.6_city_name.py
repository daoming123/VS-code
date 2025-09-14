def city_country(city_name, The_country):
    """返回城市的名称及其所属的国家的字符串"""
    return f"{city_name.title()}, {The_country.title()}"

print(city_country("santiago", "chile"))
print(city_country("beijing", "china"))
print(city_country("new york", "usa"))