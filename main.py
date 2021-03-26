from selenium import webdriver
from findfunctions import *
from helpfunctions import *
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("user-data-dir=speedtyper")
chrome_driver = "chromedriver"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

gtw(driver,"https://www.livechat.com/typing-speed-test/")
print(driver.title)
typer = fbi(driver, "test-input")

def getwordlist():
    return fbtns(fbxp(driver, '//*[@id="app"]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]'),"span")

def printwordlist(wordlist):
    for word in wordlist:
        print(gih(word))

def typeword(word,input):
    input.send_keys(word + " ")

while True:
    wordlist = getwordlist()
    str_wordlist = []
    for word in wordlist:
        str_wordlist.append(gih(word))
    for word in str_wordlist:
        typeword(word,typer)