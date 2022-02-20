import time


class Thermometer:
    symbols = ['\\', '|', '/', '-']

    def __init__(self, max):
        self.max = float(max)

    def display(self, index):
        percent = int(float(index) / self.max * 100.0)
        j = int(percent / 10)
        dots = "." * (10-j)
        hash = "#" * j
        print("%s%s% d%%" % (hash, dots, percent), end="\r")


class Spinner:
    symbols = ['\\', '|', '/', '-']

    def __init__(self, delta):
        self.delta = delta

    def display(self, index):
        i = int(index / self.delta) % 4
        print(self.symbols[i], end="\r")


if __name__ == "__main__":
    s = Spinner(1)
    for i in range(100):
        s.display(i)
        time.sleep(1)
