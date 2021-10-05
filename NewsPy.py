import requests


def getData(key,search):

	r = requests.get(f'https://newsapi.org/v2/everything?q={search}&from=2021-09-29&sortBy=popularity&apiKey={key}').json()

	headlines = []
	descriptions = []
	try:
		for i in range(10):
			title = r['articles'][i]['title']
			description = r['articles'][i]['description']
			headlines.append(title)
			descriptions.append(description)
		for i in range(len(headlines)):
			print(f'{headlines[i]}\n {descriptions[i]}\n\n')
	except Exception as e:
		print(f'No results found for term {search} \n {e}')


key = "6d88448b5a8848a58e4bc8083b5b939c"
search = input("Search Something : ")
getData(key,search)    
