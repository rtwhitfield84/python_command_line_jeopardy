import requests
import random

def jeopardy():
	random_jeopardy_key = random.randrange(9000,10000)
	r = requests.get('https://jeopartymode.firebaseio.com/{}.json'
					.format(random_jeopardy_key))

	print(r.json())

jeopardy()