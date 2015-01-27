#!/usr/bin/python
'''
	Interprets all the keywords
'''

from commands import *
from config import config
from selenium.webdriver.common.proxy import *

browser_list = []
config = config()

# Keyword List = [Open Browser, Open Browser With Proxy, Close Browser, Open URL]

def interpret(words):
	'''
		Interprets Keywords in a line

		@param: words - Keywords in a line
	'''

	for keyword in words:
		if (keyword == "Open Browser"):
			browser = open_browser()
			browser_list.append(browser)

		elif (keyword == "Open Browser With Proxy"):
			proxy = Proxy({'proxyType': ProxyType.MANUAL,
						   'httpProxy': config.proxy,
						   'ftpProxy': config.proxy,
						   'sslProxy': config.proxy,
						   'noProxy': '' # set this value as desired
						   })
			browser = open_browser_with_proxy(proxy)
			browser_list.append(browser)

		elif (keyword == "Close Browser"):
			if len(browser_list) > 0:
				close_browser(browser_list.pop())
			else:
				print keyword,": No Browser To be Closed"

		elif (keyword == "Maximize Window"):
			if len(browser_list) > 0:
				browser = browser_list[-1]
				maximize_window(browser)
			else:
				print keyword,": No Browser Opened"

		elif (keyword == "Open URL"):
			# URL entered in file should be of format "https://....." or "http://....."
			if len(browser_list) > 0:
				browser = browser_list[-1]
				index = words.index(keyword)
				if len(words) > index+1:
					url = words[index+1]
					words.pop(index+1)
					open_url(browser, url)
				else:
					close_browser(browser_list.pop())
					print keyword,": No Url Specified"
			else:
				print keyword,": No Browser Opened"

		else:
			if len(browser_list) > 0:
				close_browser(browser_list.pop())
			print "Keyword: ",keyword," Not Found"
