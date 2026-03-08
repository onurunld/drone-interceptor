from datetime import datetime

class Logger:
    def __init__(self, filepath="logs.txt"):
        self.filepath = filepath

    def log(self, x, y, status):
        with open(self.filepath, "a") as f:
            f.write(f"{datetime.now()} | Drone({x}, {y}) | {status}\n ")


