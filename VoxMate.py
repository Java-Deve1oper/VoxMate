#import speech_recognition as sr
import pyttsx3
import os
import dateTime

pyttsx3.speak("Hi Good Morning  Vipin ")

pyttsx3.speak("What can i do for you ")

#r = sr.Recognizer()
z = input()
if("time" in z )  or ("date" in z):
   dateTime.dateT(z)
elif (("run" in  z) or ("open" in z)) and (("media" in z)or("player" in z)):
  os.system("vlc")
elif (("run" in  z) or ("open" in z)) and (("notepad" in z)or("editior" in z)):
  os.system("notepad")
elif (("run" in  z) or ("open" in z)) and (("chrome" in z)or("mozila" in z)):
  os.system("chrome")
else:
  pyttsx3.speak("No , such thing available")