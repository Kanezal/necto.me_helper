from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import warnings
from selenium.webdriver.chrome.options import Options



class NektoMe:
    def __init__(self):
        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 0,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome("chromedriver.exe", options=opt)
        self.driver.get("https://nekto.me/audiochat#/")

    def press_button_search(self):
        button = self.driver.find_element_by_id("searchCompanyBtn")
        button.click()

    def press_end_button(self):
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div/div[2]/button[1]").click()
            time.sleep(0.3)
            self.driver.find_element_by_xpath("/html/body/div[6]/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print("Program: you are not in dialogue")

    def press_next_button(self):
        try:
            button = self.driver.find_element_by_class_name("btn.btn-lg.go-scan-button")
            button.click()
        except NoSuchElementException:
            pass

    def press_settings_buttons(self):
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div[1]/div[4]/div[2]/div/button").click()
            self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div[1]/div[2]/div[1]/div/button[2]").click()
            self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div[1]/div[2]/div[2]/div/button[3]").click()
            self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div[1]/div[3]/div[1]/div[1]/button[2]").click()
            self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div[1]/div[3]/div[2]/div[1]/button[2]").click()
        except NoSuchElementException:
            warnings.warn("WARNING: BUTTON IS MISSING")

    def stop(self):
        self.driver.close()
        self.driver.quit()

    def captcha_passer(self):
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[3]/section/div[2]/div/div/iframe")
        except NoSuchElementException:
            print("Program: no captcha found")
