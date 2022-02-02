import random


def get_usage():
    lines = open('useragents.txt').read().splitlines()
    usage = random.choice(lines)
    return usage

