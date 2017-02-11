import requests
import random

def jeopardy():
	random_jeopardy_key = random.randrange(9000,10000)
	r = requests.get('https://jeopartymode.firebaseio.com/{}.json'
					.format(random_jeopardy_key))

	print("\n""********************** \n"  
		"Command Line Jeopardy! \n" 
		"**********************")

	for k,v in r.json().items():
		if str(k) == 'answer':
			answer = v
		if str(k) == 'question':
			question = v
		if str(k) == 'category':
			category = v
		if str(k) == 'value':
			value = v
		if str(k) == 'round':
			j_round = v
		print(k,v+'\n')

	user_answer = str(input('What is: '))
	if user_answer == answer:
		print('correct')
jeopardy()