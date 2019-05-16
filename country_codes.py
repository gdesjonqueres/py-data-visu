from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Returns a pygal country code given a  country name"""
    # values = list(COUNTRIES.values())
    # keys = list(COUNTRIES.keys())
    #
    # try:
    #     index = values.index(country_name)
    # except ValueError:
    #     # Not found
    #     return None
    #
    # return keys[index]

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    return None
