from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pynotifier import Notification
import time

LONG_WAIT = 10**12

def get_driver(data_dir):
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=' + data_dir)
    return webdriver.Chrome(options=options)

def load_noredirect(driver, url):
    driver.get('https://' + true_url)
    WebDriverWait(driver, LONG_WAIT).until(EC.url_contains(true_url))

if __name__ == '__main__':
    true_url = input("Enter url: ").strip()
    if true_url.find('://'):
        true_url = true_url[true_url.find('://') + 3 :]
    if true_url.endswith('/'):
        true_url = true_url[:-1]

    driver = get_driver('/home/gmarks/.config/google-chrome-2/')
    load_noredirect(driver, true_url)
    print('page loaded')
    
    while 1:
        WebDriverWait(driver, LONG_WAIT).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'list-row--answered')]")))
        print('new q found')
        Notification(title='New question spotted!',
                     description=true_url,
                     duration=60,
                     urgency=Notification.URGENCY_CRITICAL).send()
        time.sleep(30)
                                        
