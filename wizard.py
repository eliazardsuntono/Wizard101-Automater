from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def press(inter=1):
    while True:
        keyboard.press('d')
        keyboard.release('d')
        print("Pressed 'd'")
        time.sleep(inter)

if __name__ == "__main__":
    try:
        press()
    except KeyboardInterrupt:
        print("Stopped")

