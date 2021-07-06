# one-piece-character-data-scraper
---
This project downloads the info for each of the individual canon characters of the Japanese manga series written and illustrated by Eiichiro Oda. [one piece](https://en.wikipedia.org/wiki/One_Piece) listed on https://onepiece.fandom.com/wiki/List_of_Canon_Characters. 

The downloaded info contains the following details of each individual if applies or is available:
- Japanese Name
- Romanized Name
- Official English Name
- Debut
- Affiliations
- Occupations
- Status
- Birthday
- Japanese VA
- Funi English VA
- Residence
- Epithet
- Age
- Height
- Blood Type
- Bounty
- Odex English VA
- 4Kids English VA
- Origin
- Alias
- Real name
- English Name
- Type
- Meaning
- Size
- Weight
- First Appearance.1
- Age at Death
- Zombie Number
- First appearance
- Region
- Gladiator Number
- Features
- Literal Meaning
- Captain
- Total Bounty
- CP9 key
- Affiliation
- Completion Date
- Affiliates

## Requirements
Python 3.8.10
Scrapy 2.5

## How to use
```
git clone git@github.com:JassonCordones/one-piece-chraracter-data-scraper.git
pip install pip install -r requirements.txt
scrapy crawl char_info -o data.json
```

