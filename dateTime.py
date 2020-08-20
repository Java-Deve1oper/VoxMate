import pyttsx3   # this moduke is for  textTospeak 
from datetime import datetime  # for current date & time
from datetime import date

def dateT(inp):
    if("time" in  inp):
       pyttsx3.speak(datetime.now().strftime("%H:%M:%S"))
    elif("date" in inp):
       pyttsx3.speak(date.today())
    
      




