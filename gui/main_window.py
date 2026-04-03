from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout
from core.bot import GrassBot

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # UI Elements
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.start_btn = QPushButton("Start Bot")
        self.stop_btn = QPushButton("Stop Bot")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.log)
        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        self.setLayout(layout)

        # Bot
        self.bot = None

        # Connect buttons
        self.start_btn.clicked.connect(self.start_bot)
        self.stop_btn.clicked.connect(self.stop_bot)

    def start_bot(self):
        self.log.append("Starting bot...")
        self.bot = GrassBot(log_callback=self.log.append)
        self.bot.start()

    def stop_bot(self):
        if self.bot:
            self.bot.stop()
            self.log.append("Bot stopped.")