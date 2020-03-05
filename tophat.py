from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pynotifier import Notification
import time

true_url = input("Enter url: ").strip()
if true_url.find('://'):
    true_url = true_url[true_url.find('://') + 3 :]
if true_url.endswith('/'):
    true_url = true_url[:-1]


options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=/home/gmarks/.config/google-chrome-2/')

driver = webdriver.Chrome(options=options)
driver.get('https://' + true_url)

WebDriverWait(driver, 10000000).until(EC.url_contains(true_url))
print('on page')
while 1:
    WebDriverWait(driver, 10000000000).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'list-row--answered')]")))
    print('found')
    Notification(title='New question spotted!',
                 description=true_url,
                 duration=60,
                 urgency=Notification.URGENCY_CRITICAL).send()
    time.sleep(30)
                                        
