# +++++++++++++++++++++++++++++++++++++++++++++
# This file will be included into functions.py
# It contains global variables
# +++++++++++++++++++++++++++++++++++++++++++++

# MAIN URL
# e. g. https://www.kununu.com/de/COMPANY-NAME/kommentare/
url = 'https://www.kununu.com/de/wuerth-industrie-service/kommentare/'

# FILES
file_title = "titles.txt"
file_date  = "dates.txt"
file_score = "score.txt"
file_stars = "stars.txt"
file_recom = "recomms.txt"

# XPATH
reviews		= '//div[@class="index__summaryLine__1Y3Gv"]/h2[@class="index__totalReviews__Fcmkx p-small-semibold"]//text()'
company_name	= '//div[@class="index__nameStart__1-yIw"]//text()'
title		= '//h3[@class="index__title__2uQec h3-semibold"]//text()'
datetime	= '//span[@class="index__dateBlock__372Rm"]/time[@class="p-tiny-regular text-dark-63"]/@datetime'
score		= '//div[@class="index__block__36tsj index__scoreBlock__138n3"]//text()'
star		= '//div[@class="index__rating__3nC2L"]/div[@class="index__ratingBlock__lNDrc"]/div[@class="index__block__36tsj index__scoreBlock__138n3"]/span[@class="index__stars__2ads4 index__large__1Ez3-"]//@data-score'
recommended	= '//span[@class="p-tiny-bold"]//text()'      

# OTHERS
sort		= '?sort=oldest'	# '?sort=newest'; '?sort=best', '?sort=worst'
first_page	= 1
last_page       = 40

# PAGE CALCULATOR
# Each page contains 10 entries
#est_last_page = int((reviews / 10))
#remainder = est_last_page % 1

# PAGES
#pages = est_last_page + (1 - remainder) + 1 
