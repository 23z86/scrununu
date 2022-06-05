"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   _____                                                                     
  (        ___  .___  ,   . , __   ,   . , __   ,   .
   `--.  .'   ` /   \ |   | |'  `. |   | |'  `. |   |
      |  |      |   ' |   | |    | |   | |    | |   |
 \___.'   `._.' /     `._/| /    | `._/| /    | `._/|

build.........2
status........alpha
date..........20220605
author........23z86
language......DE/Python3
gitpage.......https://github.com/23z86/scrununu
description...Simple web scraper for kununu.com
..............kununu is a professionally operated employer rating platform
..............where employees can rate their employer anonymously
                                                                                
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import requests
from lxml import html
import os.path
import globals

def output_file(i_file, i_url, i_xpath, i_first_page, i_last_page, i_sort):
    file = open(i_file, "w")
    
    print(f'Writing {i_file}, please wait...')
    
    for page in range(i_first_page, i_last_page):
        temp_url = i_url + str(page) + i_sort
        request = requests.get(temp_url)
        tree = html.fromstring(request.content)        
    
        section = tree.xpath(i_xpath)
        
        for sections in section:
            file.write(sections+"\n")  

    file.close()    

def get_company(i_url, i_xpath):
    request = requests.get(i_url)
    tree = html.fromstring(request.content)  
    
    print(tree.xpath(i_xpath))
    
def write_data(i_file, i_url, i_xpath, i_first_page, i_last_page, i_sort):
    output_file(i_file=i_file,
                i_url=i_url,
                i_xpath=i_xpath,
                i_first_page=i_first_page,
                i_last_page=i_last_page,
                i_sort=i_sort)

def check_file(i_file, i_review):
    
    if os.path.exists(i_file):
        
        title_reviews = open(i_file, "r")
        title_lines = title_reviews.readlines()
        line_counter = 0
        
        for lines in title_lines:
            line_counter += 1
        
        if any(line_counter for i in i_review):
            
            print(f'OK - {line_counter} lines found in {title_reviews.name}')
        else:   
            print(f'Warning - {line_counter} lines found in {title_reviews.name}')
    else:
        print('File not found')
    
    
#get_company(globals.url, globals.company_name) #- successfully tested
write_data(globals.file_title, globals.url, globals.title, globals.first_page, globals.last_page, globals.sort) #- successfully tested
#write_data(globals.file_date, globals.url, globals.datetime, globals.first_page, globals.last_page, globals.sort)
#write_data(globals.file_score, globals.url, globals.score, globals.first_page, globals.last_page, globals.sort)
#write_data(globals.file_stars, globals.url, globals.star, globals.first_page, globals.last_page, globals.sort)
#write_data(globals.file_recom, globals.url, globals.recommended, globals.first_page, globals.last_page, globals.sort)
check_file(globals.file_title, globals.reviews) #- successfully tested