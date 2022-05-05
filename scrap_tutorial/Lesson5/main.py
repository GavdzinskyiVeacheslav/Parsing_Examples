import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_data(url):

	headers = {

		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"Accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
		"User-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrom",
		}

	r = requests.get(url=url, headers=headers)

	with open("index.html", 'w', encoding='utf-8') as file:
		file.write(r.text)

	# get hotels urls 
	r = requests.get("https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most", headers=headers)
	soup = BeautifulSoup(r.text, "lxml")

	hotels_cards = soup.find_all("div", class_='hotel_card_dv')

	for hotel_url in hotels_cards:
		hotel_url = hotel_url.find("a").get("href")
		print(hotel_url)


def get_data_with_selenium(url):
	options = webdriver.ChromeOptions()
	#options.add_argument('--headless')
	
	# try:
	# 	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
			
	# 		options=options,
	# 	)
	# 		#executable_path="D:/Desktop/Parsing_Examples/scrap_tutorial/Lesson5/chromedriver.exe",
		

	# 	driver.get(url=url)
	# 	time.sleep(5)

	# 	with open('index_selenium.html', 'w', encoding='utf-8') as file:
	# 		file.write(driver.page_source)
	# except Exception as ex:
	# 	print(ex)
	# finally:
	# 	driver.close()
	# 	driver.quit()

	with open("index_selenium.html", encoding='utf-8') as file:
		src = file.read()

		# get hotels urls 
		
	soup = BeautifulSoup(src, "lxml")

	hotels_cards = soup.find_all("div", class_='hotel_card_dv')

	for hotel_url in hotels_cards:
		hotel_url = "https://tury.ru/" + hotel_url.find("a").get("href")
		print(hotel_url)


def main():
	#get_data("https://tury.ru/hotel/most_luxe.php")
	get_data_with_selenium('https://tury.ru/hotel/most_luxe.php')



if __name__ == '__main__':
	main()