population_data = {
    'Norway': 5332334,
    'Sweden': 10887665,
    'Finland': 5443221,
    'Denmark': 344545,
}


def find_below_10m(population_by_country: dict) -> list:
    result = []
    for country_name, population in population_by_country.items():
        if population < 10_000_000:
            result.append(country_name)
    
    return result


below_10m = find_below_10m(population_data)
# print(below_10m)


music_groups = {'BTS': 3, 'BlackPink': 4}
other_groups = {'X-Japan': 5, 'BTS': 6}

music_groups.update(other_groups)
print(music_groups)


default_settings = {
    'show_bar': False,
    'always_close': True,
    'never_abandon': True,
}

user_settings = {
    'always_close': False,
}


default_settings.update(user_settings)
settings = default_settings