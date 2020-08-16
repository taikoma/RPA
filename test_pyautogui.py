import pyautogui as pg
import subprocess
import time
import win32gui

#subprocess.Popen("C:/Program Files/Blender Foundation/Blender/blender.exe")
#subprocess.Popen('C:/Windows/notepad.exe')

hWnd = win32gui.FindWindow("GHOST_WindowClass",None)
if hWnd is not 0:
  win32gui.SetForegroundWindow(hWnd)

time.sleep(5)
#pg.press('enter')

pg.screenshot('screenshot.png')

