import requests

url = 'https://psychotype-joker.ru/api/jokes/random_joke/'
response = requests.get(url)
joke = response.json()
print(joke['text'])


#https://psychotype-joker.ru/api/storys/random_story/