cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


# def get_all_jeeps():
#     jeeps = cars['Jeep']
#     models = ', '.join(jeeps)
#     return models

def get_all_jeeps():
    return ', '.join(cars['Jeep'])


# def get_first_model_each_manufacturer():
#     firstmodels = []
#     for maker in cars:
#         models = cars[maker]
#         firstmodels.append(models[0])
#     return firstmodels

def get_first_model_each_manufacturer():
    return [models[0] for models in cars.values()]


# def get_all_matching_models(grep='trail'):
#     search_result = []
#     for models in cars.values():
#         for model in models:
#             if grep.lower() in model.lower():
#                 search_result.append(model)
#     search_result.sort()
#     return search_result


def get_all_matching_models(grep='trail'):
    grep = grep.lower()
    models = sum(cars.values(), [])  # flatten list of lists
    matching_models = [model for model in models
                       if grep in model.lower()]
    return sorted(matching_models)


# def sort_car_models():
#     new_cars = {}
#     for maker in cars:
#         models = cars[maker]
#         models.sort()
#         new_cars[maker] = models
#     return new_cars

def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    return {manufacturer: sorted(models) for
            manufacturer, models in cars.items()}
