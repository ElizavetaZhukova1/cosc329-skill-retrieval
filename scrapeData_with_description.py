import requests
from requests import get
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from time import sleep
import csv
from random import randint 

postings = []
def get_description(jobLink):
    response = requests.get(jobLink)
    soup = BeautifulSoup(response.content, "html.parser")
    description=soup.find('div', 'jobsearch-jobDescriptionText')
    if description is None:
        return ''
    return description.text


def getPosts(pos, loc, province, page):
    url = (f'https://ca.indeed.com/jobs?q={pos}&l={loc}%2C+{province}&start={page}')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    all_posts = soup.find_all('div', class_='mosaic mosaic-provider-jobcards')
    if not all_posts:
        return
    posts = all_posts[0]
    posts = posts.find_all(class_='result')
    for item in posts:
        info = {
        #getting the title
        'title': item.find('h2').text,
        #getting the company
        'company': item.find('span', 'companyName').text,
        #getting the location
        'location': item.find('div', class_ = 'companyLocation').text,
        #getting the job description
        #'description': item.find('div', class_ = 'job-snippet').text,
        'description': get_description('https://www.indeed.com'+item.get('href')),
        #getting the post date
        'postDate': item.find('span', 'date').text,
        #the name of position
        'position': pos,
        }
        if info['description']: #If there's something in the description, add the job to the dataset
            postings.append(info)

for i in range(6, 11):
    getPosts('developer', 'Toronto', 'ON', i)
    time.sleep(1)
    getPosts('manager', 'Toronto', 'ON', i)
    time.sleep(1)

print(len(postings))
try:
    old_df=pd.read_csv('jobs.csv')
    new_df=pd.DataFrame(postings)
    final_df=old_df.append(new_df)
except pd.errors.EmptyDataError as err:
    final_df=pd.DataFrame(postings)

final_df.to_csv('jobs.csv')

'''
jobs = pd.DataFrame(postings)
jobs.to_csv('jobs.csv')
'''