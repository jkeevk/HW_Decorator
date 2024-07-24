import requests
from logger_param import logger

@logger('superhero.log')
def super_hero():
    url = "https://akabab.github.io/superhero-api/api"
    response = requests.get(f'{url}/all.json')
    all_hero_info = response.json()
    heroes = {}
    for hero_info in all_hero_info:
        name = hero_info['name']
        if name == 'Hulk':
            heroes[hero_info['name']] = hero_info['powerstats']['intelligence']
        elif name == 'Captain America':
            heroes[hero_info['name']] = hero_info['powerstats']['intelligence']
        elif name == 'Thanos':
            heroes[hero_info['name']] = hero_info['powerstats']['intelligence']

    sorted_people = sorted(heroes.items(), key=lambda item: item[1])
    result = sorted_people[-1][0]
    return result

if __name__ == '__main__':
    super_hero()
