import pyglet
import threading
import pyttsx3
import time
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import tkinter as tk
import tkinter
from tkinter import messagebox
from tkinter import *
import os
import time
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)


def anim():
    animation = pyglet.image.load_animation('giphy1.gif')
    animSprite = pyglet.sprite.Sprite(animation)
 
 
    w = animSprite.width
    h = animSprite.height
 
    window = pyglet.window.Window(w,h,"MuteX")
    icon=pyglet.image.load('chatbot.ico')
    window.set_icon(icon)
 
    r,g,b,alpha = 0.5,0.5,0.8,0.5
 
    pyglet.gl.glClearColor(r,g,b,alpha)
    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()
    pyglet.app.run()
def help():
    root = Tk()
    root.title("Help")
    root.minsize(230, 25) 
    def window():
        top = Tk()  
        top.title("Help Window")
        text = Text(top)  
        text.insert(INSERT, ":: MuteX The Virtual Asistant ::\n")  
        text.insert(END, "Following Commands You can give  the Assistant :\n")  
        text.insert(END, "Command :: Open google \n For opeining google in browser\n ")
        text.insert(END, "Command :: Open Youtube \n For opeining youtube in browser\n ")
        text.insert(END, "Command :: keyword Wikipedia  \n For searching On wikipedia\n ")
        text.pack()  
        top.mainloop()  
    framewindow = Button(root, text="Help", command=window)
    framewindow.pack()
    framewindow.grid(column=1,row=1,sticky=E+W)
    root.grid_columnconfigure(1,weight=1)

    root.mainloop()
def speak(audio):
    time.sleep(1)
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 
    speak('I am Listening Tell Me What Can i Do')
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        speak("Recognizing...")   
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("You Said",query)

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak('Not getting please Say that Again')  
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('debhere23.com', 'Debiprasad#99')
    server.sendmail('debhere23@gmail.com', to, content)
    server.close()
def search(qury):
    CHROME_DVR_DIR = 'C:\webdrivers\chromedriver.exe'
    driver = webdriver.Chrome(CHROME_DVR_DIR)
    baseurl=u'https://twitter.com/search?q='
    query=qury
    url=baseurl + query
    driver.get(url)
    time.sleep(1)   

    
if __name__ == "__main__":
    thread1 = threading.Thread(target = anim)
    thread1.start()
    thread2 = threading.Thread(target = speak)
    thread2.start()
    thread3 = threading.Thread(target = help)
    thread3.start()
    speak('Hello ')
    speak('Im Mutex  Welcome Here')
    wish()
    while True:
        query = takeCommand().lower()
        if 'hi' in query:
            print('Hello Their')
            speak('hello their')
            
        elif 'who is the creator' in query:
            speak('Its a Teamwork by Debi and Mahesh')
        elif 'who are you'in query:
            speak('am just an artificial inteligence')
        elif 'what can you do' in query:
            speak('i can play music open google and serch wikipedia etc')
        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak('opening Stackoverflow')
            webbrowser.open("stackoverflow.com")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results) 
        elif 'play music' in query:
            music_dir = 'E:\Music\English'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak('Whom you want to send ::')
                to = input()    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend debi . I am not able to send this email")  
        elif 'twitter' in query:
            speak("Whom you want to search")
            src=takeCommand()
            speak('Searching On Twitter ')
            search(src)
            time.sleep(1)
            speak('Executed')
            speak('Here What i found on twitter')
