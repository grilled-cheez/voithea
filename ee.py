import os
import smtplib
import webbrowser
import speech_recognition as sr
import pyttsx3 as tts
import datetime
import openai
from openai import error
import pyaudio
import gradio as gr

engine = tts.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
openai.api_key = str(open("api_key.txt", "r").readline())
y = 1


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def play_song():
    pass


def date_info():
    return datetime.date()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language="en-in")
    except Exception as e:
        print("Say that again please...")
        return "None"
    y = 1
    return query


def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages


def get_chatgpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=1.1, max_tokens=4000
    )
    return response["choices"][0]["message"]["content"]


def dalle_gen(prompt, num):
    response = openai.Image.create(prompt=prompt, n=num, size="1024x1024")
    image_url = response["data"][0]["url"]
    print("Opening the requested images in a browser")
    speak("opening the requested images in a browser")
    for i in response["data"]:
        webbrowser.open_new_tab(i.get("url"))
        print((i.get("url")))


def main():
    print("""My name is Voithea. How can I help you?\n""")
    global y
    while y == 1:
        q = takeCommand()
        test_words = ["generate", "image", "images"]
        print("Processing. Please wait...\n\n")
        speak("Processing. Please wait")
        if "send" and ("email" and "mail") in q:
            print(f"mailn called")
            continue
        elif q == "shutdown":
            print("shutting down")
            y = 0
            break
        elif (
            "generate" in q.split(maxsplit=4)
            and "image" in q.split(maxsplit=4)
            or "images" in q.split(maxsplit=4)
        ):
            num_list = [int(i) for i in q.split() if i.isdigit()]
            num = 1
            if len(num_list) != 0:
                num = num_list[0]
                if num >= 6:
                    print(
                        "Insufficient resources to generate {num} images. Generating 5 images."
                    )
                    num = 5
            for i in ["generate", "images", "image", "of", str(num)]:
                q = q.replace(i, "")
            dalle_gen(q, num)
        elif "the time" in q:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}\n")
            speak(f"The time is {strTime}")
        elif "the date" in q:
            print(datetime.datetime.now().strftime("%m/%d/%Y"))
            speak(datetime.datetime.now().strftime("%m/%d/%Y"))
        elif "open" in q.split(maxsplit=4):
            url = q.split()[1]
            print("Opening in browser...\n")
            speak("opening webpage")
            if "." in url:
                webbrowser.open_new_tab(f"https://www.{url}")
            else:
                webbrowser.open_new_tab(f"https://www.{url}.com")
        else:
            messages = [
                {
                    "role": "system",
                    "content": "You are called voitheia, my personal assistant.",
                },
                {
                    "role": "user",
                    "content": "I am User.",
                },
            ]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            # for debugging --> pprint.pprint(messages)
            user_input = q
            messages = update_chat(messages, "user", user_input)
            try:
                model_response = get_chatgpt_response(messages)
                messages = update_chat(messages, "assistant", model_response)
            except error.RateLimitError:
                print("Server busy. Please try again after sometime")
            print(f"{model_response}\n")
            speak(model_response)


if __name__ == "__main__":
    main()
