# -*- coding: utf-8 -*-
"""03182024.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kO-6lNiHltnurF1_eFKv2Ke-qYRvSwpS
"""

import requests
from bs4 import BeautifulSoup
url = "https://www.microsoft.com/en-us/"
response = requests.get(url)
if response.status_code == 200:
  soup = BeautifulSoup(response.text, 'html.parser')
  page_title = soup.title.text.strip()
  print(f"Page Title: {page_title}")
else:
  print("Failed to retrieve the webpage")

import requests
from bs4 import BeautifulSoup
url = "https://www.microsoft.com/en-us/"
response = requests.get(url)
if response.status_code == 200:
  soup = BeautifulSoup(response.text, 'html.parser')
  for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.startswith('http'):
      print(href)
else:
  print("Failed to retrieve the webpage")

