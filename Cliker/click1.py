import sys
import pyautogui as auto
import keyboard as key

start_key = input( "Клавиша запуска: " )
stop_key = input( "Клавиша остановки: " )

while True:
    if key.is_pressed( start_key ):
        while True:
         auto.click(clicks=2, interval=0.25)
         if key.is_pressed( stop_key ):
           break
           break
           exit(0)
           sys.exit()


