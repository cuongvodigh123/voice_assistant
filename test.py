def main(): 
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import pywhatkit as kit
    from AppOpener import run
    import time
    import requests
    import smtplib
    import wikipedia
    import googlesearch
    from googlesearch import search
    import subprocess
    import os
    import webbrowser
    import answer
    import sound
    from selenium import webdriver
    import subprocess
    wikipedia.set_lang("vi")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.runAndWait()
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def robot(query):
        if __name__ == "__main__":

            if True:      
                if "mở trình duyệt" in query:
                    try:
                        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe'
                        subprocess.Popen([chrome_path])
                    except:
                        speak("Lỗi 12")

    # robot(take_user_cmd().lower())
    robot("mở trình duyệt")
    
    while True:
        pass
main()