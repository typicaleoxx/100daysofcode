import pyttsx3
speak=pyttsx3.init()
speak.say(input("What do want your computer to say?"))
speak.runAndWait()