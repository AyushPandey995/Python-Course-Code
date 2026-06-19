name = "Ayush"
print(name)
date = 7
print(date)
cgpa = 8.92
print(cgpa)
print(type(name))
print(type(date))
print(type(cgpa))

"""module example"""
import pyttsx3
engine = pyttsx3.init()

engine.say("Hey Ayush.. I am Jarvis, and I will do what ever you say ")
engine.runAndWait()