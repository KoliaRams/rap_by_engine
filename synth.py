import pyttsx3
from pynput import keyboard

engine = pyttsx3.init()

with open('./texte.txt') as f:
        lines = f.read().splitlines()
        # time.sleep(25)

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', 'french')
#print(voices)
#for voice in voices:
#    print("Voice")
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+30)

volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.75)
"""
engine.say(lines)
engine.runAndWait()
"""
# if keyboard.is_pressed('q'):
#     engine.say(lines)
#     engine.runAndWait()



def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def on_press(key):
    key_name = get_key_name(key)
    if key_name == "Key.space":
        engine.say(lines)
        engine.runAndWait()

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()