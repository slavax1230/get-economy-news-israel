from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")

CHROME_DRIVER_PATH = "/app/chromedriver"
# SERVICE = Service(CHROME_DRIVER_PATH)
DRIVER = webdriver.Chrome(options=options)

class Getinfo:
    def close(self):
        DRIVER.get("https://www.ynet.co.il/economy/category/429")
        mivzak = DRIVER.find_elements(By.CLASS_NAME, "slotSubTitle")
        
        # Open a text file to write the output
        with open('output.txt', 'w', encoding='utf-8') as file:
            for i in mivzak:
                file.write("-")
                file.write("\n" + i.text + "\n")
info = Getinfo()
info.close()

# Make sure to close the driver after the operation is completed
DRIVER.quit()
