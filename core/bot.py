import threading
import time
from core.window_manager import WindowManager
from vision.capture import capture_window
from vision.matcher import TemplateMatcher
from input.controller import MovementController


class GrassBot:
    def __init__(self, log_callback=print):
        self.running = False
        self.log = log_callback

        self.window = WindowManager("Poke Nexus.exe")
        self.matcher = TemplateMatcher("assets/templates/")
        self.controller = MovementController()

    def start(self):
        self.running = True
        threading.Thread(target=self.run, daemon=True).start()

    def stop(self):
        self.running = False

    def run(self):
        hwnd = self.window.setup()

        if not hwnd:
            self.log("Game not found!")
            return

        self.log("Game ready. Starting detection...")

        while self.running:
            frame = capture_window(hwnd)
            points = self.matcher.find(frame)

            if points:
                target = points[0]
                self.controller.move_towards(target)
                self.log(f"Moving to {target}")

            time.sleep(0.1)