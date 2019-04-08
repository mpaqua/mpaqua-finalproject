from bs4 import BeautifulSoup
import requests
import json
import re
#import time
#time.sleep(15)


#To get the information from the object records on a specific page
url = "https://denverartmuseum.org/collection?f%5B0%5D=field_co_department_term%3A1073&page=1"
results_page = requests.get(url)
page_html = results_page.text
soup = BeautifulSoup(page_html, "html.parser")

all_labels = soup.find_all("div", attrs = {'class':'info'})

for a_div in all_labels:
	#print('_______________________________________________________')
	#print(a_div.text)

	alink = a_div.find('a')

	abs_url = 'https://denverartmuseum.org'+ alink['href']
	#print(abs_url)
	item_request = requests.get(abs_url)
	item_html = item_request.text
	item_soup = BeautifulSoup(item_html, "html.parser")

	#Title:
	title = item_soup.find("h1", attrs={"class": "object-title"})
	print(title.text)

	#Culture:
	cultures_data = []
	culture = item_soup.find("h2", text="Culture")
	all_culture_values = culture.find_next_sibling()
	tribes = all_culture_values.find_all("li")
	for tribe in tribes:
		#print(tribe.text)
		cultures_data.append(tribe.text)

	print("Culture", cultures_data)

	#Known Provenance
	provenance_data = []
	provenance = item_soup.find("h2", text="Known Provenance")
	if provenance != None:
		all_provenance_values = provenance.find_next_sibling("div", attrs={"class": "field-value"})
		#using a function to run a regex for year dates in the provenance
		def find_dates(date_regex):
			date_regex = re.compile('([0-9]',all_provenance_values)
			return results
		print(date_regex)

	#Exhibition History
	exhibition_data = []
	exhibition = item_soup.find("h2", text="Exhibition History")
	if exhibition != None:
		all_exhibitions = exhibition.find_next_sibling()
		exhibitions = all_exhibitions.find_all("li")
		for exhibition in exhibitions:
			print(exhibition.text)
			exhibition_data.append(exhibition.text)

	print('_______________________________________________________')


#Project Notes:
#Suggested additions once I'm ready to scrape the whole website:
	#To delay the code somewhat so that I'm not constantly scraping the whole site:
		#import time module “import time”
		#time.sleep( how many seconds you want it to sleep)
	#To scrape multiple pages:
		#for page in range (1,58):
	#url = “https://///whatever page = + pages
		#would this be something that you write a function for?
