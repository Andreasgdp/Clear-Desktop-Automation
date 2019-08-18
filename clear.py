import os
import winshell

# TODO make the program use some kind of observer like https://www.youtube.com/watch?v=qbW6FRbaSl0
# TODO make the program an executable that can be run without terminal as a backgroundprocess in windows (https://www.youtube.com/watch?v=lOIJIk_maO4)

directory = 'C:/Users/andre/Desktop/'

directory_move = 'C:/Users/andre/OneDrive - Syddansk Erhvervsskole/MISC/'


def create_shortcut(filename, dest):
  program_files = winshell.programs()
  target = f'{dest}{filename}'
  winshell.CreateShortcut(
    Path = os.path.join(dest, f'{filename}.lnk'),
    Target=f'{dest}{filename}')


def move_file(filename, start_dest, end_dest):
  counter = 1
  file_exists = os.path.isfile(f'{end_dest}{filename}')
  while file_exists:
    new_filename = f'({counter}) - {filename}'
    counter += 1
    file_exists = os.path.isfile(f'{end_dest}{new_filename}')
  os.rename(f'{start_dest}{filename}', f'{end_dest}{new_filename}')


for filename in os.listdir(directory):
  if filename == 'Games':
    continue
  if filename == 'desktop.ini':
    continue
  if filename.startswith('~'):
    continue
  if filename.startswith('.'):
    continue
  if not filename.endswith('.lnk'):
    create_shortcut(filename, directory)
    move_file(filename, directory, directory_move)