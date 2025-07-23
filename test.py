import pyautogui
from pathlib import Path
def press_sign_button():
    pic_addr = str(Path(__file__).parent / 'login.png')
    #pic_addr = 'C:/Users/LENOVO/Desktop/crawl/login.png'
    loc = pyautogui.locateOnScreen(pic_addr)
    print(loc)
print(str(Path(__file__).parent / 'login.png'))
press_sign_button()