from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class NektoMe:
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://nekto.me/audiochat#/")

    def press_button_search(self):
        button = self.driver.find_element_by_id("searchCompanyBtn")
        button.click()

    def press_end_button(self):
        button = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div/div[2]/button[1]")
        button.click()

    def press_end2_button(self):
        button = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[3]/button[2]")
        button.click()

    def press_next_button(self):
        try:
            button = self.driver.find_element_by_class_name("btn.btn-lg.go-scan-button")
            button.click()
        except NoSuchElementException:
            print("Not found next button")

    def press_settings_buttons(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div[1]/div[4]/div[2]/div/button").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div[1]/div[2]/div[1]/div/button[2]").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div[1]/div[2]/div[2]/div/button[3]").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div[1]/div[3]/div[1]/div[1]/button[2]").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div[1]/div[3]/div[2]/div[1]/button[2]").click()

    def stop(self):
        self.driver.close()
        self.driver.quit()
