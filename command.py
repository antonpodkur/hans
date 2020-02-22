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
engine.setProperty('rate', 170) 
r=sr.Recognizer()

random.seed()
#asking to continue dictionary///////
asktocont={1:"Do you want to continue?", 2:"Something else?", 3:"Maybe, you want something?",4:"Please, say no, i want  to go!"}
amount_asktocont=0
for i in asktocont:
	amount_asktocont+=1

#GREETINGS //////////
greetings={1:"Hello, my name is Hans!",2:"Hi, Hans is here!",3:"Welcome to my kingdom,buddy!",4:"Greetings, my boss!"}
#amount of frases////////////////////
amount = 0
for i in greetings:
	amount+=1
num = random.randint(1,amount)
if num==1:
	engine.say(greetings[1])
	engine.runAndWait()
if num ==2:
	engine.say(greetings[2])
	engine.runAndWait()
if num ==3:
	engine.say(greetings[3])
	engine.runAndWait()
if num ==4:
	engine.say(greetings[4])
	engine.runAndWait()
ans = "yes"
while ans == "yes":
	
		#LISTENING///////////
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		engine.say("What can i do for you?")
		engine.runAndWait()
		print("What can i do for you?: ")
		audio= r.listen(source)
	try:
		command=r.recognize_google(audio)
		engine.say(command)
		engine.runAndWait()
		print(command)
	except sr.UnknownValueError:
		print("Could not undertand audio")
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
		#COMMANDS////////////////////////////////////
		
		#what can u do////////////
	if command == "commands" or command == "show the commands" or command == "command" or command == "what can you do" or command == "what do you can":
		print("Aviable commands:")
		engine.say("Here you can see the avaible commands.")
		engine.runAndWait()
		print("Open the browser")
		print("Open link")
		print("Search the web")
		print("Open telegram")
		print("Tell me the date")
		print("What is the time")
		print("Today or this day")
		
		#date/////////////////
	if command == "tell me the date" or command == "date" or command == "the date":
		datevar = datetime.date.today().strftime("%B %d, %Y")
		print(datevar)
		engine.say(datevar)
		engine.runAndWait()
		
		#time/////////////////////
	if command  == "what is the time" or command == "time" or command == "show time":
		datevar = datetime.datetime.now().strftime("%I:%M%p")
		print(datevar)
		engine.say(datevar)
		engine.runAndWait()
		
		#everything about this day/////////////
	if command == "today" or command == "this day":
		datevar = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
		print(datevar)
		engine.say("Today is "); engine.say(datevar)
		engine.runAndWait()
		
		#open the browser///////////////////
	if command == "open the browser" or command == "browser":
		engine.say("Okay, my boss!")
		engine.runAndWait()
		webbrowser.open('http://google.com')
		
		#open the link////////////////////////
	if command == "open link" or command == "link":
		link = input("Enter your link: ")
		webbrowser.open(link)
		
		#serch the web////////////////////////
	if command == "search the web" or command == "search" or command == "web" or command == "search web":
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			engine.say("What do you want to search?")
			engine.runAndWait()
			print("What do you want to search?")
			audio= r.listen(source)
		try:
			whattosearch = r.recognize_google(audio)
			engine.say(whattosearch)
			engine.runAndWait()
			print(whattosearch)
		except sr.UnknownValueError:
			print("Could not undertand audio")
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
		url = "https://www.google.com.ua/search?q={0}".format(whattosearch)    
		webbrowser.open(url)
		
		#open telegram/////////////////
	if command == "open telegram" or command == "telegram":
		os.system("telegram-desktop")
	
	#do you want to continue////////////////
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		#choosing what to say/////////////4
		num=random.randint(1,amount_asktocont)
		engine.say(asktocont[num])
		engine.runAndWait()
		print(asktocont[num])
		audio= r.listen(source)
	try:
		ans=r.recognize_google(audio)
		print(ans)
	except sr.UnknownValueError:
		print("Could not undertand audio")
		break
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))

#ENDING////////////////
endings = {1:"Goodbye, boss, i love you!", 2:"See you later!", 3:"Have a nice day", 4:"So, i can do everything i want?"}
#amount/////////
amount = 0
for i in endings:
	amount+=1
num = random.randint(1,amount)
engine.say(endings[num])
engine.runAndWait()
