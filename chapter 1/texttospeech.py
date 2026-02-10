import pyttsx3


def speak(text: str) -> None:
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()


def main() -> None:
	try:
		user_text = input("Enter text to speak : ")
	except EOFError:
		user_text = ""

	if not user_text.strip():
		user_text = "Aadi is King, and he is the best programmer in the world."

	speak(user_text)


if __name__ == "__main__":
	main()