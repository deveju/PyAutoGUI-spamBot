import pyautogui as gui
import time

msg = input("Type your message: ") 
nTimes = input("How many times will the message be displayed? ")

time.sleep(2) # Time for the code to start running after you type the n°ofTimes(in seconds)

for i in range(int(nTimes)):
    gui.typewrite(msg);
    gui.press("Enter");
