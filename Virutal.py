import speech_recognition as sr
import pyttsx3
import pygetwindow as gw
import os
import webbrowser
import wikipedia                  
import pywhatkit
r=sr.Recognizer()
engine = pyttsx3.init()
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
with sr.Microphone() as source:
    try:
        print("please say something")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        speech=r.recognize_google(audio)
        print("the word be:"+speech)
        if 'how are you' in speech:
            print("I am fine")
        elif 'what are you doing' in speech:
            print("waiting for your command")
        elif 'open Notepad' in speech:
            file=input("enter the filename with extension:")
            print("the filename is:"+file)
            path="c:\\Program Files\\Notepad++"+"\\"+file
            os.startfile(path)
            print("The notepad is opened")
        elif 'close notepad' in speech:
            size=len(file)
            s=file[:size - 4]
            notepadWindow=gw.getWindowsWithTitle(s)[0]
            notepadWindow.close()
            print("The notepad is closed")
        elif 'open Google' in speech:
            webbrowser.open("https://www.google.com")
            print("Google is opened")
        elif 'close Google' in speech:
            googlewindow=gw.getWindowsWithTitle("chrome")[0]
            googlewindow.close()
            print("Google is closed")
        elif 'open YouTube' in speech:
            webbrowser.get('chrome').open("https://youtube.com/")
            print("The Youtube is opened")
        elif 'close YouTube' in speech:
            youtube=gw.getWindowsWithTitle("chrome")[0]
            youtube.close()
            print("The YouTube is closed")
        elif 'play'in speech:
            song=speech.replace('play','')
            pywhatkit.playonyt(song)
        elif 'open Instagram' in speech:
            webbrowser.get('chrome').open('https://www.instagram.com/')
            print("Instagram is opened")
        elif 'close Instagram' in speech:
            Instagram=gw.getWindowsWithTitle("chrome")[0]
            Instagram.close()
            print("Instagram is closed")
        elif 'open Facebook' in speech:
            webbrowser.get('chrome').open('https://www.facebook.com/')
            print("Facebook is opened")
        elif 'close Facebook' in speech:
            facebook=gw.getWindowsWithTitle("chrome")[0]
            facebook.close()
            print("Facebook is closed")
        elif 'open Twitter' in speech:
            webbrowser.get('chrome').open('https://twitter.com/i/flow/login')
            print("Twitter is opened")
        elif 'close Twitter' in speech:
            Twitter=gw.getWindowsWithTitle("chrome")[0]
            Twitter.close()
            print("Twitter is closed")
        elif 'open Snapchat'in speech:
            webbrowser.get('chrome').open('https://accounts.snapchat.com/accounts/v2/login')
            print("Snapchat is opened")
        elif 'close Snapchat' in speech:
            Snapchat=gw.getWindowsWithTitle("chrome")[0]
            Snapchat.close()
            print("Snapchat is closed")
        elif 'nice to meet you' in speech:
            print("ok")
    except Exception as e:
        print("Error")
    engine.say(speech)
    engine.runAndWait()
