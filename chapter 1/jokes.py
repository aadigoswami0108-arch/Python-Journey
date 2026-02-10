import pyjokes
import pyttsx3

a = pyjokes.get_joke()


#(Aadi created this program hehhe)
print("Bas Kar bassi")
print("PRINTING JOKES.......")
print(a)


engine = pyttsx3.init()
engine.say(a)
engine.runAndWait()