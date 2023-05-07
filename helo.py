def main():  # I know main function isn't required in py
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


    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.runAndWait()

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Tôi là chatbot")
    user = "adam"
    # user = input("type your name: ")

    def greet_user():
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak(f"GOOD MORNING {user}")
        elif hour > 12 and hour < 17:
            speak(f"GOOD AFTERNOON {user}")
        else:
            speak(f"GOOD EVENING {user}")

    def take_user_cmd():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("..........LISTENING...........")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print(".......Recognizing........")
            query = r.recognize_google(audio, language='vi-en')
            print(f"User said: {query}\n")
        except Exception:
            print("Sorry, I didn't get that, I'd appreciate if you could try again  ")
            query = "NONE"
        return query

    greet_user()

    def robot():
        if __name__ == "__main__":

            if True:
                query = take_user_cmd().lower()

                if "mở notepad" in query:
                    try:
                        speak("opening notepad")
                        subprocess.Popen(["notepad.exe"])
                    except:
                        speak("Unknown error occurred")

                elif "play on youtube" in query:
                    try:
                        speak("What do you want to play on youtube?")
                        req = take_user_cmd().lower()
                        kit.playonyt(req)
                    except:
                        speak("Unknown error occurred")

                elif "thời gian" in query:
                    try:
                        speak(datetime.date.today())
                        speak(time.strftime("%H:%M:%S", time.localtime()))
                    except:
                        speak("Unknown error occurred")

                elif "mở thư mục" in query:
                    try:
                        speak("opening file explorer")
                        os.startfile('explorer.exe')
                    except:
                        speak("Unknown error occurred")

                elif "mở máy tính" in query:
                    try:
                        speak("opening calculater")
                        os.startfile('calc.exe')
                    except:
                        speak("Unknown error occurred")

                elif "mở cài đặt" in query:
                    try:
                        speak("opening settings")
                        os.system("start ms-settings:")
                    except:
                        speak("Unknown error occurred")
                elif "mở văn bản" in query:
                    try:
                        speak("opening word")
                        os.startfile(r'C:\Users\ADMIN\Desktop\Word 2016.lnk')
                    except:
                        speak("Unknown error occurred")
                                
                elif "mở trình duyệt" in query:
                    try:
                        speak("opening chrome")
                        # os.startfile(r'C:\Users\Public\Desktop\Google Chrome.lnk')
                        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe")
                        
                    except:
                        speak("Unknown error occurred")

                elif "mở thư điện tử" in query:
                    try:
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open('https://mail.google.com/mail/')
                    except:
                        speak("Unknown error occurred")
                elif "mở zalo" in query:
                    try:
                        
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open('https://chat.zalo.me/')
                    except:
                        speak("Unknown error occurred")
                
                else:
                        speak("I found this on the web")
                        for url in search(query):
                            print(url)

    robot()

    while True:
        speak("Would you like to run this tool again? \n")

        query = take_user_cmd().lower()

        if query == "có" or query == "đúng vậy":
            speak("very well, say again what you want me to do")
            robot()
        elif query == "không" or query == "không phải bây giờ" :
            speak("Cool thanks for using the programme")
            hour = datetime.datetime.now().hour
            if hour >= 22 and hour < 6:
                speak(f"Good NIGHT{user}")
            else:
                speak(f"have a good day{user}")
            break
        else:
            speak(print("That maybe beyond my abilities at the moment"))


main()