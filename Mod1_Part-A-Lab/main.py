# task: Display a personalized greeting based on the user’s name and the time of day.
from datetime import datetime

def say(text):
    # replace with actual TTS logic
    print(text)

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
            name = input("What is your name? ")
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
    to_say = f"Hello {user_name}. The date is {date}, it is {day}, and the time is {time}"
    say(to_say)




