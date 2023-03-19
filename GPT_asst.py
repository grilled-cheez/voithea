from openai import error
import openai
import datetime
import pyttsx3 as tts
import speech_recognition as sr
import webbrowser
import os
import webview
import smtplib
from email.message import EmailMessage
import json
import PySimpleGUI as sg
from AppOpener import open as appopen
import textwrap as tw

stop_value = 0
engine = tts.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
openai.api_key = str(open("api_key.txt", "r").readline())
y = 1

mymail = os.environ.get("email_temp")
mypass = os.environ.get("pass_temp")

# mute button linked heree
mute_value = 0
lq = []
state = ''


def speak(audio):
    if mute_value == 1:
        engine.stop()
    engine.say(audio)
    engine.runAndWait()


def play_song():
    pass


def dall_e_layout(urls):  # function takes the list of urls of the generated images and produces a well laid output requires an index.txt file and an empty index.html file
    h = 0
    w = 0
    # def dall_e_layout(urls):  # function takes the list of urls of the generated images and produces a well laid output requires an index.txt file and an empty index.html file
    f = open('index.txt', 'r+')
    webpage = open('index.html', 'w+')
    webcode = f.read()
    num = len(urls)

    if num <= 2:
        w1 = 1
    elif 2 < num <= 4:
        w1 = 2
    else:
        w1 = 3
    h = 730
    w = 1.035 * w1 * 341
    if '<div class="container">' in webcode:
        ind = webcode.index('<div class="container">') + \
            len('<div class="container">')
        for i in range(0, len(urls), 2):
            image_design = ''
            image_design = image_design + \
                f'<div class="image"> <img src="{urls[i]}" height="341px" width="341px"/> </div> '
            webcode = webcode[:ind] + image_design + webcode[ind:]
        ind1 = webcode.index('<div class="container1">') + \
            len('<div class="container1">')
        for i in range(1, len(urls), 2):
            image_design = ''
            image_design = image_design + \
                f'<div class="image"> <img src="{urls[i]}" height="341px" width="341px"/> </div> '
            webcode = webcode[:ind1] + image_design + webcode[ind1:]

    webpage.write(webcode)
    webpage.close()
    window = webview.create_window(
        'Images', 'index.html', width=int(w*1.26), height=int(h*1.28))
    webview.start()


def date_info():
    return datetime.date()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        state = "Listening..."
        print("Listening...")
        window["-ST-"].update(state)
        window.refresh()
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        state = "Recognizing..."
        print("Recognizing...")
        # Using google for voice recognition.
        window["-ST-"].update(state)
        window.refresh()
        query = r.recognize_google(audio, language="en-in")
    except Exception as e:
        state = "Say that again please..."
        print("Say that again please...")
        window["-ST-"].update(state)
        window.refresh()
        return "None"
    y = 1
    window["-ST-"].update(state)
    window.refresh()
    lq.append(f"Query: {query}")
    window["-LB-"].update(lq)
    window.refresh()
    return query


def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages


def get_chatgpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages,
    )
    return response["choices"][0]["message"]["content"]


def dalle_gen(prompt, num):
    imgs = []
    response = openai.Image.create(prompt=prompt, n=num, size="1024x1024")
    image_url = response["data"][0]["url"]
    print("Opening the requested images in a browser")
    speak("opening the requested images in a browser")
    for i in response["data"]:
        # webbrowser.open_new_tab(i.get("url"))
        print((i.get("url")))
        imgs.append(i.get("url"))
    print(imgs)
    window.refresh()
    dall_e_layout(imgs)


