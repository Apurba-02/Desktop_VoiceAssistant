import pyttsx3
import speech_recognition
from bs4 import BeautifulSoup
import requests
import datetime
import pyautogui
import os
import wolframalpha
from online import find_my_ip, search_on_google, youtube, weather_forecast
from INTRO import play_gif

play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
      
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "stop" in query:
                    speak("Ok sir , You can me call anytime")
                    break 
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                    
                elif "open youtube" in query:
                    speak("What do you want to play on youtube sir?")
                    video = takeCommand().lower()
                    youtube(video)

                elif "open google" in query:
                    speak(f"What do you want to search on google")
                    query = takeCommand().lower()
                    search_on_google(query)
                    
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                    
                elif "temperature" in query:
                    search = "temperature in  kolkata Newtown"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                elif 'weather' in query:
                    city = find_my_ip()
                    speak(f"Getting weather report for your city {city}")
                    weather, temp, feels_like = weather_forecast(city)
                    speak(f"The current temperature is {temp}, but it feels like {feels_like}")
                    speak(f"Also, the weather report talks about {weather}")
                    speak("For your convenience, I am printing it on the screen sir.")
                    print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")
                    
                elif "what's the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                    
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                elif "calculate" in query:
                    app_id = ""
                    client = wolframalpha.Client(app_id)
                    ind = query.lower().split().index("calculate")
                    text = query.split()[ind + 1:]
                    result = client.query(" ".join(text))
                    try:
                        ans = next(result.results).text
                        speak("The answer is " + ans)
                        print("The answer is " + ans)
                    except StopIteration:
                        speak("I couldn't find that . Please try again")


                elif 'what is' in query or 'who is' in query or 'which is' in query:
                    app_id = ""
                    client = wolframalpha.Client(app_id)
                    try:

                        ind = query.lower().index('what is') if 'what is' in query.lower() else \
                            query.lower().index('who is') if 'who is' in query.lower() else \
                                query.lower().index('which is') if 'which is' in query.lower() else None

                        if ind is not None:
                            text = query.split()[ind + 2:]
                            res = client.query(" ".join(text))
                            ans = next(res.results).text
                            speak("The answer is " + ans)
                            print("The answer is " + ans)
                        else:
                            speak("I couldn't find that. Please try again.")
                    except StopIteration:
                        speak("I couldn't find that. Please try again.")    
                    
                elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                     
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                    
                elif "game" in query:
                    from game import game_play
                    game_play()
                    
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break
                    
                elif "go to sleep" in query:
                    speak("Ok sir , Stopping the voice Assistant")
                    exit()