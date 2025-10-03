<<<<<<< HEAD
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含有关用户的简介"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile(
    'zhong', 'jialing',
    hometown='Jiang_Xi',
    birthday='2007_July_16',
    favorite_color='Blue'
)

print(user_profile)
=======
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含有关用户的简介"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile(
    'zhong', 'jialing',
    hometown='Jiang_Xi',
    birthday='2007_July_16',
    favorite_color='Blue'
)

print(user_profile)
>>>>>>> ddb9f76865614855e9dbead36ef2c8d652b156f5
