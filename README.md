# Google SSoC Web Scraper
This is a web scraper to collect the list of open-source organisations that participated in Google SSoC from 2016-2020 (2015 and older ones have a different website layout). This scraper was used before organisations for the current year are released, to check which organisations have been consistently participating in the past five years. If you want to know which organisations have been consistently participating in the past, and are interested in any of them, you can do research prior to release date, as they may participate again. 

### Step 1: Scrape organisation names by year.
`scrape.py` - scrapes organisations names from the website. To use, change '2020' in URL to desired year.

### Step 2: Output to 20xx.txt files by year.
### Step 3:
`ssoc_orgs.py` - takes the common organisations year on year and outputs consistently participating organisations from [start year] to [end year].

### Step 4: Out final list.
`ssoc_orgs_final.txt` - contains list of consistently participating organisations from 2016 to 2020.
