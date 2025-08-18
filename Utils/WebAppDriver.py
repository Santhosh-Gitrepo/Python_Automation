import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Utils.Logger import logger_setup
from datetime import datetime
import os


class WebAppDriver:
    def __init__(self, url):
        self.log = logger_setup()
        self.url = url
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option("detach", True)
        # options.add_argument("--headless")                # Headless mode
        # options.add_argument("--no-sandbox")              # Required in some CI
        # options.add_argument("--disable-dev-shm-usage")   # Avoid memory issues
        # options.add_argument("--disable-gpu")             # Safe for headless
        # options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)

    def launch(self):
        self.driver.get(self.url)
        self.log.info("Launched the Browser with Web App")

    def close(self):
        self.driver.quit()
        self.log.info("Closed the Web App with browser")

    def get_element_by_xpath(self, element):
        element = self.driver.find_element(By.XPATH, element)
        return element

    def get_element_by_id(self, element):
        element = self.driver.find_element(By.ID, element)
        return element

    def get_element_by_name(self, element):
        element = self.driver.find_element(By.NAME, element)
        return element

    def get_element_by_text(self, element):
        element = self.driver.find_element(By.LINK_TEXT, element)
        return element

    def get_element_by_class(self, element):
        element = self.driver.find_element(By.CLASS_NAME, element)
        return element

    def get_element_by_partial_text(self, element):
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, element)
        return element

    def get_element_by_css(self, element):
        element = self.driver.find_element(By.CSS_SELECTOR, element)
        return element

    def get_elements_by_xpath(self, element):
        element = self.driver.find_elements(By.XPATH, element)
        return element

    def get_elements_by_id(self, element):
        element = self.driver.find_elements(By.ID, element)
        return element

    def get_elements_by_name(self, element):
        element = self.driver.find_elements(By.NAME, element)
        return element

    def get_elements_by_text(self, element):
        element = self.driver.find_elements(By.LINK_TEXT, element)
        return element

    def get_elements_by_class(self, element):
        element = self.driver.find_elements(By.CLASS_NAME, element)
        return element

    def get_elements_by_partial_text(self, element):
        element = self.driver.find_elements(By.PARTIAL_LINK_TEXT, element)
        return element

    def get_elements_by_css(self, element):
        element = self.driver.find_element(By.CSS_SELECTOR, element)
        return element

    def get_screenshot(self):
        screen_dir = "screenshots"
        if not os.path.exists(screen_dir):
            os.makedirs(screen_dir)
        time.sleep(1)
        current_time = datetime.now().strftime("%H-%M-%S")
        self.driver.save_screenshot(f"{screen_dir}/{current_time}.png")
