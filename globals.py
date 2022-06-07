import requests
import sys
from lxml import html
# +++++++++++++++++++++++++++++++++++++++++++++
# This file will be included into functions.py
# It contains global variables
# +++++++++++++++++++++++++++++++++++++++++++++

# MAIN URL
# e. g. https://www.kununu.com/de/COMPANY-NAME/kommentare/
url = 'https://www.kununu.com/de/pass-consulting-group/kommentare/'

if not url:
    sys.exit("Please initialize the URL variable!")

if not requests.get(url).status_code == 200:
    sys.exit(f'Page {url} not found, exiting...')

# FILES
file_title = "titles.txt"
file_date = "dates.txt"
file_score = "score.txt"
file_stars = "stars.txt"
file_recom = "recomms.txt"
file_depmt = "depart.txt"

# XPATH
reviews = '//div[@class="index__summaryLine__1Y3Gv"]/h2[@class="index__totalReviews__Fcmkx p-small-semibold"]//text()'
company_name = '//div[@class="index__nameStart__1-yIw"]//text()'
company_end = '//div[@class="index__nameEnd__DIV05"]//text()'
title = '//h3[@class="index__title__2uQec h3-semibold"]//text()'
datetime = '//span[@class="index__dateBlock__372Rm"]/time[@class="p-tiny-regular text-dark-63"]/@datetime'
score = '//div[@class="index__block__36tsj index__scoreBlock__138n3"]//text()'
star = '//div[@class="index__rating__3nC2L"]/div[@class="index__ratingBlock__lNDrc"]/div[@class="index__block__36tsj index__scoreBlock__138n3"]/span[@class="index__stars__2ads4 index__large__1Ez3-"]//@data-score'
recommended = '//span[@class="p-tiny-bold"]//text()'
department = '//span[@class="index__sentence__3PKUg text-dar-63 index__middot__3vlu3"]//text()'

# OTHERS
sort = '?sort=oldest'	# '?sort=newest', '?sort=best', '?sort=worst'
option = 'file'                 # 'cli', 'file'

# PAGE CALCULATOR
# Each page contains 10 entries
request = requests.get(url)
tree = html.fromstring(request.content)
section = tree.xpath(reviews)
from_list_to_str = section[0][:-13]
count_reviews = int(from_list_to_str)

est_last_page = (count_reviews / 10)
remainder = est_last_page % 1

first_page = 1
last_page = int(est_last_page + (1 - remainder) + 1)
