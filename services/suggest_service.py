import requests


class YandexMapSuggestService:
    def __init__(self):
        self.apiKey = "910e3126-6d29-4d1c-8b09-321db6b2a40b"

    def getSuggestions(self, text):
        return requests.get(f'https://suggest-maps.yandex.ru/v1/suggest?apikey={self.apiKey}&text={text}').json()
