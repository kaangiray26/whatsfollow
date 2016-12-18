#!/usr/bin/python
#-*- encoding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
import os
driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
time.sleep(2)
while True:
  try:
    img = driver.find_element_by_class_name("cont-input-search")
  except NoSuchElementException:
    pass
  try:
    if img.is_displayed():
      break
  except NameError:
    pass
time.sleep(2)
isim=driver.find_element_by_css_selector(".input.input-search")
name=raw_input("Name:")
isim.send_keys(name)
time.sleep(5)
driver.find_element_by_css_selector(".emojitext.ellipsify").click()
time.sleep(2)
old=""
file=open("%s.txt" %(name.replace("_","")),"a")
file.write("%s\n" %(name))
print "\nStatus:"
print ""
os.system("printf '\e[8;6;26t'")
try:
  while True:
    try:
      status=driver.find_element_by_css_selector(".pane-header.pane-chat-header").find_element_by_css_selector(".chat-status.ellipsify").find_element_by_css_selector(".emojitext.ellipsify").get_attribute("title")
      if status != old:
        print status
        file.write("%s\n" %(status.encode('utf-8')))
        old=status
        os.popen("say Status Updated")
    except (NoSuchElementException,StaleElementReferenceException):
      pass
except KeyboardInterrupt:
  file.close()
  exit()
