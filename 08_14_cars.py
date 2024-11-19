def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('Subaru', 'Crosstrek', color='Blue Pearl', tow_package=True)

print(car)
