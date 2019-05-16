import json

from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code

filename = 'population_data.json'

world_pop = {}

with open(filename) as f:
    json_data = json.load(f)

    for pop_data in json_data:
        if pop_data['Year'] == '2010':
            country_name = pop_data['Country Name']
            country_pop = int(float(pop_data['Value']))
            country_code = get_country_code(country_name)

            if country_code:
                print('{} ==> {:,}'.format(country_code, country_pop))
                world_pop[country_code] = country_pop
            else:
                print('Error: no pygal code for ', country_name)
            # print('{} - {} ==> {:,}'.format(pop_data['Country Code'], pop_data['Country Name'], float(pop_data['Value'])))

cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in world_pop.items():
    if pop < 10**7:
        cc_pop_1[cc] = pop
    elif pop < 10**9:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))

wm_style = RS('#336699', base_style=LCS(value_font_family='googlefont:Raleway',
                  value_font_size=30,
                  value_colors=('white',)))
wm = World(style=wm_style, human_readable=True, print_values=True)
wm.title = "World Population in 2010, by Country"
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_population.svg')
