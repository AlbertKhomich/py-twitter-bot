from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os
import speed_test

SPEED_UP = 150
SPEED_DOWN = 10
LOGIN_TW = 'Ohgfgkhgfgh7894'
PASSWORD_TW = os.environ['PASSWORD_TW']

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

bot = speed_test.TwitterBot(driver, SPEED_DOWN, SPEED_UP, PASSWORD_TW, LOGIN_TW)

speed = bot.check_speed()
bot.tweet(speed[0], speed[1])
