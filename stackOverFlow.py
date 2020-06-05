import requests
from bs4 import BeautifulSoup


print("""


      ___           ___                               
     /\__\         /\__\                      ___     
    /:/  /        /:/ _/_       ___          /\  \    
   /:/  /        /:/ /\__\     /\__\         \:\  \   
  /:/  /  ___   /:/ /:/ _/_   /:/__/          \:\  \  
 /:/__/  /\__\ /:/_/:/ /\__\ /::\  \      ___  \:\__\ 
 \:\  \ /:/  / \:\/:/ /:/  / \/\:\  \__  /\  \ |:|  | 
  \:\  /:/  /   \::/_/:/  /   ~~\:\/\__\ \:\  \|:|  | 
   \:\/:/  /     \:\/:/  /       \::/  /  \:\__|:|__| 
    \::/  /       \::/  /        /:/  /    \::::/__/  
     \/__/         \/__/         \/__/      ~~~~      

""")

question = input('Type a question : ')
words = question.split(' ')

url = 'https://stackoverflow.com/search?q='+'+'.join(words)

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all('a',class_='question-hyperlink')

mylist = []

for item in items :
	if item['href'].startswith('/questions/'):
		mylist.append(item['href'])


link = 'https://stackoverflow.com'+mylist[0]

try:
	page = requests.get(link)

	soup = BeautifulSoup(page.content, 'html.parser')

	items = soup.find_all('div', class_='post-text')

	mylist = []
	for item in items:
		mylist.append(item)
	print(mylist[1].text)
except: 
	print('No fu-----g clue!')