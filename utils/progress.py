import time


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
