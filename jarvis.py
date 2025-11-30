
import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess
import google.generativeai as genai 

# Logging configuration
LOG_DIR = 'logs'
LOG_FILE_NAME = 'application.log'
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Activating voice
engine = pyttsx3.init("sapi5")
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('rate', 125)
engine.setProperty('voice', voices[0].id)


# This is speak function
def speak(text):

    """
    This function converts text to voice

    Args:
        text
    return:
        Voice
    """

    engine.say(text)
    print(f"Assistant:", text)
    engine.runAndWait()

# This function recognize the speech and convert it to text
def takeCommand():

    """"This function takes command & recognize
    Return:
        text as query
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!.......")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')  # or bn-BD
        print(f"User said: {query}")
        return query

    except Exception as e:
        print("Didn't catch that, say again...")
        return "None"   
    
def greeting():
   import datetime
   time_now = datetime.datetime.now()
   hour = time_now.hour   # integer
   minute = time_now.minute
   print(f"{hour}:{minute}")
   if 0 <= hour < 12:
       speak("Good Morning sir!")
   elif 12 <= hour < 18:
       speak("Good Afternoon sir!")
   else:
       speak("Good Evening sir!")

  # speak("I am Jarvis. Please tell me how may I help you today?")

def play_music():
    music_dir="G:\Bootcamp\JARVIS-Voice-Assistant-system\JARVIS_Voice_Assistant_system\music"
    try:
        songs=os.listdir(music_dir)
        if songs:
            random_song=random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))
            logging.info(f"Playing music: {random_song}")
        else:
            speak("No music files found in your music directory.")
    except Exception as e:
        speak("Sorry sir, I could not find your music folder.")



def YouTube_music():
    youtube_links = [
        "https://www.youtube.com/watch?v=Lxvg_MQ-fpI&list=RDLxvg_MQ-fpI&start_radio=1",
        "https://www.youtube.com/watch?v=jfKfPfyJRdk",
        "https://www.youtube.com/watch?v=5qap5aO4i9A"
    ]

    random_link = random.choice(youtube_links)
    webbrowser.open(random_link)


def gemini_model_response(user_input):
    GEMINI_API_KEY = "AIzaSyB6d3MsM0ajY5UaUTFtwBY7j83DYzFQxzo"
    genai.configure(api_key=GEMINI_API_KEY) 
    model = genai.GenerativeModel("gemini-2.5-flash") 
    prompt = f"Your name is JARVIS, You act like JARVIS. Answar the provided question in short, Question: {user_input}"
    response = model.generate_content(prompt)
    result = response.text

    return result





greeting()
speak("I am Jarvis. How are you doing? Please tell me how may I help you today?")


while True:
    # query = takeCommand().lower()

    # if query:  
    #     speak(query)
    
    query=takeCommand().lower()

    print(query)


    if 'name' in query:
        speak("My name is Jarvis")
        logging.info("user asked for assistant's name.")


    elif "time" in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir the time is {strTime}")


    #small talk
    elif "how are you" in query:
        speak("I am fine sir! And you?")

    elif "fine" in query:
        speak("Okay Thank you sir! Please say can I help you ?")



    elif "who made you" in query or " who build you" in query:
        speak("It was created by Tauhid Mahmud, a brilliant mind!")


    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")
        logging.info("")


    #Open Google
    elif "open google" in query or "open a google" in query:
        speak("ok sir. please type here what do you want to read")
        webbrowser.open("google.com")
        logging.info("User requested to open Google.")


    #Calculator 
    elif "open calculator" in query or "calculator" in query:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")
        logging.info("User requested to open the calculator")



     # Notepad
    elif "open notepad" in query:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
        logging.info("User requested to open Notepad.")

    #Open terminal
    elif "open terminal" in query or "open cmd" in query or "open a terminal" in query:
        speak("Opening command prompt terminal")
        subprocess.Popen("cmd.exe")
        os.system("start cmd")
        logging.info("User requested to open Command prompt.")
    

    #play music
    elif "play music" in query or "music" in query:
        play_music()

    #Play_YouTube_Music
    elif "play youtube music" in query:
        YouTube_music()


    #Calender
    elif "open calender" in query or "calender" in query or "open a calender" in query:
        speak("Opening windows calender")
        webbrowser.open("https://calendar.google.com")
        logging.info("User requested to open Calendar.")


    #YouTube Search
    elif "youtube" in query:
        speak("Opening YouTube for you")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        logging.info("User requested to search on YouTube.")


    #Open facebook
    elif "open facebook" in query or "open a facebook" in query:
        speak("ok sir. opening facebook")
        webbrowser.open("https://www.facebook.com/")
        logging.info("User requested to open Facebook.")

    #Wikipedia
    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        logging.info("User requested information from Wikipedia.")


    #open GitHub
    elif "open github" in query or "open a github" in query:
        speak("ok sir. opening github")
        webbrowser.open("github.com")
        logging.info("User requested to open GitHub.")


# Open LinkedIn
    elif "open linkedin" in query or "open a linkedin" in query:
        speak("Ok sir, opening LinkedIn.")
        webbrowser.open("https://www.linkedin.com/jobs/")
        logging.info("User requested to open LinkedIn.")


    # Jokes
    elif "joke" in query:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I asked my computer for a joke… and it gave me a blue screen!",
            "Why was the JavaScript developer sad? Because he didn’t 'Node' how to Express himself.",
            "Why was the computer cold? It forgot to close its Windows.",
            "Why do Python devs eat snacks? Because they love bytes!",
            "My WiFi went down for 5 minutes… so I had to talk to my family. They seem like nice people.",
            "Why don’t robots panic? They have nerves of steel.",
            "A SQL query walks into a bar… He joins two tables and asks for a drink."
        ]

        speak(random.choice(jokes))
        logging.info("User requested a joke.")



    elif "exit" in query or "bye" in query:
        print("Thank you for your time sir. Have a grate day ahead!")
        logging.info("User Exited the program. ")
        exit()

    
    else:
        response = gemini_model_response(query)
        speak(response)
        logging.info("User asked for others question")
        

    

