def main(end):  # I know main function isn't required in py
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
            speak("hãy nói lại để tôi rõ hơn ")
            query = "hãy nói lại"
            # robot()
        return query

    greet_user()
    def robot():
    
        if __name__ == "__main__":

            if True:
                query = "mở notepad"
                print("query=",query)
                if query=="hãy nói lại": 
                    robot()
                
                if "một ngày" in query and ("đẹp trời" in query or "tồi tệ" in query):
                    try:
                        if "đẹp trời" in query:  
                            speak("Tôi chỉ là 1 công cụ máy tính, tôi không thể biết được hôm nay như thế nào")
                            if "để" not in query:
                                speak("bạn có muốn nói một thứ gì khác không")
                                robot()
                        elif "tồi tệ" in query:
                            speak("Tôi không biết, nhưng hy vọng bạn sẽ có một ngày tốt hơn.")
                            if "để" not in query:
                                speak("Tôi không thể cảm nhận được cảm giác của bạn, nhưng tôi luôn ở đây để giúp bạn nếu cần.")
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

                    
    speak("Hãy nói gì đó")
    robot()

    while True:
        query = take_user_cmd().lower()
        
        if query == "có" or query == "đúng vậy":
            speak("rất tốt, hãy hỏi tôi tiếp đi")
            robot()
        elif query == "không" or query == "không phải bây giờ" or query == "nâu" or query == "lâu":
            speak("cảm ơn vì đã sử dụng tôi")
            hour = datetime.datetime.now().hour
            if hour >= 22 and hour < 6:
                speak(f"chúc buổi tối tốt lành")
            else:
                speak(f"chúc một ngày mới an lành")
            break
        else:
            speak(print("Điều đó có lẽ vượt quá khả năng của tôi vào lúc này"))


main(False)