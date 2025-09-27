def make_car(make, model, **car_info):
    """创建一个字典，其中包含制造商和型号和其他关于车子的信息"""
    car_info['manufacturer'] = make
    car_info['car model'] = model
    return car_info

car_information = make_car(
    'BMW', '225L',
    color='Blue',
    Optional_accessories='sound system'
)

print(car_information)
