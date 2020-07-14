from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://liveupdates.hindustantimes.com/india/coronavirus-india-world-latest-news-covid-19-death-toll-july-8-2020-21594171380795.html")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[:10] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news})
