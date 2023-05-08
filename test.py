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
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.runAndWait()
    
    user = "Cương"
    
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
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
            print("Sorry, I didn't get that, I'd appreciate if you could try again ")
            speak("hãy nói lại để tôi rõ hơn ")
            query = "hãy nói lại"
        return query
    def robot():
        if __name__ == "__main__":

            if True:
                query = "hãy tìm kiếm người việt nam trên mạng"
                if "hãy tìm kiếm" in query and "trên mạng" in query:
                    try:
                        speak("tôi tìm được thứ này trên web")
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        query = query.replace("hãy tìm kiếm","")
                        query = query.replace("trên mạng","")
                        for url in search(query):
                            x=url
                            print(url)
                            break
                        webbrowser.get('chrome').open(x)
                        
                    except:
                        speak("Lỗi không xác định")    
    robot()

    while True:
        speak("Bạn có thêm câu hỏi gì với tôi không ? \n")

        query = take_user_cmd().lower()

        if query == "có" or query == "đúng vậy":
            speak("rất tốt, hãy hỏi tôi tiếp đi")
            robot()
        elif query == "không" or query == "không phải bây giờ" or query == "nâu" or query == "lâu":
            speak("cảm ơn vì đã sử dụng tôi")
            hour = datetime.datetime.now().hour
            if hour >= 22 and hour < 6:
                speak(f"chúc buổi tối tốt lành{user}")
            else:
                speak(f"chúc một ngày mới an lành{user}")
            break
        else:
            speak(print("Điều đó có lẽ vượt quá khả năng của tôi vào lúc này"))


main()