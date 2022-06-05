"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   _____                                                                .        
  (        ___  .___  ,   . , __   ,   . , __   ,   .      _   __      /|    ___ 
   `--.  .'   ` /   \ |   | |'  `. |   | |'  `. |   |      |   /        |   /   `
      |  |      |   ' |   | |    | |   | |    | |   |      `  /         |  |    |
 \___.'   `._.' /     `._/| /    | `._/| /    | `._/|       \/         _|_ `.__/|

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

def get_company():
    request = requests.get(globals.url)
    tree = html.fromstring(request.content)  
    
    print(tree.xpath(globals.company_name))
    
def get_title():
    file_title = open(globals.file_title, "w")
    
    for page in range(globals.first_page, globals.last_page):
        temp_url = globals.url + str(page) + globals.sort
        request = requests.get(temp_url)
        tree = html.fromstring(request.content)        
    
        title = tree.xpath(globals.title)
        
        for titles in title:                
            file_title.write(titles+"\n")    
    file_title.close()

def get_datetime():
    file_date = open("dates.txt", "w")
    
    for page in range(globals.first_page, globals.last_page):
        temp_url = globals.url + str(page) + globals.sort
        request = requests.get(temp_url)
        tree = html.fromstring(request.content)        
    
        datetime = tree.xpath(globals.datetime)
        
        for datetimes in datetime:
            if datetimes == "(aktualisiert)":
                datetimes = ""
                
            file_date.write(datetimes[:10]+"\n")    
    file_date.close()

def get_score():
    file_score = open("score.txt", "w")

    for page in range(globals.first_page, globals.last_page):
        temp_url = globals.url + str(page) + globals.sort
        request = requests.get(temp_url)
        tree = html.fromstring(request.content)
        
        score = tree.xpath(globals.score)
        
        for scores in score:
            file_score.write(scores+"\n")
    file_score.close()
            
def get_stars():
    file_stars = open("stars.txt", "w")
    
    for page in range(globals.first_page, globals.last_page):
        temp_url = globals.url + str(page) + globals.sort
        request = requests.get(temp_url)
        tree = html.fromstring(request.content)    
        
        star = tree.xpath(globals.star)
        
        for stars in star:
            if stars == "":
                stars = "No data"
            
            file_stars.write(stars+"\n")    

    file_stars.close()        
        

def get_recommendation():
    file_recom = open("recomms.txt", "w")
    
    for page in range(globals.first_page, globals.last_page):
        temp_url = globals.url + str(page) + globals.sort
        request = requests.get(temp_url)
        tree = html.fromstring(request.content)
        
        recommended = tree.xpath(globals.recommended)
        
        for recoms in recommended:
            if recoms == "":
                recoms = "No data"
            
            file_recom.write(recoms+"\n")    

    file_recom.close()

def check_reviews():
    
    if os.path.exists(globals.file_title):
        
        title_reviews = open(globals.file_title, "r")
        title_lines = title_reviews.readlines()
        line_counter = 0
        
        for lines in title_lines:
            line_counter += 1
        
        if any(line_counter for i in globals.reviews):
            
            print(f'OK - {line_counter} lines found in {title_reviews.name}')
        else:   
            print(f'Warning - {line_counter} lines found in {title_reviews.name}')
    else:
        print('File not found')
    
    
#get_company() #- successfully tested
#get_title() #- successfully tested
#get_datetime()
#get_score()
#get_stars()
#get_recommendation()
#check_reviews() - successfully tested