from core.speaker import speak

def process(command : str) :
    if "stop listening" in command or "exit" in command or "quit" in command :
        speak("Shutting Down. Goodbye!")
        exit()
    else :
        speak("I heard you say " + command)