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
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Tôi là chatbot")
    user = "Cương"
    # user = input("type your name: ")

    def greet_user():
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak(f"Chào buổi sáng thưa ngài {user}")
        elif hour > 12 and hour < 17:
            speak(f"chào buổi chiều thưa ngài {user}")
        else:
            speak(f"chào buổi tối thưa ngài {user}")

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

                if "một ngày" in query and ("đẹp trời" in query or "tồi tệ" in query):
                    try:
                        speak("Tôi chỉ là 1 công cụ máy tính, tôi không thể biết được hôm nay như thế nào")
                        speak("bạn có muốn nói một thứ gì khác không")
                        robot()
                    except:
                        speak("Lỗi không xác định")
                if "mở notepad" in query:
                    try:
                        speak("mở nốt bát")
                        subprocess.Popen(["notepad.exe"])
                    except:
                        speak("Lỗi không xác định")

                elif "play on youtube" in query:
                    try:
                        speak("bạn muốn mở gì ở youtube?")
                        req = take_user_cmd().lower()
                        kit.playonyt(req)
                    except:
                        speak("Lỗi không xác định")

                elif "thời gian" in query:
                    try:
                        speak(datetime.date.today())
                        speak(time.strftime("%H:%M:%S", time.localtime()))
                    except:
                        speak("Lỗi không xác định")

                elif "mở thư mục" in query:
                    try:
                        speak("mở thư mục")
                        os.startfile('explorer.exe')
                    except:
                        speak("Lỗi không xác định")

                elif "mở máy tính" in query:
                    try:
                        speak("đang mở máy tính")
                        os.startfile('calc.exe')
                    except:
                        speak("Lỗi không xác định")

                elif "mở cài đặt" in query:
                    try:
                        speak("đang mở cài đặt")
                        os.system("start ms-settings:")
                    except:
                        speak("Lỗi không xác định")
                elif "mở văn bản" in query:
                    try:
                        speak("opening word")
                        os.startfile(r'C:\Users\ADMIN\Desktop\Word 2016.lnk')
                    except:
                        speak("Lỗi không xác định")
                                
                elif "mở trình duyệt" in query:
                    try:
                        speak("opening chrome")
                        # os.startfile(r'C:\Users\Public\Desktop\Google Chrome.lnk')
                        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe")
                        
                    except:
                        speak("Lỗi không xác định")

                elif "mở thư điện tử" in query:
                    try:
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open('https://mail.google.com/mail/')
                    except:
                        speak("Lỗi không xác định")
                elif "mở zalo" in query:
                    try:
                        
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open('https://chat.zalo.me/')
                    except:
                        speak("Lỗi không xác định")
                
                elif "mở facebook" in query:
                    try:
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open('https://www.facebook.com/')
                    except:
                        speak("Lỗi không xác định")
                
                elif "hãy tìm kiếm" in query and "trên mạng" in query:
                    try:
                        speak("tôi tìm được thứ này trên web")
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        url = search(query)[0]
                        for url in search(query):
                            print(url)
                        webbrowser.get('chrome').open(url)
                        
                    except:
                        speak("Lỗi không xác định")    
                        
                else:
                    pass

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