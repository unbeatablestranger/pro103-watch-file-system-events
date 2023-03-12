import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Dell/Downloads/WhiteHatJr/pro103-watch-file-system-events"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}")

    def on_moved(self, event):
        print(f"Hey, {event.src_path} was moved or its name was changed")    

    def on_modified(self, event):
        print(f"Hey, {event.src_path} was modified")


#Initialize Event Handler Class
event_handler = FileEventHandler()

#Initialize Observer
observer = Observer()

#Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

#Start The Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()        
