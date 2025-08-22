# task: Display a personalized greeting based on the user’s name and the time of day.
from datetime import datetime
import pyttsx3

### set up the TTS engine ###
engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_date_time():
    dated = datetime.now().date()
    time = datetime.now().time()
    date = dated.strftime("%B %d, %Y")
    day = dated.strftime("%A")
    time = time.strftime("%I:%M %p")
    return date,day,time

def get_info(info):
    with open("data.txt", 'w') as data_file:
        if info == "name":
            speak("Can you please tell me your name?")
            name = input("")
            data_file.seek(0)
            data_file.write(name)

def update_info():
    with open("data.txt", 'r') as d:
        data = [line.strip() for line in d]
    return data

if __name__ == "__main__":
    # load and update data
    d = update_info()
    # check if we know the user's name
    user_name = d[0]
    if user_name == 'None':
         get_info("name")
         d = update_info()
         user_name = d[0]

    ## start building the string to say
    date, day, time = get_date_time()
    to_say = f"Hello {user_name}. The date is {date}, on a {day}, and the time is {time}"
    speak(to_say)
