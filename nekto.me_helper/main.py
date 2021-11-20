import pyautogui
import speech_recognition as sr
import sys


def next_button():
    button_position = pyautogui.locateCenterOnScreen("Button_next.png")
    if button_position is not None:
        save_position = pyautogui.position()
        pyautogui.click("Button_next.png")
        pyautogui.moveTo(save_position)


r = sr.Recognizer()
mic = sr.Microphone()
while True:
    next_button()
    with mic as audio_file:
        audio = r.listen(audio_file, phrase_time_limit=1.5)
    try:
        cmd = r.recognize_google(audio)
        print(cmd)
        if "stop" in cmd.lower():
            saved_position = pyautogui.position()
            pyautogui.click("Button_end.png")
            pyautogui.sleep(0.15)
            pyautogui.click("Button_end_2.png")
            pyautogui.moveTo(saved_position)
        if "unit" in cmd.lower():
            sys.exit("Program stop with code: 0")
    except sr.UnknownValueError:
        print("Miss")
    except sr.RequestError as e:
        print("Error")
    next_button()
