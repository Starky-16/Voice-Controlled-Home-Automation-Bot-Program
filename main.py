import speech_recognition as sr

# Simulated devices
devices = {
    "light": False,
    "fan": False,
    "ac": False
}

def control_device(device, action):
    if device in devices:
        if action == "on":
            devices[device] = True
            print(f"{device.capitalize()} turned ON ✅")
        elif action == "off":
            devices[device] = False
            print(f"{device.capitalize()} turned OFF ❌")
        else:
            print("Unknown action! Say 'on' or 'off'.")
    else:
        print("Unknown device! Try light, fan, or AC.")

def parse_command(command):
    words = command.lower().split()
    if "on" in words:
        for device in devices:
            if device in words:
                control_device(device, "on")
                return
    elif "off" in words:
        for device in devices:
            if device in words:
                control_device(device, "off")
                return
    print("Command not recognized! Try again.")

def listen_and_execute():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎤 Say a command like 'Turn on the light' or 'Turn off the fan'...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        parse_command(command)
    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
    except sr.RequestError:
        print("Speech recognition service error!")

if __name__ == "__main__":
    while True:
        listen_and_execute()
