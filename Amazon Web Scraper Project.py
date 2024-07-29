#!/usr/bin/env python
# coding: utf-8

# In[37]:


from bs4 import BeautifulSoup
import requests
import smtplib # sending emails
import time
import datetime
import csv
import pandas as pd


# In[27]:


URL = 'https://www.amazon.ca/Zak-Designs-Minecraft-Torch-Shaped-Resistant/dp/B07VVHZMJ4?th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

print(soup2)

title = soup2.find(id='productTitle').get_text()

print(title)

price = soup2.find(class_='aok-offscreen').get_text()

print(price)


# In[31]:


price = soup2.find(class_='aok-offscreen').get_text()
print(price)


# In[33]:


today = datetime.date.today()
print(today)


# In[45]:


header = ['Title', 'Price', 'Date']
data = [title.strip(), price.strip(), today]

#with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
#    writer = csv.writer(f)
#    writer.writerow(header)
#    writer.writerow(data)


# In[47]:


df = pd.read_csv(r'C:\Users\Javeria\AmazonWebScraperDataset.csv')
print(df)


# In[49]:


with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


def check_price():
    URL = 'https://www.amazon.ca/Zak-Designs-Minecraft-Torch-Shaped-Resistant/dp/B07VVHZMJ4?th=1'
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"} 
    
    page = requests.get(URL, headers=headers)
    
    soup1 = BeautifulSoup(page.content, "html.parser")
    
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    
    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(class_='aok-offscreen').get_text()
    today = datetime.date.today()
    
    header = ['Title', 'Price', 'Date']
    data = [title.strip(), price.strip(), today]
    
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    if(price < 20):
        send_mail()
 


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    #server.login('insert username','insert password') :D
    
    subject = "MINECRAFTWATERBOTTLEMINECRAFTWATERBOTTLE"
    body = "BUY THE TORCH."
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'javdev.xo@gmail.com',
        msg
    )


# In[ ]:




