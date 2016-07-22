#!python3
# Copyright (c) 2016 Petr Veprek
"""Disk Usage"""

import argparse, enum, math, operator, os, string, sys, time

TITLE = "Disk Usage"
VERSION = "0.0.0"
VERBOSE = False
COUNT = 20
class Mode(enum.Enum): plain = 0; grouped = 1; gazillion = 2
MODE = Mode.gazillion
WIDTH = 80

def now(on="on", at="at"):
    return "{}{} {}{}".format(
        on + " " if on != "" else "", time.strftime("%Y-%m-%d"),
        at + " " if at != "" else "", time.strftime("%H:%M:%S"))

def printable(str, max):
    str = "".join([char if char in string.printable else "_" for char in str])
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
    print("{} {}".format(TITLE, VERSION))
    if VERBOSE:
        print("\a", end="")
        print("Python {}".format(sys.version))
        print("Command '{}'".format(sys.argv[0]))
        print("Arguments {}".format(sys.argv[1:]))
        print("Executed {}".format(now()))
        start = time.time()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs="?", help="top directory to analyze [%(default)s]", default=os.getcwd())
    parser.add_argument("-c", "--count", help="number of largest directories to show [%(default)s]", type=int, default=COUNT)
    arguments = parser.parse_args()
    directory = arguments.directory
    count = arguments.count
    
    print("Analyzing {}".format(directory))
    usage = {}
    for path, dirs, files in os.walk(directory):
        print("\rScanning {: <{}}".format(printable(path, WIDTH), WIDTH), end="")
        usage[path] = sum(map(os.path.getsize, filter(os.path.isfile, map(lambda file: os.path.join(path, file), files))))
    print("\r         {: <{}}\r".format("", WIDTH), end="")
    
    usage = sorted(usage.items(), key=operator.itemgetter(1), reverse=True)
    widthCount = places(len(usage), min=2)
    widthIndex = places(min(count,len(usage)), min=5-1-widthCount)
    other = sum(map(lambda pair: pair[1], usage[count:]))
    total = sum(map(lambda pair: pair[1], usage))
    widthSize = max(
        max(map(lambda pair: places(pair[1], mode=MODE), usage[:count])),
        places(other, mode=MODE),
        places(total, mode=MODE))
    for i, (path, size) in enumerate(usage[:count]):
        print("{:{}}/{} {:>{}} {}".format(i+1, widthIndex, len(usage), format(size, mode=MODE), widthSize, path))
    if (count < len(usage)):
        print("{:>{}} {:>{}}".format("OTHER", widthIndex+1+widthCount, format(other, mode=MODE), widthSize))
    print("{:>{}} {:>{}}".format("TOTAL", widthIndex+1+widthCount, format(total, mode=MODE), widthSize))
    
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
