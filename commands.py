#!/usr/bin/python
'''
	Defines commands for the keywords
    Uses Selenium
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui

def open_browser():
	'''
		Opens a firefox browser

		@return: variable for webdriver
	'''
	return webdriver.Firefox()

def open_browser_with_proxy(proxy):
	'''
		Opens a Firefox Browser behind a proxy

		@param: proxy - proxy details
		@return: variable for webdriver
	'''
	return webdriver.Firefox(proxy = proxy)

def close_browser(driver):
	'''
		Closes the opened browser

		@param: driver - variable for the opened browser (see "open_browser")
	'''
	driver.close()

def maximize_window(driver):
	'''
		Maximises the opened browser

		@param: driver - variable for the opened browser (see "open_browser")
	'''
	driver.maximize_window()

def open_url(driver, url):
	'''
		Opens a Webpage in the firefox browser

		@param: driver - variable for the opened browser (see "open_browser")
		@param: url - URL of the webpage
	'''
	driver.get(url)
