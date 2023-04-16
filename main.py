from pprint import pprint
import requests

def request():

    url = 'https://akabab.github.io/superhero-api/api/all.json'

    response = requests.get(url)

    if response.status_code == 200:
        print('Good jod! Let\'s continue!\n')
    if response.status_code != 200:
        print('Where is  200?\n')

    info = response.json()

    three_superheroes = ['Hulk', 'Captain America', 'Thanos']

    three_superheroes_list = []
    for i in info:
        for n in three_superheroes:
            if i['name'] == n:
                three_superheroes_list.append(i)

    intelligence = []

    for i in three_superheroes_list:
        intelligence.append(i['powerstats']['intelligence'])
    for i in three_superheroes_list:
        if i['powerstats']['intelligence'] == max(intelligence):
            print(f"The most intellegence superhero {i['name']}.")

request()