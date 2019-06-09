import scrapy
from bs4 import BeautifulSoup as bs
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import requests
import re

#Replace this
class spider(scrapy.Spider):
	def __init__(self):
		self.name = 'spider'
		self.allowed_domains = ['en.wikipedia.org']
		api_url = 'https://api.thewikigame.com/api/v1/group/22033570-e1fd-4a9f-9a96-9068082b88aa/current-round/'
		headers = {
		    'Authorization': 'Token 653dc5b73dbc2cb506cdb36d10d77b2d50ff4148' #Might need to change this
		}
		response = requests.get(api_url, headers=headers)
		start_index = response.text.index('"start_article"')
		start_index = response.text[start_index:].index('link') + start_index
		start_link = response.text[start_index+6:].split(',')[0]
		start_link = 'https://en.wikipedia.org/wiki/'+start_link.replace('"', '')
		end_index = response.text.index('"goal_article"')
		end_index = response.text[end_index:].index('link') + end_index
		end_link = response.text[end_index+6:].split(',')[0]
		self.end_link = 'https://en.wikipedia.org/wiki/'+end_link.replace('"', '')
		self.start_urls = [start_link]
		self.dont_overwrite = False
	def get_page_name(self, url):
		return url.replace('https://en.wikipedia.org/wiki/', '')
	def start_requests(self):
		url = self.start_urls[0]
		path = self.get_page_name(url)
		yield scrapy.Request(url=url,
							callback=self.parse, 
							meta={'path': path}, 
							errback=self.handle_failure)
	def handle_failure(self, failure):
		yield scrapy.Request(url=failure.request.url, 
							callback=self.parse, 
							meta={'path': failure.request.meta['path']},
							errback=self.handle_failure)
	def parse(self, response):
		soup = bs(response.text, 'html.parser')
		links = []
		for link in soup.findAll('a', attrs={'href': re.compile('^/wiki/')}):
		    path = link.get('href')[6:]
		    not_allowed = ['Special:', 'Wikipedia:', 'Portal:', 'Category:', 'File:', 'Template:', 'Template_talk:', 'Help:', 'Talk:']
		    allowed = True
		    for word in not_allowed:
		        if path.startswith(word):
		            allowed = False
		            break
		    if allowed and path != 'Main_Page':
		        links.append(path)
		links = list(set(links))
		links = ['https://en.wikipedia.org/wiki/'+l for l in links]
		for link in links:
			if self.get_page_name(link) in path:
				continue
			new_path = response.meta['path']+', '+self.get_page_name(link)
			if link == self.end_link and self.dont_overwrite == False:
				with open('path.txt', 'w') as outfile:
					outfile.write(new_path)
				raise scrapy.exceptions.CloseSpider('Path Found!')
				self.dont_overwrite = True
			yield scrapy.Request(url=link,
							callback=self.parse, 
							meta={'path': new_path}, 
							errback=self.handle_failure)

def find_best_path():
	process = CrawlerProcess(get_project_settings())
	process.crawl(spider)
	process.start()

find_best_path()