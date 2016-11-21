#! /usr/bin/env python
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_URL ='https://movie.douban.com/nowplaying/shanghai/'

def download_page(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
    data = requests.get(url, headers=headers).content
    return data

def parse_html(html):
    soup = BeautifulSoup(html)
    
    movie_now = soup.find('div', attrs={'id': 'nowplaying'})
    movie_modbd = movie_now.find('div', attrs={'class': 'mod-bd'})
    movie_list_soup = movie_modbd.find('ul', attrs={'class': 'lists'})
    movie ={}
    movie_list = []    
    for movie_li in movie_list_soup.find_all('li',attrs={'class': 'list-item'}):
        try:
            
            movie_name = movie_li.find('a', attrs={'data-psource': 'title'}).getText().strip()            
            movie_score = movie_li.find('span', attrs={'class': 'subject-rate'}).getText()
            #movie_director = movie_li.li['data-director']
            #movie_actors = movie_li.li['data-actors']
            movie_url = movie_li.a['href']
            movie_picurl = movie_li.img['src']
            movie = {'movie_name':movie_name,'movie_score':movie_score,'movie_url':movie_url,'movie_picurl':movie_picurl}
            movie_list.append(movie)
        except:
            pass

    #return movie_list.sort(key = int(movie_list['movie_score']))
    return movie_list
   

def main():
    url = DOWNLOAD_URL
    html = download_page(url)
    list = parse_html(html)

            
if __name__== '__main__':
    main()