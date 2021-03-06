#!python3
# Copyright (c) 2016 Petr Veprek
"""Disk Usage"""

import argparse, colorama, enum, math, os, string, sys, time

TITLE = "Disk Usage"
VERSION = "1.4"
VERBOSE = False
COUNT = 20
class Mode(enum.Enum): plain = 0; grouped = 1; gazillion = 2
MODE = Mode.gazillion
MIN_WIDTH = 9+0+3 # intro + directory + ellipsis
MAX_WIDTH = os.get_terminal_size().columns if sys.stdout.isatty() else 80
WIDTH = MAX_WIDTH
WIDTH = min(max(WIDTH, MIN_WIDTH), MAX_WIDTH)

def now(on="on", at="at"):
    return "{}{} {}{}".format(
        on + " " if on != "" else "", time.strftime("%Y-%m-%d"),
        at + " " if at != "" else "", time.strftime("%H:%M:%S"))

def printable(str, max):
    str = "".join([char if char in string.printable else "?" for char in str])
    if len(str) > max: str = str[:max-3] + "..."
    return str

def plain(num):
    return "{}".format(num)

def grouped(num):
    return "{:,}".format(num)

def gazillion(num, suffix="B"):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if num < 1024.0:
            return "{:.{}f}{}{}".format(num, 1 if num % 1 > 0 else 0, unit, suffix)
        num /= 1024.0
    return "{:.{}f}{}{}".format(num, 1 if num % 1 > 0 else 0, 'Yi', suffix)

def format(num, mode=Mode.plain):
    return(
        grouped(num)   if mode == Mode.grouped   else
        gazillion(num) if mode == Mode.gazillion else
        plain(num))

def places(num, min=0, mode=Mode.plain):
    return max(min, len(format(num, mode)))

def main():
    colorama.init()
    print("{} {}".format(TITLE, VERSION))
    if VERBOSE:
        print("\a", end="")
        print("Python {}".format(sys.version))
        print("Command '{}'".format(sys.argv[0]))
        print("Arguments {}".format(sys.argv[1:]))
        print("Executed {}".format(now()))
        start = time.time()
    
    parser = argparse.ArgumentParser(description="Prints `COUNT` largest directories found under top `directory`.")
    parser.add_argument("directory", nargs="?", help="set top directory to analyze [%(default)s]", default=os.getcwd())
    parser.add_argument("-c", "--count", help="set number of largest directories to print [%(default)s]", type=int, default=COUNT)
    parser.add_argument("-s", "--silent", help="suppress progress messages [false]", action = "store_true", default=False)
    parser.add_argument("-w", "--width", help="set console width for progress indicator [%(default)s]", metavar="<{},{}>".format(MIN_WIDTH,MAX_WIDTH), type=int, choices=range(MIN_WIDTH,MAX_WIDTH+1), default=WIDTH)
    arguments = parser.parse_args()
    directory = arguments.directory
    count = arguments.count
    silent = arguments.silent
    width = arguments.width
    
    if not silent:
        print("Analyzing {}".format(directory))
        BACKTRACK = ("\r" if width < MAX_WIDTH else "\033[A") if sys.stdout.isatty() else "\n"
    started = time.time()
    usage = {}
    numFiles = 0
    for path, dirs, files in os.walk(directory):
        if not silent:
            print("Scanning {: <{}}".format(printable(path, width-9), width-9), end=BACKTRACK)
        files = list(filter(os.path.isfile, map(lambda file: os.path.join(path, file), files)))
        numFiles += len(files)
        usage[path] = sum(map(os.path.getsize, files))
    if not silent:
        print("         {: <{}}".format("", width-9), end=BACKTRACK)
        seconds = max(1, round(time.time() - started))
        dirRate = round(len(usage) / seconds, 1)
        fileRate = round(numFiles / seconds, 1)
        print("Found {} director{} with {} file{} in {} second{} ({} director{}/s, {} file{}/s)".format(
            grouped(len(usage)), "y" if len(usage) == 1 else "ies",
            grouped(numFiles),   ""  if numFiles == 1   else "s",
            grouped(seconds),    ""  if seconds == 1    else "s",
            grouped(dirRate),    "y" if dirRate == 1    else "ies",
            grouped(fileRate),   ""  if fileRate == 1   else "s"))
    
    usage = sorted(usage.items(), key=lambda item:(-item[1], item[0]))
    widthCount = places(len(usage), min=2, mode=Mode.grouped)
    widthIndex = places(count, min=5-1-widthCount, mode=Mode.grouped)
    other = sum(map(lambda pair: pair[1], usage[count:]))
    total = sum(map(lambda pair: pair[1], usage))
    widthSize = max(
        max(map(lambda pair: places(pair[1], mode=MODE), usage[:count])),
        places(other, mode=MODE),
        places(total, mode=MODE))
    for i, (path, size) in enumerate(usage[:count]):
        print("{:>{}}/{} {:>{}} {}".format(grouped(i+1), widthIndex, grouped(len(usage)), format(size, mode=MODE), widthSize, path))
    if (count < len(usage)):
        print("{:>{}} {:>{}}".format("Other", widthIndex+1+widthCount, format(other, mode=MODE), widthSize))
    print("{:>{}} {:>{}}".format("Total", widthIndex+1+widthCount, format(total, mode=MODE), widthSize))
    
    if VERBOSE:
        elapsed = time.time() - start
        seconds = round(elapsed)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        weeks, days = divmod(days, 7)
        print("Completed {}".format(now()))
        print("Elapsed {:d}w {:d}d {:d}h {:d}m {:d}s ({:,.3f}s)".format(weeks, days, hours, minutes, seconds, elapsed))
    print("\a", end="")

if '__main__' == __name__:
    main()
