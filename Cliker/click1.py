import pyautogui as auto
import keyboard as key

start_key = input( "Клавиша запуска: " )
stop_key = input( "Клавиша остановки: " )

while True:
   if key.is_pressed( start_key ):
     auto.tripleClick()

   if key.is_pressed( stop_key ):
       break;