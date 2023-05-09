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
            
    greet_user()        
    speak("Tôi là trợ lý âm thanh của bạn")
    
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

    def robot(query):
        if __name__ == "__main__":

            if True:
                ok=0
                print("query = ",query)
                if query == "hãy nói lại":
                    robot(take_user_cmd())
                if "một ngày" in query and ("đẹp trời" in query or "tồi tệ" in query) and "để" not in query:
                    try:
                        if "đẹp trời" in query:
                            speak(answer.answer("đẹp trời",1))
                        elif "tồi tệ" in query:
                            speak(answer.answer("tồi tệ",2))
                        speak("bạn có muốn nói một thứ gì khác không")
                        robot("hãy nói lại")
                    except:
                        speak("Lỗi 1")
                elif "một ngày" in query and ("đẹp trời" in query or "tồi tệ" in query) and "để" in query:
                    try:
                        if "đẹp trời" in query:
                            speak(answer.answer("đẹp trời",1))
                        elif "tồi tệ" in query:
                            speak(answer.answer("tồi tệ",2))
                    except:
                        speak("Lỗi 2")
                elif "đẹp trai" in query or "xấu trai" in query or "vẻ đẹp" in query: 
                    try:
                        if "đẹp trai" in query:
                            speak(answer.answer("đẹp trai",1))
                        elif "xấu trai" in query:
                            speak(answer.answer("xấu trai",2))
                        elif "vẻ đẹp" in query: 
                            speak(answer.answer("vẻ đẹp",1))
                    except:
                        speak("Lỗi 3")  
                elif "sức khoẻ tốt" in query:
                    try:
                        speak(answer.answer("sức khoẻ tốt",3))
                    except:
                        speak("Lỗi 4")  
                elif "bạn tên là gì" in query:
                    try:
                        speak(answer.answer("bạn tên là gì",1))
                    except:
                        speak("Lỗi 4")  
                elif "ăn cơm chưa" in query:
                    try:
                        speak(answer.answer("ăn cơm chưa",1))
                    except:
                        speak("Lỗi 4")  
                elif ("tìm kiếm" in query or "tìm" in query) and "trên mạng" in query:
                    try:
                        speak(answer.answer("tìm kiếm thông tin trên mạng",1))
                        query=take_user_cmd().lower()
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        for url in search(query):
                            x=url
                            print(url)
                            break
                        webbrowser.get('chrome').open(x)
                    except:
                        speak("Lỗi 6") 
                elif "muốn tìm hiểu" in query and "công ty công nghệ" in query:
                    try:
                        speak(answer.answer("công ty công nghệ",1))
                    except:
                        speak("Lỗi 6")
                elif "hãy định nghĩa" in query:
                    try:
                        speak("đang định nghĩa")
                        query = query.replace("hãy định nghĩa","")
                        data=wikipedia.summary(query).split(".")
                        speak(data[0])
                        data.pop(0)
                        while True:
                            if len(data)==0:
                                speak("xin cảm ơn đã lắng nghe")
                                break
                            speak("Bạn muốn nghe tiếp không")
                            a=take_user_cmd().lower()
                            # a=input()
                            if a=="không" or a=="tôi không muốn" or a=="đủ rồi" or len(data)==0 or "dừng lại" == a:
                                speak("xin cảm ơn đã lắng nghe")
                                break
                            else:
                                if len(data)>1:
                                    speak(data[0])
                                    data.pop(0)
                                    speak(data[0])
                                    data.pop(0)
                                else:
                                    speak(data[0])
                                    data.pop(0)
                    except:
                        speak("Lỗi định nghĩa")
                else:
                    ok+=1          
                #second 
                if "mở notepad" in query or "mở wattpad" in query:
                    try:
                        speak("mở nốt bát")
                        subprocess.Popen(["notepad.exe"])
                    except:
                        speak("Lỗi 5")

                elif ("play" in query and "youtube" in query) or "mở youtube"in query:
                    try:
                        speak("bạn muốn mở gì ở youtube?")
                        req = take_user_cmd().lower()
                        kit.playonyt(req)
                    except:
                        speak("Lỗi 6")
                elif ("nghe" in query or "mở" in query) and "nhạc mario" in query:
                    sound.nhacmario()
                elif "hãy cho tôi biết" in query and "mấy giờ" in query and ("lúc này" in query or "bây giờ" in query or "núc này" in query or "núc lày" in query):
                    try:
                        speak(datetime.date.today())
                        speak(time.strftime("%H:%M:%S", time.localtime()))
                    except:
                        speak("Lỗi 7")

                elif "mở thư mục" in query:
                    try:
                        speak("mở thư mục")
                        os.startfile('explorer.exe')
                    except:
                        speak("Lỗi 8")

                elif "mở máy tính" in query:
                    try:
                        speak("đang mở máy tính")
                        os.startfile('calc.exe')
                    except:
                        speak("Lỗi 9")

                elif "mở cài đặt" in query:
                    try:
                        speak("đang mở cài đặt")
                        os.system("start ms-settings:")
                    except:
                        speak("Lỗi 10")
                elif "mở văn bản" in query:
                    try:
                        speak("mở trình soạn thảo văn bản ")
                        os.startfile(r'C:\Users\ADMIN\Desktop\Word 2016.lnk')
                    except:
                        speak("Lỗi 11")
                                
                elif "mở trình duyệt" in query:
                    try:
                        speak("mở trình duyệt chôm")
                        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe")
                        
                    except:
                        speak("Lỗi 12")

                elif "mở thư điện tử" in query or "gửi thư cho" in query:
                    try:
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open('https://mail.google.com/mail/')
                    except:
                        speak("Lỗi 13")
                elif "mở zalo" in query:
                    try:
                        speak("mở zalo")
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open('https://chat.zalo.me/')
                    except:
                        speak("Lỗi 14")
                
                elif "mở facebook" in query:
                    try:
                        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open('https://www.facebook.com/')
                    except:
                        speak("Lỗi 15")
                
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
                        speak("Lỗi 16")    
                        
                else:
                    ok+=1
                if ok>=2:
                    speak("tôi không hiểu hoặc không thể giúp bạn, hãy hỏi một câu khác dễ hơn với tôi")    
    
    speak("hãy nói gì đó để tôi có thể giúp bạn")
    robot(take_user_cmd().lower())
    # robot("hãy định nghĩa người  việt nam")
    while True:
        speak("Bạn có thêm câu hỏi gì với tôi không ? \n")

        query = take_user_cmd().lower()
        if query == "không" or query == "không phải bây giờ" or query == "hâm" or query=="âm":
            speak("cảm ơn vì đã sử dụng tôi")
            hour = datetime.datetime.now().hour
            if hour >= 22 and hour < 6:
                speak(f"chúc buổi tối tốt lành")
            else:
                speak(f"chúc một ngày mới an lành ")
            break
        
        robot(query)

main()