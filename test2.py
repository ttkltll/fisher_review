import math


def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def print_lyrics():
    print("I'm␣a␣lumberjack,␣and␣I'm␣okay.")
    print("I␣sleep␣all␣night␣and␣I␣work␣all␣day.")

repeat_lyrics()


def compare(x, y):
    if x > y:
        return 1
    elif x ==y:
        return 0
    else:
        return -1

compare(3, 4)


def distance(x1, y1, x2, y2):
    dx = x2 -x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

