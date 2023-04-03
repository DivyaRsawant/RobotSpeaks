import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to RobotSpeaks by Divya")
    while True:
        x = input("Enter what do I speak : ")
        if x == "bye":
            pyttsx3.speak("bye- bye")
            break
        engine.say(x)
        engine.runAndWait()
