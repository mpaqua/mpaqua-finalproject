from bs4 import BeautifulSoup
from random import randint
import requests, json, re, time

#Delay when scraping pages to avoid being blocked:
time.sleep(randint(1,5))

#Using a function to run a regex to identify object numbers in the absolute url:
def find_numbers(url_text):
	url_text = url_text.replace("https://denverartmuseum.org/object/", "")
	number_regex=re.compile('[0-9\.]+')
	results = number_regex.findall(url_text)
	if len(results)>0:
		return results[0]
	else:
		return None
	#return number_regex.findall(url_text)

#Using a function to run a regex to isolate year dates in the provenance line:
def find_dates(html_text):
	date_regex = re.compile('[0-9]{4}')
	return date_regex.findall(html_text)

#List to write dictionary out to JSON
all_data = []

#To scrape multiple pages:
for i in range(0,59):
	page="https://denverartmuseum.org/collection?f%5B0%5D=field_co_department_term%3A1073&page={}".format(i)
	html = requests.get(page)
	results_page = requests.get(page)
	page_html = results_page.text
	soup = BeautifulSoup(page_html, "html.parser")


	all_labels = soup.find_all("div", attrs = {'class':'info'})

	for a_div in all_labels:
		alink = a_div.find('a')

		abs_url = 'https://denverartmuseum.org'+ alink['href']
		item_request = requests.get(abs_url)
		item_html = item_request.text
		item_soup = BeautifulSoup(item_html, "html.parser")

		#Title:
		title = item_soup.find("h1", attrs={"class": "object-title"})
		print("Title:", title.text)

		#Date Created:
		created = item_soup.find("h2", attrs={"class": "object-date"})
		if created != None:
			print("Date Created:", created.text)

		#Object Number:
		object_number= find_numbers(abs_url)
		print("Object Number", object_number)

		#Culture:
		cultures_data = []
		culture = item_soup.find("h2", text="Culture")
		if culture != None:
			all_culture_values = culture.find_next_sibling()
			tribes = all_culture_values.find_all("li")
			for tribe in tribes:
				cultures_data.append(tribe.text)
				print("Culture:", cultures_data)

		#Known Provenance
		provenance_data = []
		provenance = item_soup.find("h2", text="Known Provenance")
		if provenance != None:
			all_provenance_values = provenance.find_next_sibling("div", attrs={"class": "field-value"})
			dates = find_dates(all_provenance_values.text)
			print("Provenance:",dates)

		#Exhibition History
		exhibition_data = []
		exhibition = item_soup.find("h2", text="Exhibition History")
		if exhibition != None:
			all_exhibitions = exhibition.find_next_sibling()
			exhibitions = all_exhibitions.find_all("li")
			for exhibition in exhibitions:
				print("Exhibition History:",exhibition.text)
				exhibition_data.append(exhibition.text)

		print('_______________________________________________')
		data = {
			"title":title.text,
			"objectnumber":object_number,
			"datecreated":created.text,
			"cultures": cultures_data,
			"provenance": dates,
			"exhibitions": exhibition_data}
		all_data.append(data)

	#Print Results to JSON File
	with open("data.json", "w") as outfile:
		json.dump(all_data,outfile, indent= 2)
