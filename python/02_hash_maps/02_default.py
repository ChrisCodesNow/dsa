from collections import defaultdict


def group_by_state(cities_list):
    cities_by_state = defaultdict(list)

    for state, city in cities_list:
        cities_by_state[state].append(city)

    return cities_by_state


def display_cities(cities_by_state):
    for state, cities in cities_by_state.items():
        cities = ', '.join(cities)
        line = state + ': ' + cities
        print(line)


if __name__ == '__main__':
    city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

    cities_by_state = group_by_state(city_list)
    display_cities(cities_by_state)