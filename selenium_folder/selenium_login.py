from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from utils.pipelines import *
import json 

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--top-most")
options.add_argument("--incognito")

def selenium_login(username:str, password:str, id_selenium: int):
        s=SeleniumPipeline()
        items=s.get_item_by_own_id(id_selenium)
        url= items[2]
        driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        driver.maximize_window()
        by = {"NAME": By.NAME, "ID": By.ID, "CSS_SELECTOR": By.CSS_SELECTOR, "CLASS_NAME": By.CLASS_NAME}
        driver.find_element(by[json.loads(items[3])[0]],json.loads(items[3])[1]).send_keys(username)
        driver.find_element(by[json.loads(items[4])[0]],json.loads(items[4])[1]).send_keys(password)
        driver.find_element(by[json.loads(items[5])[0]],json.loads(items[5])[1]).click()
        return