
import pyttsx3

a = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!"
print(a)
engine = pyttsx3.init()
engine.say(a)
engine.runAndWait()