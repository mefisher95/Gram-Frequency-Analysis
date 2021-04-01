import time
import math

def clear_screen():
    print('\033[2J\033[0;0H')

class ProgressTracker:
    def __init__(self, iterable, title):
        self.len = len(iterable)
        self.count = 0
        self.start = time.time()
        self.tite = title

    def update(self):
        self.count += 1
        elapsed = time.time() - self.start

        if (self.count >= self.len): 
            print()
            return

        hour = int(elapsed // 3600)
        elapsed %= 3600
        min = int(elapsed // 60)
        second = int(elapsed % 60)

        barlen = math.ceil(self.count / self.len * 20)
        bar = "=" * (barlen - 1) + ">" + " " * (20 - barlen)

        output = "{0}: {1:5.2f}% [{2}] Elapsed: {3:2}h {4:2}m {5:2}s".format(self.tite, self.count/self.len * 100, bar, hour, min, second)
        backspace = "\b" * len(output)
        output = backspace + output
        print(output, end='')