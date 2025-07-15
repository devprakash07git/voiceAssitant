import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2   
import socket 
import wikipedia
import webbrowser
import pywhatkit as Kit
import smtplib
import sys 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 'voice' not 'voices'

# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# To convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
 
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query

        except sr.WaitTimeoutError:
            print("⏰ Timeout: You didn't speak in time.")
            speak("You didn't speak in time.")
            return "none"

        except sr.UnknownValueError:
            print("🙊 Could not understand the audio.")
            speak("I could not understand. Please say that again.")
            return "none"

        except Exception as e:
            print(f"❌ Error: {e}")
            speak("Say that again please.")
            return "none"


#to wish 
def wish() :
    hour =  int(datetime.datetime.now().hour)

    if hour>0 and hour<12 :
        speak("Good Morning")
       # print("Good Morning")
    elif hour>12 and hour<18 :
          speak("good afternoon") 
        #  print( "good afternoon")
    else:
         speak("good evening") 
        # speak("Good Morning")

    speak("i am jarvis sir. tell me how can  i help you")
    #print(" i am jarvis sir. tell me how can  i help you")

def senEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('your email id', to , content)
    server.close()
         

if __name__ == "__main__":
    wish()
     
    while True :

        query = takecommand().lower()
        #logic building for task
        if "open notepad" in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
            
        elif "open command prompt" in query :
             os.system("start cmd")

        elif "open camera" in query :
            cap=cv2.VideoCapture(0) 
            while True :
                ret , img= cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==5 :
                    break
            cap.release()
            cv2.destroyAllWindows()
        
        elif "ip address" in query:
         hostname= socket.gethostname()
         local_ip=socket.gethostbyname(hostname)
         speak(f" your ip is{local_ip}")

        elif "wikipedia" in query :
         speak("searching wikipedia....")
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=2)
         speak("according to wikipedia")
         speak(results)
        # print(results)

        elif "open youtube" in query :
         webbrowser.open("www.youtube.com")

        elif "search" in query:
          speak("What should I search for?")
          cm=  takecommand().lower()
          if query:
            webbrowser.open(f"https://www.google.com/search?q={cm}")

        elif "open google" in query:
             speak("sir,what shoild i search on google")
             cm=takecommand().lower()
             webbrowser.open(f"{cm}")

        elif "send message" in query:
            Kit.sendwhatmsg("+1234567891","this is python programing",13,2)

        elif "send email" in query :
            try:
                speak("what should i say??")
                content =takecommand().lower 
                to=" djheurgr@gmail.com" #sender email
                sendEmail(to,content)
                speak(" Email has been sent ...")
            
            except Exception as e: 
                print(e)
                speak("sorry sir, i am not able to sent this email to ...")

        elif "no thanks" in query :
            speak("thamks for using me sir , have a good day")
            sys.exit()
        
       
       
        speak("sir , do you have any other work")




        

         
         


         



 
    
