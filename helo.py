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
    import answer

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.runAndWait()
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Tôi là trợ lý của bạn")
    user = "Cương"
    # user = input("type your name: ")

    def greet_user():
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak(f"Chào buổi sáng thưa ngài {user}")
        elif hour >= 12 and hour < 17:
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
            print("..........Recognizing.........")
            query = r.recognize_google(audio, language='vi-en')
            print(f"User said: {query}\n")
        except Exception:
            query = "hãy nói lại"
        return query

    greet_user()

    def robot():
        if __name__ == "__main__":

            if True:
                query = take_user_cmd().lower()
                if query == "hãy nói lại":
                    robot()
                if "một ngày" in query and ("đẹp trời" in query or "tồi tệ" in query) and "để" not in query:
                    try:
                        if "đẹp trời" in query:
                            speak(answer.answer("đẹp trời"))
                        elif "tồi tệ" in query:
                            speak(answer.answer("tồi tệ"))
                        speak("bạn có muốn nói một thứ gì khác không")
                        robot()
                    except:
                        speak("Lỗi không xác định")
                elif "một ngày" in query and ("đẹp trời" in query or "tồi tệ" in query) and "để" in query:
                    speak(answer.check_weather(query))
                elif "đẹp trai" in query or "xấu trai" in query or "vẻ đẹp" in query: 
                    try:
                        if "đẹp trai" in query:
                            speak(answer.answer("đẹp trai"))
                        elif "xấu trai" in query:
                            speak(answer.answer("xấu trai"))
                        elif "vẻ đẹp" in query: 
                            speak(answer.answer("vẻ đẹp"))
                    except:
                        speak("Lỗi không xác định")    
                if "mở notepad" in query or "mở Wattpad" in query:
                    try:
                        speak("mở nốt bát")
                        subprocess.Popen(["notepad.exe"])
                    except:
                        speak("Lỗi không xác định")

                elif ("play" in query and "youtube" in query) or "mở youtube"in query:
                    try:
                        speak("bạn muốn mở gì ở youtube?")
                        req = take_user_cmd().lower()
                        kit.playonyt(req)
                    except:
                        speak("Lỗi không xác định")

                elif "hãy cho tôi biết" in query and "mấy giờ" in query and ("lúc này" in query or "bây giờ" in query or "núc này" in query or "núc lày" in query):
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
                        speak("mở trình soạn thảo văn bản ")
                        os.startfile(r'C:\Users\ADMIN\Desktop\Word 2016.lnk')
                    except:
                        speak("Lỗi không xác định")
                                
                elif "mở trình duyệt" in query:
                    try:
                        speak("mở trình duyệt chôm")
                        # os.startfile(r'C:\Users\Public\Desktop\Google Chrome.lnk')
                        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe")
                        
                    except:
                        speak("Lỗi không xác định")

                elif "mở thư điện tử" in query or "gửi thư cho" in query:
                    try:
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open('https://mail.google.com/mail/')
                    except:
                        speak("Lỗi không xác định")
                elif "mở zalo" in query:
                    try:
                        speak("mở zalo")
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
                        query = query.replace("hãy tìm kiếm","")
                        query = query.replace("trên mạng","")
                        for url in search(query):
                            x=url
                            print(url)
                            break
                        webbrowser.get('chrome').open(x)
                        
                    except:
                        speak("Lỗi không xác định")    
                        
                elif "không có gì để hỏi" in query or "để lúc khác" in query:
                    pass
                    
    
    speak("hãy nói gì đó")
    robot()

    while True:
        speak("Bạn có thêm câu hỏi gì với tôi không ? \n")

        query = take_user_cmd().lower()

        if query == "có" or query == "đúng vậy" or query =="tất nhiên":
            speak("rất tốt, hãy hỏi tôi tiếp đi")
            robot()
        elif query == "không" or query == "không phải bây giờ" or query == "nâu" or query == "lâu":
            speak("cảm ơn vì đã sử dụng tôi")
            hour = datetime.datetime.now().hour
            if hour >= 22 and hour < 6:
                speak(f"chúc buổi tối tốt lành")
            else:
                speak(f"chúc một ngày mới an lành ")
            break
        else:
            speak(print("Điều đó có lẽ vượt quá khả năng của tôi vào lúc này"))


main()