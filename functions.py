"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   _____                                                                     
  (        ___  .___  ,   . , __   ,   . , __   ,   .
   `--.  .'   ` /   \ |   | |'  `. |   | |'  `. |   |
      |  |      |   ' |   | |    | |   | |    | |   |
 \___.'   `._.' /     `._/| /    | `._/| /    | `._/|

build.........3
status........alpha
date..........20220607
author........23z86
language......DE/Python3
gitpage.......https://github.com/23z86/scrununu
description...Simple web scraper for kununu.com
..............kununu is a professionally operated employer rating platform
..............where employees can rate their employer anonymously
                                                                                
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import requests
from lxml import html
import os.path
import globals

print(f'{globals.count_reviews} entries expected...')


def output_file(i_file, i_xpath, i_option, i_url=globals.url, i_first_page=globals.first_page, i_last_page=globals.last_page, i_sort=globals.sort):

    if i_url[-1:] != "/":
        i_url = i_url + "/"

    file = open(i_file, "w")

    if i_option == 'file':
        print(f'Writing {i_file}, please wait...')

    for page in range(i_first_page, i_last_page):
        temp_url = i_url + str(page) + i_sort
        request = requests.get(temp_url)
        tree = html.fromstring(request.content)

        section = tree.xpath(i_xpath)

        for sections in section:
            if i_file == globals.file_date:
                sections = sections[:10]

            if i_option == 'cli':
                print(sections)

            file.write(sections + "\n")

    file.close()

    if os.stat(i_file).st_size == 0:
        os.remove(i_file)


def get_company(i_url, i_xpath):
    request = requests.get(i_url)
    tree = html.fromstring(request.content)

    return (tree.xpath(i_xpath)[0])


def merge_company_name(i_url, i_xpath_name, i_xpath_end):

    company_name = get_company(i_url=i_url, i_xpath=i_xpath_name)

    company_end = get_company(i_url=i_url, i_xpath=i_xpath_end)

    print(company_name, company_end)


def write_data(i_file, i_xpath):
    output_file(i_file=i_file,
                i_xpath=i_xpath,
                i_option=globals.option)


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

merge_company_name(globals.url, globals.company_name, globals.company_end) #- successfully tested
#rite_data(globals.file_title, globals.title) #- successfully tested
#write_data(globals.file_date, globals.datetime)
#write_data(globals.file_score, globals.score)
#write_data(globals.file_stars, globals.star)
#write_data(globals.file_recom, globals.recommended)
#write_data(globals.file_depmt, globals.department)
#check_file(globals.file_title, globals.reviews) #- successfully tested
