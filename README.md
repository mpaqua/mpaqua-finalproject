# Megan Paqua - PCH Final Project

## Project Overview

This project uses Python to scrape the Denver Art Museum’s collection website (https://denverartmuseum.org/collection). For this project, I focused on the works of art in their “Native Arts” department, which contains archaeological and historic artifacts as well as contemporary artworks from indigenous cultures of North America and the South Pacific, as well as ethnic groups in Africa.
For this project, I used six modules:
1) Beautiful Soup
2) Requests
3) JSON
4) Re
5) Time
6) Randint

I’ve pulled out relevant information about each of these objects including: the title, the object number, the date the work was created, the culture associated with the work or the artist/artisan, the provenance dates, and any exhibition the work was featured in.  I used two functions to run two regular expressions, the first to identify the object number from the site URL, and the second to isolate the provenance dates rather than the whole descriptive text.
This information was all saved in the file data.json.
After this information was compiled, I used data.json to write a CSV file for use in my data visualizations. In this script (dataviz.py), I isolated the last year in the provenance list to identify the year that the work entered the museum. I then added the following information about each object: the object number, the title, and the culture. This information was saved in a file called dataviz.csv.

This file was used to create visualizations in Tableau Public to track:

   1) A timeline of acquisition activity - I was interested to see if the passing of NAGPRA in 1990 affected the museum’s rate of acquisitions of “Native Arts.”  Surprisingly, this was not the case, and there was an unexpected spike in acquisitions in 2003.
    
   2) Culture frequency - I wanted to see which cultures were most represented in the collection; however, due to some objects having several cultures associated with them — for a variety of reasons— it was not possible to directly graph that. This chart instead tracks the frequency with which each cultural group is referenced in the collections information.

After having so much difficulty representing the frequency of the cultures, I used data.json to write another CSV file. Using mapscv.py, I compiled a list of each of the cultural terms used in the collection. This list was intended to be used to create a map using the Native-Land.ca API.

In order to do this, the cultures needed to be written to a csv file to match the form used in their list of “Territory Slugs.” While it was possible to do this for some of the cultures programmatically, others needed to be compared by hand. This was due to different names being used for the same culture between the two resources as well as differing levels of specificity.  
  For example, the Denver Art Museum has a great deal of specificity in their cultural terms for various Pueblo peoples, while Native-Land.ca groups them all together as “Pueblo”; conversely, the Denver Art Museum often uses generic or outdated terms for Alaska native groups, while Native-Lands.ca is extremely specific.

  The completed list of relevant territory slugs, all instances of names being changed, as well as lingering questions or issues with the mapping were all recorded in a text file (native_land_notes.rtf). As Native-Land.ca does not currently support mapping for groups outside of the US and Canada, a secondary map was created in Tableau to map the groups from Mexico, Africa, and the South Pacific.
The list of territory slugs was then amended to the Native-Lands.ca mapping iframe (https://native-land.ca/api/embed/embed.html?maps=territories&name=)

The final Native-Land map, as well as the map showing the international groups can be found on the Tableau Public dashboard as well.

## Instructions for Use:

1) To run this yourself you’ll need to download the final.py script, and run it using Python3.

2) When it's finished running, you'll see a file labled data.json at the same level where you've saved the original python script.

3) Next, run the script dataviz.py. This script will create a CSV file titled “dataviz.csv” at the same level as the other files that has the object number, title, final provenance year, and associated culture for each object.

4) Next, run the script map.py. This will produce a csv file titled “map.csv” at the same level as the other files, which contains list of all of the cultures referenced in the Native Arts collections pages.

5) To use these cultures in the Native-Lands.ca interface, use the list of “territory slugs” found in the "native_land_notes.rtf" text file; this has a complete list of updated names, plus a record of any changes or issues encountered when comparing the two sources. Copy and paste the territory slugs into the Native-Land.ca url: https://native-land.ca/api/embed/embed.html?maps=territories&name=

6) If you would like to see the Tableau visualizations I made using dataviz.csv and map.csv, you can find them on Tableau Public dashboard (links below)

## Links

Github repository:https://github.com/mpaqua/mpaqua-finalproject

Tableau Dashboard: https://public.tableau.com/profile/megan6673#!/vizhome/ProgramforCulturalHeritageFinalProject/Maps

Denver Art Museum Collections Website:https://denverartmuseum.org/collection

Native-Land.ca API Endpoint:https://native-land.ca/api/index.html

Native-Land.ca Documentation: https://native-land.ca/api-docs/
