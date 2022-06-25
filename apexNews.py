from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

# make executable
app_path = os.path.dirname(sys.executable)
# format date time
now = datetime.now()
month_date_year = now.strftime("%b%d%Y")

## URL
url = "https://apexranked.com/news/"
xpath = '//div[@class="blog-text"]'

# headless-mode
options = Options()
options.headless = True

# Setup Selenium driver
path = "C:/chromedriver_win32/chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

# Grab Container
newsContainer = driver.find_elements(by="xpath", value='//div[@class="blog-text"]')

content = []

# Iterate through container and get title,description,link
for i in newsContainer:
    title = i.find_element(by="xpath", value='./h5/a').text
    desc = i.find_element(by="xpath", value='./p').text
    link = i.find_element(by="xpath", value='./a').get_attribute("href")
    output = {"title": title, "desc": desc, "link": link}
    content.append(output)

# Change to dataframe
df_news = pd.DataFrame(content)

# save to csv file
filename = f'apex_news{month_date_year}.csv'
save_path = os.path.join(app_path, filename)
df_news.to_csv(save_path)
driver.close()
driver.quit()
