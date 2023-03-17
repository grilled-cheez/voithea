import speech_recognition as sr
import pyttsx3 as tts
import os
import smtplib
import webbrowser
import wikipedia
import datetime
import wolframalpha
import openai
import pyaudio


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening")

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing")

            Query = r.recognize_google(audio, language="en-in")
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again")
            return "None"

        return Query


def speak(audio):
    engine = tts.init()

    voices = engine.getProperty("voices")

    engine.setProperty("voice", voices[1].id)

    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")


def Hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    speak("kyaa hai?")


def Take_query():
    Hello()

    while True:
        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output
        query = input("query bolo  :  ")
        """takeCommand().lower()"""

        if "play a song called" in query:
            speak("Playing the gaana ")
            songname = query.s

            webbrowser.open(f"www.youtube.com/{songname}")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "which day it is" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        # this will exit and terminate the program
        elif "bye" in query:
            speak("Bye. chew tea yah")
            exit()

        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("I am Baburao gunpath rao aaptae.")


if __name__ == "__main__":
    Take_query()
