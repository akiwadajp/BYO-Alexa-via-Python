import speech recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listeners = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getPorperty("voices")
engine.setProperty('voice', voices[1].id)

def talk(text):
  engine.say(text)
  engine.runAndWait()
  
def take_command():
  try:
    talk(info)def take command):
  
 try:
  with sr.Microphone() as source:
    print('listening ...')
    voice = listern.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower()
    if 'alexa' in command:
      command = command.replace('alexa', '')
      print(command)
 
except:
  pass
return command

def run_alexa():
  command = take_command()
  print(command)
  if 'play' in command:
    song = command.replace('play', '')
    talk('Playing ' + song)
    pywhatkit.playonyt(song)
  elif 'time' in command:
    time = datetime.datetime.now()
