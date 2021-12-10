import keyboard
from time import sleep
from functools import cache


REPLACE_MAP = {
    '@': 'shift+2',
    '#': 'shift+3',
}


@cache
def sanitize_chr(ch: str):
    if ch.isupper():
        ch = f"shift+{ch}"
    elif x := REPLACE_MAP.get(ch):
        ch = x

    return ch


def send():
    sleep(0.5)
    keyboard.press_and_release("enter")
    sleep(0.5)
    keyboard.press_and_release("enter")


print("Waiting for 3 seconds...")
sleep(3)

while True:
    print("Collecting")
    for c in map(sanitize_chr, "/collect"):
        keyboard.press_and_release(c)
    send()

    print("Waiting...")
    sleep(2)

    print("Throwing")
    for c in map(sanitize_chr, "/throw"):
        keyboard.press_and_release(c)
    sleep(0.5)
    keyboard.press_and_release("enter")
    for c in map(sanitize_chr, "@Loo"):
        keyboard.press_and_release(c)
    send()

    print("Waiting...")
    sleep(31)
