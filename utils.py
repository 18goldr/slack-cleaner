# -*- coding: utf-8 -*-


class Colors():
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Counter():
    def __init__(self):
        self.total = 0

    def increase(self):
        self.total += 1
