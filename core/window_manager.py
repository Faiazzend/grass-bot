import psutil
import win32gui
import win32process
import win32con


class WindowManager:
    def __init__(self, process_name):
        self.process_name = process_name
        self.hwnd = None

    def get_pid(self):
        for proc in psutil.process_iter(['pid', 'name']):
            if self.process_name.lower() in proc.info['name'].lower():
                return proc.info['pid']
        return None

    def get_hwnd(self, pid):
        def callback(hwnd, hwnds):
            _, p = win32process.GetWindowThreadProcessId(hwnd)
            if p == pid and win32gui.IsWindowVisible(hwnd):
                hwnds.append(hwnd)

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        return hwnds[0] if hwnds else None

    def setup(self):
        pid = self.get_pid()
        if not pid:
            return None

        hwnd = self.get_hwnd(pid)
        if not hwnd:
            return None

        win32gui.ShowWindow(hwnd, 5)
        win32gui.SetForegroundWindow(hwnd)

        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 1024, 768, 0)

        self.hwnd = hwnd
        return hwnd