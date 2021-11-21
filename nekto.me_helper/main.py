import speech_recognition as sr
import sys
from nektome import NektoMe
import time


def main():
    n = NektoMe()
    n.press_settings_buttons()
    r = sr.Recognizer()
    mic = sr.Microphone()
    while True:
        while True:
            with mic as audio_file:
                audio = r.listen(audio_file, phrase_time_limit=0.8)
            try:
                cmd = r.recognize_google(audio)
                print(cmd)
                if "stop" in cmd.lower():
                    n.press_end_button()
                    time.sleep(0.3)
                    n.press_end2_button()
                if "unit" in cmd.lower():
                    n.stop()
                    sys.exit("Program stop with code: 0")
            except sr.UnknownValueError:
                print("Silence")
            except sr.RequestError as e:
                print("Error")
            n.press_next_button()


if __name__ == '__main__':
    main()
