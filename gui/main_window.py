from core.bot import GrassBot

class MainWindow(QWidget):
    def __init__(self):
        ...
        self.bot = None

    def start_bot(self):
        self.log.append("Starting bot...")

        self.bot = GrassBot(log_callback=self.log.append)
        self.bot.start()

    def stop_bot(self):
        if self.bot:
            self.bot.stop()
            self.log.append("Bot stopped.")