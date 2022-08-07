# So today, we are building the internet bot with Selenium that will click on cookies without us doing anything.
# The bot will click on a cookie for 5 minutes and than automatically choose the product from the store.
#
# We will need to install the webdriver for this and import the Selenium.
# Also, we will need the time module
# In my case I will need to download [chrome webdriver](https://chromedriver.chromium.org/downloads)
# and save it into the folder of my choice now import all the modules that I will need
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Now we will have to save the pass to the webdriver that
# I just downloaded into variable and connect to the web service of my choice:
chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
# Now we have access to the html elements of the web service I chose.
# First, we save the cookie that I need to click into a variable:
cookie = driver.find_element(By.ID, "cookie")

# Also, we will need to save the beginning of those five minutes and the start of the time into a variable.
# The `time()` method is a method of `time` module and its used to get the time in seconds since the when
# the timestarts in a browser. It will basically take the time from the moment we called the method.
timeout = 300   # 5 minutes from now
timeout_start = time.time()

# now to click the cookie endlessly untill the five minutes are over we will use the while loop
while True:
    cookie.click()
    delta = time.time() - timeout_start
    if delta >= timeout:
        break

# now in our webpage we will find all the rewards that are available and save them into the list.
# Also, we will need to save the amount of cash that we have into variable to use it for later:
store_list = [store_item for store_item in driver.find_elements(By.CSS_SELECTOR, "#store div[class='']")]
cash = float(driver.find_element(By.ID, "money").text.replace(",","").strip(" "))

# Now we will iterate through our list of rewards to extract the prices to check if we earned anything.
# If we earned something than we will choose the biggest available reward and click on it
for store_item in store_list:
    price = float(store_item.find_element(By.CSS_SELECTOR, "b").text.split(' ')[-1].replace(",","").strip(" "))
    if cash >= price:
        store_list[-1].click()

