import speech_recognition as sr
import sys
from nektome import NektoMe


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
                cmd = r.recognize_google(audio).lower()
                print("Command: " + cmd)
                if "stop" in cmd:
                    n.press_end_button()
                if "finish" in cmd:
                    n.stop()
                    sys.exit("Program stop with code: 0")
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Program: error")
            n.press_next_button()
            # n.captcha_passer()


if __name__ == '__main__':
    main()
