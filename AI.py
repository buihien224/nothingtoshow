import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:	
	    print("Robot: I'm Listening")
	    audio = robot_ear.listen(mic)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""

	print("You: " + you)


	if you == "":
		robot_brain = "Say something, Hien224"
	elif you == "hello":
		robot_brain = "Hello Hien224"
	elif you == "today":
		today = date.today()
		robot_brain = today.strftime("%d/%m/%Y")
	elif you == "time now":
	    now = datetime.now()
	    robot_brain = now.strftime("%H hours %M minutes %S second")
	elif you == "who are you":
	    robot_brain = "not you"
	elif "tell me if you can hear me" in you:
		robot_brain = "hi Hien224"
	elif "goodbye" in you:
		robot_brain = "Bye bye bye"
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "Have a nice day"

	print("Robot: " + robot_brain)


	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()

