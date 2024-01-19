import requests

headers = {
        "X-RapidAPI-Key": "f1ab364b9amsh47af4fe40162754p1f1b53jsne8e93ad1642d",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }


def wordAPI_everything(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"
    response = requests.get(url, headers=headers)

    return response.json()


def wordAPI_define(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"
    response = requests.get(url, headers=headers)

    return response.json()


def wordAPI_synonyms(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/synonyms"
    response = requests.get(url, headers=headers)

    return response.json()


def wordAPI_antonyms(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/antonyms"
    response = requests.get(url, headers=headers)

    return response.json()


def wordAPI_pronunciation(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/pronunciation"
    response = requests.get(url, headers=headers)

    return response.json()


def wordAPI_syllables(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/syllables"
    response = requests.get(url, headers=headers)

    return response.json()


def wordAPI_examples(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/examples"
    response = requests.get(url, headers=headers)

    return response.json()


def wordAPI_partOf(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/partOf"
    response = requests.get(url, headers=headers)

    return response.json()


