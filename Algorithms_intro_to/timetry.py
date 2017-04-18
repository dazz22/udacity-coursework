import signal
import time


def foo(num):
    for a in range(num):
        print("Tick")
        time.sleep(1)


def timeout_handler(signum, frame):
    print("took too long")
    raise

signal.signal(signal.SIGALRM, timeout_handler)

signal.alarm(3)
factor = 0 * .25 + .25
links = 0
for n in range(256):
    links = links + n * factor

print(factor)
print(links)
signal.alarm(0)
