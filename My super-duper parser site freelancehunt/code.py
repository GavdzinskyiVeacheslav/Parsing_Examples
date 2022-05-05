import requests
from bs4 import BeautifulSoup
import json

job_descriptions_url_list = []
titles = []
for i in range(1): # number 4 all pages - number 2 only first page to keep track of the latest added orders
	url = f'https://freelancehunt.com/projects?skills[]=22&page={i}'

	print(url)

	q = requests.get(url)
	result = q.content

	soup = BeautifulSoup(result, 'lxml')	
	job_descriptions = soup.find_all(class_='biggest visitable')
 		
	for task in job_descriptions:
		titles.append(task.text)
		task_page_url = 'https://freelancehunt.com'+ task.get('href')
		job_descriptions_url_list.append(task_page_url)



with open('job_descriptions_url_list.txt', 'w', encoding="utf-8") as file:
	for line in job_descriptions_url_list:
		file.write(f'{line}\n')

#---------------------------------------------------------------------------

with open('job_descriptions_url_list.txt', encoding="utf-8") as file:
	lines = [line.strip() for line in file.readlines()]

data_dict = [] 
count = 0


for line in lines:
	q = requests.get(line)
	result = q.content


	soup = BeautifulSoup(result, 'lxml')
	task = soup.find(id="project-description").text

	data_dict.append(task)

with open('data/New.txt', 'w', encoding='utf-8') as file:
	d = dict(zip(titles, data_dict))
	for k, v in d.items():
		file.write(f'{k}{v}\n')
