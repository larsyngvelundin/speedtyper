#from findfunctions import *
from time import sleep

def sl(x): #Sleep with console log
    print("Sleeping " + str(x) + " seconds...")
    sleep(x)

def gih(e): #Get inner HTML
    return e.get_attribute("innerHTML")

def ghref(e): #Get href from element
    return e.get_attribute('href')

def c(e): #Click
    e.click()

def cj(e,d):
    d.execute_script("arguments[0].click();", e)

def cutstart(s,n): #Cuts n amount of characters from string
    return s[n:]

def cutend(s,n): #Cuts end of string n = characters from end
    end = len(s) - n
    return s[0:end]
  
def cutendpos(s,n): #Cuts end of a string n = characters from start
	return s[0:n] 

def gtw(d,s): #Go to website
    d.get(s)