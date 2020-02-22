import os
import webbrowser
import subprocess
import pyttsx3
import speech_recognition as sr
import random
import datetime

engine =pyttsx3.init()
voices = engine.getProperty('voices') 
rate = engine.getProperty('rate')
engine.setProperty('rate', 150) 
r=sr.Recognizer()


#GREETINGS //////////
engine.say("Oh, oh, oh, hello Dolling! Oh, i forget! Hans is here!")
engine.runAndWait()

	#LISTENING///////////
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	engine.say("Can i start, boss?")
	engine.runAndWait()
	print("Can i start, boss?")
	audio= r.listen(source)
	command = input()
# try:
# 	command=r.recognize_google(audio)
# 	engine.say(command)
# 	engine.runAndWait()
# 	print(command)
# except sr.UnknownValueError:
# 	print("Could not undertand audio")
# except sr.RequestError as e:
# 	print("Could not request results; {0}".format(e))
		
	#COMMANDS////////////////////////////////////
	
	#day
if command == "day" or command == "this day" or command == "today"or command == "yes":
	os.system("clear")
	print("*Hmm .. Hmm*")
	print("To my wonderful mother on your birthday: You have given me tough love.\
		 \nYou have given honest advice even when I didn’t want to hear it.\
		 \nYou have encouraged me and chastised me when I needed it.\
		  \nYou are everything to me and the reason I turned out to be the best version of me.\
		  \nI am wishing you a wonderful birthday, from my heart to yours!")
	engine.say("To my wonderful mother on your birthday: You have given me tough love. You have given honest advice even when I didn’t want to hear it. You have encouraged me and chastised me when I needed it. You are everything to me and the reason I turned out to be the best version of me. I am wishing you a wonderful birthday, from my heart to yours!")
	engine.runAndWait()
	print()
	print("Dear Mom.\
		\nYou are responsible for the person I am today.\
		\nSo when I mess up, remember that I am just a product of my upbringing.\
		\nHave a special birthday!")
	engine.say("Dear Mom. You are responsible for the person I am today. So when I mess up, remember that I am just a product of my upbringing. Have a special birthday!")
	engine.runAndWait()
