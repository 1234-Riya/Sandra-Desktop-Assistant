import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Sandra. Please tell me how may I help you")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 3500
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None" #None string will be returned
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender's email', 'password')
    server.sendmail('reciever's email', to, content)
    server.close()
if __name__ == "__main__":
    wishme()
    # while True:
    if 1:
        query = takeCommand().lower()

    #logic for executing task based on query
    # speak('Riya is a goodgirl')
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences =3)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open chandigarh' in query:
            webbrowser.open("cuims.in")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.in")
        elif 'play music' in query:
            music_dir = "C:\\string\\Riya\\audioFiles"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strtime)   
            speak(f"Sir, the time is {strtime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\riya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "sender's email"
                sendemail(to,content)
                speak("email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry There is some problem in fetching the data")

        elif 'quit' in query:
            speak("Thankyou sir for your time")
            exit()

        
