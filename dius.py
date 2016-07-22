#!python3
# Copyright (c) 2016 Petr Veprek
"""Disk Usage"""

import enum, math, operator, os, string, sys, time

TITLE = "Disk Usage"
VERSION = "0.0.0"
VERBOSE = False
COUNT = 20
class Mode(enum.Enum): plain = 0; grouped = 1; gazillion = 2
MODE = Mode.plain
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
            return "{:5.{}f}{}{}".format(num, 1 if num % 1 > 0 else 0, unit, suffix)
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
    
    top = os.getcwd()
    print("Analyzing {}".format(top))
    usage = {}
    for path, dirs, files in os.walk(top):
        print("\rScanning {: <{}}".format(printable(path, WIDTH), WIDTH), end="")
        usage[path] = sum(map(os.path.getsize, filter(os.path.isfile, map(lambda file: os.path.join(path, file), files))))
    print("\r         {: <{}}\r".format("", WIDTH), end="")
    usage = sorted(usage.items(), key=operator.itemgetter(1), reverse=True)
    widthCount = places(len(usage), min=2)
    total = sum(map(lambda pair: pair[1], usage))
    widthTotal = places(total, mode=Mode.gazillion)
    for i, (path, size) in enumerate(usage[:COUNT]):
        print("{:{}}/{} {:>{}} {}".format(
            i+1, widthCount,
            len(usage),
            format(size, mode=Mode.gazillion), widthTotal,
            path))
    if (COUNT < len(usage)):
        print("{:>{}} {:>{}}".format(
            "OTHER", 2*widthCount+1,
            format(sum(map(lambda pair: pair[1], usage[COUNT:])), mode=Mode.gazillion), widthTotal))
    print("{:>{}} {:>{}}".format(
        "TOTAL", 2*widthCount+1,
        format(total, mode=Mode.gazillion), widthTotal))
    
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
