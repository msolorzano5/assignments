# task: Display a personalized greeting based on the user’s name and the time of day.

import time

def main():
    # check if we know the user name
    with open("data.txt", 'r') as d:
        d = [line.strip() for line in d]
        
    exec(d)
    print(user_name)






if __name__ == "__main__":
    main()
