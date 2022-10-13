import random  #random variable generators
import pyautogui #an automation library that allows mouse and keyboard control.
import string #collection of string constants. 
import pyttsx3 #python module to convert text to speech.
# chars1 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ #`~!@$%^&*()_+|}{':?>< -=\][';/.,"
# chas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# bat = 'tab'

engine = pyttsx3.init()

chars = string.printable 
chars_list = list(chars) 

def speak(text): #function name is speak and parameter is text.
    engine.say(text)
    engine.runAndWait() #if the engine is currently busy speaking an utterance or not. Returns: True if speaking, false if not.

# print(chars1)
print('Hey, Enter your password now...')
speak('Hey, Enter your password now')
password = pyautogui.password("Enter a password:")

guess_password = " "

while(guess_password != password): 
    guess_password = random.choices(chars_list, k=len(password))  #len -> returns the number of items in a container
    # guess_password = random.choices(chas, k=len(password))
    # guess_password = random.choices(bat, k=len(password))

    print("\t\t<=================" + str(guess_password) + "==================>") #str -> converts the input into a string 

    if(guess_password == list(password)): #list -> if no argument is given, the constructor creates a new empty list.
        print('your password is:' + "".join(guess_password)) #The argument must be an iterable if specified.
        speak('your password is : ' + "".join(guess_password)) #.join -> joins strings together into one.
        break
