import mss
from PIL import Image
import pyautogui
import time

time.sleep(1)

def main():
    clicks = 0
    current_square = 0

    start_time = time.time()

    with mss.mss() as mss_instance:
        while time.time() - start_time < 65:
            if clicks < 1:
                current_square = 2
            elif clicks < 2:
                current_square = 3
            elif clicks < 3:
                current_square = 4
            elif clicks < 5:
                current_square = 5
            elif clicks < 7:
                current_square = 6
            elif clicks < 10:
                current_square = 7
            elif clicks < 16:
                current_square = 8
            else:
                current_square = 9

            row, column = 0, 0

            monitor_1 = {"top": 403, "left": 652, "width": 494, "height": 494}
            screenshot = mss_instance.grab(monitor_1)

            img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")

            array_ = []

            for j in range(9):
                for i in range(9):
                    x = int(494 / current_square + (988 / current_square * i))
                    y = int(494 / current_square + (988 / current_square * j))
                    array_.append(tuple(img.getpixel((x, y))))

            new_set = set(array_)

            for val in new_set:
                if array_.count(val) == 1:
                    index_ = array_.index(val)
                    column = index_ % current_square + 1
                    row = index_ // current_square + 1
                    print(row, column)

            screen_x = monitor_1["left"] + column * 494 / current_square - 247 / current_square
            screen_y = monitor_1["top"] + row * 494 / current_square - 247 / current_square

            pyautogui.moveTo(screen_x, screen_y, duration=0)
            pyautogui.click()

            clicks += 1

if __name__ == "__main__":
    main()
