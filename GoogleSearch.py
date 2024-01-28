from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class elementLocatorsByXPATH():
    def locat_by_XPATH(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.google.com/")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys("DevOps")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
        time.sleep(200)
findbyid = elementLocatorsByXPATH()
findbyid.locat_by_XPATH()