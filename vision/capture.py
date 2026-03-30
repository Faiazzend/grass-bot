import mss
import numpy as np
import win32gui


def capture_window(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x1, y1, x2, y2 = rect

    with mss.mss() as sct:
        monitor = {
            "top": y1,
            "left": x1,
            "width": x2 - x1,
            "height": y2 - y1
        }

        img = np.array(sct.grab(monitor))
        return img