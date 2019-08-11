import os
import winshell

directory = 'C:/Users/andre/Desktop/'

directory_move = 'C:/Users/andre/OneDrive - Syddansk Erhvervsskole/MISC/'


def create_shortcut(filename, dest):
  program_files = winshell.programs()
  target = f'{dest}{filename}'
  winshell.CreateShortcut(
    Path = os.path.join(dest, f'{filename}.lnk'),
    Target=f'{dest}{filename}')


def move_file(filename, start_dest, end_dest):
  # TODO check if file with same name exist and if ad a (n)-suffix to the filename
  os.rename(f"{start_dest}{filename}", f"{end_dest}{filename}")


for filename in os.listdir(directory):
  if filename == 'Games':
    continue
  if filename == 'desktop.ini':
    continue
  if filename.startswith('~'):
    continue
  if filename.startswith('.'):
    continue
  if not filename.endswith(".lnk"):
    create_shortcut(filename, directory)
    move_file(filename, directory, directory_move)