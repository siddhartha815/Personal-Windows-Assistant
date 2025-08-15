import requests



# Chuck Norris API
chuck_norris_api = "(Chuck Norris API)"

# JokeAPI
random_joke = "(Joke API)"



def chuck_norris_jokes():
    cn_data = requests.get(chuck_norris_api)
    cn_json = cn_data.json()

    return cn_json

def random_jokes():
    joke_data = requests.get(random_joke)
    joke_json = joke_data.json()

    return joke_json