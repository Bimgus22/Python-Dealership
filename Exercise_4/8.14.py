def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car
my_car = make_car(
    manufacturer="Tesla",
    model="Model 3",
    color="Red",
    autopilot=True
)
print(my_car)