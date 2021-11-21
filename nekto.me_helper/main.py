import time
import speech_recognition as sr
import sys
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


n = NektoMe()
n.press_settings_buttons()
input("""
You need to confirm the microphone and pass 3 captcha after users skip you

Press enter when you ready:""")
r = sr.Recognizer()
mic = sr.Microphone()
while True:
    while True:
        with mic as audio_file:
            audio = r.listen(audio_file, phrase_time_limit=1.5)
        try:
            cmd = r.recognize_google(audio)
            print(cmd)
            if "stop" in cmd.lower():
                n.press_end_button()
                time.sleep(0.3)
                n.press_end2_button()
            if "unit" in cmd.lower():
                sys.exit("Program stop with code: 0")
        except sr.UnknownValueError:
            print("Miss")
        except sr.RequestError as e:
            print("Error")
        n.press_next_button()
