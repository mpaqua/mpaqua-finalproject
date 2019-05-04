# mpaqua-finalproject
About the Project 
  Stages of the Project
How to Use 

 Caveats to the Culture Mapping  
  I had initially planned to use the script found in the script "map.py" to identify the listed territories and convert them to a format that could be added to the Native-Land.ca url, allowing me to map the territories of the cultures represented in the Denver Art Museum's collection. This proved to be less straightforward than it initially seemed. 
  While Native-Land.ca is a useful resource for mapping indigenous territories, there were a lot of discrepancies between the names of the cultures that I scraped from the Denver Art Museum's collections website and their listed territory slugs -- which can be found here: or in their downloadable JSON file (see folder). I had originally planned to change map.py to write the final results into json and compare the two json files programmatically, but given the relatively small sample size and the level of detail needed to compare the two, I opted to go through the csv file and manually compare it to the list of territory slugs. 
  Many of the differences between the culture names were spelling discrepancies (c's instead of k's, for example), but other issues had to do with different levels of specificity between the two resources. For instance, the Denver Art Museum had detailed records for particular tribes or branches of the Pueblo peoples, but Native-Lands only had a slug for "Pueblo"; likewise, the Denver Art Museum had very generic and outdated names for Alaskan indigenous groups, and the Native-Lands general slug "Inuit" had to be applied in cases where the only identifying cultural term in the data was the (now considered pejorative) term "Eskimo." For a full list of the changes made between the maps.py csv and the final mapping data, see the text file "Mapping Changes." There were also several groups where either not enough specificity was provided by the Denver Art Museum to assign a specific slug (and no generic slug existed) OR where there were cultures that were simply not represented by Native-Lands.ca. For a complete list of these issues see the text file "Unresolved Mapping Questions".
  Additionally, because of the nature of the Native Arts collect at the Denver Art Museum, works are included in the collection from other indigenous cultures or tribal groups beyond North and South America. These were identified and put into a separated .xlsx file "International.xlsx" and mapped using Tableau. Non-indigenous cultural terms were also captured by this web scrape (Irish, Scottish, European, etc.) and were also included in this map to reflect the multi-ethnic background of some of the contemporary artists, or the cross-cultural mixed-media nature of some of the works (a European textile ammended with indigenous North American beadwork, for example). These are not intended to speak to any kind of judgement about the "indigenous" nature of European ethnic groups, and simply reflect the available data. 
