from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time
import string
import openpyxl
import os
import pandas as pd


#Loading Selenium Webdriver
path=r"C:\Users\ibenothme\Desktop\SeleniumScrap\chromedriver.exe"
driver= webdriver.Chrome(executable_path=path)
wait = WebDriverWait(driver, 5)

#generate CSV File
def import_entreprise(nom):
    df_Allianz=pd.read_csv(f'{nom}',sep=',')
    #df_Allianz=df_Allianz.drop('Unnamed: 0', 1)
    return df_Allianz
def concat_dans_une_liste(nom):
    df=import_entreprise(f'{nom}')
    Liste=[]
    Liste1=[]
    Liste2=[]
    for nom in df["nom de l'entreprise"]:
        Liste1.append(nom)
        for adress in df["adresse"]:
            Liste2.append(adress)
    Liste=Liste1+Liste2
    return Liste

Liste_allianz=concat_dans_une_liste("allianz")


#Opening Google maps
"""driver.get("https://www.google.com/maps")
time.sleep(3)
search=driver.find_element_by_name("q")
search.send_keys(" Allianz - Trevoux")
search.send_keys(Keys.RETURN)
time.sleep(5)
driver.find_element_by_class_name("DkEaL").click()
time.sleep(2)
review=driver.find_elements_by_class_name("MyEned")
for value in review:
        print(value.text)"""

#Finding the search box

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps")

# ticker symbols array
symbols =Liste_allianz
count = 1
for i in symbols[8:11]:
        driver.find_element_by_name("q").send_keys(i + Keys.RETURN)

        # elem.send_keys("spy")

        time.sleep(5)
        driver.find_element_by_class_name("DkEaL").click()
        time.sleep(2)
        review = driver.find_elements_by_class_name("MyEned")
        for value in review:
                print(value.text)
        driver.implicitly_wait(2)

        count = count + 1
        driver.back()