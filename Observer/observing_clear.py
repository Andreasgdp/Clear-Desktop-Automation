from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


import os
import time
import winshell

# TODO make the program use some kind of observer like https://www.youtube.com/watch?v=qbW6FRbaSl0 to run in the background
# TODO make the program an executable that can be run without terminal as a backgroundprocess in windows (https://www.youtube.com/watch?v=lOIJIk_maO4)

class MyHandler(FileSystemEventHandler):
  i = 1


  def on_modified(self, event):
    for filename in os.listdir(folder_to_track):
      if filename == 'Games':
        continue
      if filename == 'desktop.ini':
        continue
      if filename.startswith('~'):
        continue
      if filename.startswith('.'):
        continue
      if not filename.endswith('.lnk'):
        # create_shortcut()
        program_files = winshell.programs()
        target = f'{folder_to_track}{filename}'
        winshell.CreateShortcut(
          Path = os.path.join(folder_to_track, f'{filename}.lnk'),
          Target = f'{folder_to_track}/{filename}')
        
        # move_file()
        file_exists = os.path.isfile(f'{folder_destination}/{filename}')
        if file_exists:
          while file_exists:
            new_filename = f'({self.i}) - {filename}'
            self.i += 1
            file_exists = os.path.isfile(f'{folder_destination}/{new_filename}')
          os.rename(f'{folder_to_track}/{filename}', f'{folder_destination}/{new_filename}')
        else:
          os.rename(f'{folder_to_track}/{filename}', f'{folder_destination}/{filename}')


# folder_to_track = 'C:/Users/andre/Desktop'
# folder_destination = 'C:/Users/andre/OneDrive - Syddansk Erhvervsskole/MISC'
folder_to_track = 'C:/Users/andre/Desktop/test'
folder_destination = 'C:/Users/andre/Desktop/test2'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
  while True:
    time.sleep(10)
except KeyboardInterrupt:
  observer.stop()
observer.join()