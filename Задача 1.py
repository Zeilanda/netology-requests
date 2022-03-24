import requests


def get_hero_intelligence(name: str):
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    find_hero_url = url + name
    resp = requests.get(find_hero_url).json()
    data = resp['results']
    for characteristics in data:
        if characteristics['name'] == name:
            intelligence = characteristics['powerstats']['intelligence']
            return int(intelligence)


hulk_intelligence = (get_hero_intelligence('Hulk'), 'Hulk')
cap_intelligence = (get_hero_intelligence('Captain America'), 'Captain America')
thanos_intelligence = (get_hero_intelligence('Thanos'), 'Thanos')

max_intelligence = max([hulk_intelligence, cap_intelligence, thanos_intelligence])
print(max_intelligence[1])
