import eel
import pyautogui
from time import sleep
from threading import Thread


def config():
    try:
        sleep(1)
        pyautogui.moveTo(1721, 43)
        sleep(0.1)
        pyautogui.rightClick()
        sleep(0.1)
        pyautogui.moveTo(1721, 135)
        sleep(0.1)
        pyautogui.leftClick()

        sleep(0.1)
        pyautogui.moveTo(1400, 190)
        sleep(0.1)
        pyautogui.leftClick()
        sleep(0.1)

        pyautogui.moveTo(1721, 43)
        sleep(0.1)
        pyautogui.rightClick()
        sleep(0.1)
        pyautogui.moveTo(1721, 135)
        sleep(0.1)
        pyautogui.leftClick()
        sleep(0.1)
        pyautogui.moveTo(1400, 290)
        sleep(0.1)
        pyautogui.leftClick()
        return 0
    except Exception as e:
        print(e)
        return 1


def gui():
    eel.init('web')
    eel.start('main.html', size=(350, 350), position=(1540, 30))


def main():
    th_1, th_2 = Thread(target=config), Thread(target=gui)
    th_1.start(), th_2.start()
    th_1.join(), th_2.join()


if __name__ == '__main__':
    main()
