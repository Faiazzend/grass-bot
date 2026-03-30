import pyautogui


class MovementController:
    def move_towards(self, target):
        tx, ty = target

        screen_x, screen_y = 512, 384  # center of 1024x768

        if tx > screen_x:
            pyautogui.press('d')
        else:
            pyautogui.press('a')

        if ty > screen_y:
            pyautogui.press('s')
        else:
            pyautogui.press('w')