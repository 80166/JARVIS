import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def current_date_time():
    current_time = datetime.datetime.now()
    # now_date = datetime.date.today()
    print(f"{current_time.hour}:{current_time.minute}")
    speak(f"Its {current_time.hour} and {current_time.minute} minutes")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, Sir")
    
    
    elif hour==12 and hour<16:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")
    current_date_time()
    

    speak("I am JARVIS Sir, How can i help you")


def bye():
    speak("Thank You Sir,HAve a good day")

def takecommand():                 #it takes command from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
        # audio=r.listen(source, timeout=5, phrase_time_limit=5)
    
    try: 
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n") 

    except Exception as e:
        print("Say that again please.")
        return "None"
    
    return query


    


if __name__=="__main__":
    greet()
    while True:
     query = takecommand().lower()


    #  logic for tasks based on query
     if 'wikipedia' in query:
        speak("Searchng Wikipedia......")
        query = query.replace("wikipeadia","" )
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipeadia")
        print(results)
        speak(results)
     elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
     elif 'open google' in query:
         webbrowser.open('google.com')
     
     elif 'bye' in query:
         bye()
         exit()



         

