
from bs4 import BeautifulSoup
import requests 
import json

#To get the information from the object records on a specific page 
url = "https://denverartmuseum.org/collection?f%5B0%5D=field_co_department_term%3A1073&page=1"
results_page = requests.get(url)
page_html = results_page.text 
soup = BeautifulSoup(page_html, "html.parser")

all_labels = soup.find_all("div", attrs = {'class':'info'})

for a_div in all_labels:
	print('_______________________________________________________')
	print(a_div.text)

	alink = a_div.find('a')

	abs_url = 'https://denverartmuseum.org'+ alink['href']
	#print(abs_url)
	item_request = requests.get(abs_url)
	item_html = item_request.text
	item_soup = BeautifulSoup(item_html, "html.parser")
	all_field_divs = item_soup.find_all("div", attrs={'class':'field-value'})
	


#Project Notes: 
# In order to get the text that is included in the headings alongside "field value", use the "next sibling" method
#Suggested additions once I'm reading to scrape the whole website: 
	#To delay the code somewhat so that I'm not constantly scraping the whole site:
		#import time module “import time”
		#time.sleep( how many seconds you want it to sleep)
	#To scrape multiple pages: 	
		#for page in range (1,58): 
	#url = “https://///whatever page = + pages