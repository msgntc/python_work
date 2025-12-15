def cars(manufacturer, model, **car_info):
    """
    Docstring for cars
    
    :param manufacturer: Description
    :param model: Description
    :param car_info: Description
    """
    car_info['manufacturer_'] = manufacturer
    car_info['model_'] = model
    return car_info
car = cars('subaru', 'outback', color='blue', tow_package=True)
print(car)