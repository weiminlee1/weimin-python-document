#--*--coding:utf-8--*--
#python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = 'https://baike.daidu.com'
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
url = base_url+his[-1]

html = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html, features='html.parser') ##把网页源代码存为tag标签形式

sub_urls = soup.find_all('a',{'target':'_blank','href':re.compile('/item