def main():

    if stop_value == 0:
        print("""My name is Voithea. How can I help you?\n""")
        lq.append(f'Response: My name is Voithea. How can I help you?\n')
        window.refresh()
        global y
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
        while y == 1:
            transcript = ''
            q = "a"
            if q == "":
                q = takeCommand()

            else:
                q = takeCommand()
                lq.append(f"Query: {q}")
                window.refresh()
                test_words = ["generate", "image", "images"]
                print("Processing. Please wait...\n\n")
                state = "Processing. Please wait..."
                window["-ST-"].update(state)
                window.refresh()
                window["-LB-"].update(lq)
                window.refresh()
                speak("Processing. Please wait")

                if q == "shutdown":
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
                        if num >= 7:
                            print(
                                "Insufficient resources to generate {num} images. Generating 6 images."
                            )
                            transcript = "dalle tranccript"
                            num = 6
                    for i in ["generate", "images", "image", "of", str(num)]:
                        q = q.replace(i, "")
                    dalle_gen(q, num)

                    lq.append(f'Response : Your images have been generated')
                    window["-LB-"].update(lq)
                    window.refresh()

                elif "the time" in q:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"The time is {strTime}\n")
                    transcript = f"The time is {strTime}\n"
                    speak(f"The time is {strTime}")

                elif "the date" in q:
                    dateis = datetime.datetime.now().strftime("%m/%d/%Y")
                    print(datetime.datetime.now().strftime("%m/%d/%Y"))
                    transcript = f"The date is {dateis}\n"
                    speak(datetime.datetime.now().strftime("%m/%d/%Y"))

                elif "open" in q.split(maxsplit=4):
                    if "in" in q.split():
                        url = q.split()[1]
                        print("Opening images...\n")
                        state = 'Generating...'

                        window["-ST-"].update(state)
                        window.refresh()

                        speak("opening images")

                        if "." in url:
                            webbrowser.open_new_tab(f"https://www.{url}")
                        else:
                            webbrowser.open_new_tab(f"https://www.{url}.com")
                    else:
                        transcript = "appopen tranccript"

                        appopen(q.split()[1])

                elif (
                    "send" in q.split(maxsplit=4)
                    and "mail" in q.split(maxsplit=4)
                    or "email" in q.split(maxsplit=4)
                ):
                    stmt = f"'{q}'. Get me the subject , content and the reciever from this sentence in a python dictionary with double quotes for each element"
                    messages = update_chat(messages, "user", stmt)
                    mail_response = get_chatgpt_response(messages)
                    speak('Sure')
                    print(mail_response)
                    dict = json.loads(mail_response[mail_response.index(
                        "{"): mail_response.index("}")+1], strict=False)
                    reciever = f"{dict.get['reciever']}@gmail.com"
                    subject = f"{dict.get('subject')}"
                    content = f"{dict.get('content')}"

                    msg = EmailMessage()
                    msg["Subject"] = subject
                    msg["From"] = mymail
                    msg["To"] = reciever
                    msg.set_content(content)
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                        server.login(mymail, mypass)
                        server.send_message(msg)
                        server.quit()
                        print("Email sent")
                        speak("Email sent")
                    transcript = f"Email sent!"

                else:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=messages,
                    )
                    # for debugging --> pprint.pprint(messages)
                    user_input = q
                    messages = update_chat(messages, "user", user_input)
                    model_response = get_chatgpt_response(messages)
                    messages = update_chat(
                        messages, "assistant", model_response)
                    print(f"{model_response}\n")
                    words = model_response.split()
                    grouped_words = [' '.join(words[i: i + 10])
                                     for i in range(0, len(words), 10)]
                    for i in grouped_words:
                        lq.append(f"Response : {''.join(i)}")
                        window["-LB-"].update(lq)
                        window.refresh()
                    window["-ST-"].update(state)
                    state = "Ready!"
                    window.refresh()

                    speak(model_response)

                print(transcript)
                lq.append(f'Response : {transcript}')
                window.refresh()
            window.refresh()

        window.refresh()
    window.refresh()


col_1 = [
    [sg.LB(lq, font=(None, 11), size=(70, 30), key="-LB-")],  # user's query
    # state of the takeCommand function (reassignment)
    [sg.Text(state, font=(None, 15), key="-ST-")],
]
col_2 = [
    [sg.Button('Start', size=(8, 1))],
    [sg.Button('Terminate', size=(8, 1))],
    [sg.Button('Clear', size=(8, 1))],
    [sg.Button('Mute', size=(8, 1), button_color="red")]
]

layout = [
    [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(col_2)]
]

# STEP 2 - create the window
window = sg.Window('Voithea', layout)

# STEP3 - the event loop
while True:
    window.refresh()
    # Read the event that happened and the values dictionary
    event, values = window.read()
    print(event, values)
    window.refresh()

    # If user closed window with X or if user clicked "Exit" button then exit
    if event == sg.WIN_CLOSED or event == 'Terminate':
        window["-LB-"].update(lq)
        window.refresh()
        stop_value = 1
        break

    if event == 'Start':
        window["-LB-"].update(lq)
        window.refresh()
        main()

    if event == 'Clear':
        lq = []
        window["-LB-"].update(lq)
        window.refresh()

    if event == 'Mute':
        mute_value = 1
        lq.append()
        window["-LB-"].update(lq)
        window.refresh()
window.refresh()
window.close()
