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

sub_urls = soup.find_all('a',{'target':'_blank','href':re.compile('/item/%.+')}) ##获取a标签，属性为target,href,并以列表形式返回

file = open('web_page.txt','w',encoding='utf-8')

for item in sub_urls[:10]:
   new_url = base_url+item['href']##获取item中的href的值
    web = urlopen(new_url).read().decode('utf-8')
    page = BeautifurlSoup(web,features='html.parser')
    content = page.find_all('div',{'class':'para','label-module':'para})
    for element in content:
        if len(element.get_text()) == 0:
            pass
        elif element.get_text() == r'\n':
             pass
         else:
              file.write(element.get_text())
 file.close()
                                  
                                   
    
