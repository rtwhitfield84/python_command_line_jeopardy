import requests
import random
import parser
import os




def jeopardy():
	random_jeopardy_key = random.randrange(9000,10000)
	r = requests.get('https://jeopartymode.firebaseio.com/{}.json'
					.format(random_jeopardy_key))

	print("\n""********************** \n"  
		"Command Line Jeopardy! \n" 
		"**********************")
	print("Enter q to quit")

	for k,v in r.json().items():
		if str(k) == 'answer':
			answer = v.lower()
		if str(k) == 'question':
			question = v
			parser.strip_tags(question)
		if str(k) == 'category':
			category = v
		if str(k) == 'value':
			value = v
		if str(k) == 'round':
			j_round = v
			
	print(j_round + '\n')
	print('Category \n' + category + '\n')
	print('Question \n' + question + '\n')

	user_answer = str(input('What is: ')).lower()
	if user_answer == answer:
		os.system('clear')
		print('correct')
		jeopardy()
	elif user_answer == 'q':
		print('Goodbye')
		exit()
	else:
		os.system('clear')
		print("incorrect")
		jeopardy()

if __name__ == '__main__':
	jeopardy()