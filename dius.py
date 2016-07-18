#!python3
# Copyright (c) 2016 Petr Veprek
"""Disk Usage"""

import math
import operator
import os
import string
import sys
import time

TITLE = "Disk Usage"
VERSION = "0.0.0"
VERBOSE = False
WIDTH = 80
COUNT = 20

def now(on="on", at="at"):
    return "{}{} {}{}".format(on + " " if on != "" else "", time.strftime("%Y-%m-%d"), at + " " if at != "" else "", time.strftime("%H:%M:%S"))

def neat(str, max):
    str = "".join([char if char in string.printable else "_" for char in str])
    if len(str) > max: str = str[:max-3] + "..."
    return str

def digits(num, min=0):
    return max(min, math.ceil(math.log10(num)))

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
        print("\rScanning {: <{}}".format(neat(path, WIDTH), WIDTH), end="")
        usage[path] = sum(map(os.path.getsize, filter(os.path.isfile, map(lambda file: os.path.join(path, file), files))))
    print("\r         {: <{}}\r".format("", WIDTH), end="")
    usage = sorted(usage.items(), key=operator.itemgetter(1), reverse=True)
    digsCount = digits(len(usage),2)
    total = sum(map(lambda pair: pair[1], usage))
    digsTotal = digits(total)
    for i, (path, size) in enumerate(usage[:COUNT]):
        print("{:{}}/{} {:{}} {}".format(i+1, digsCount, len(usage), size, digsTotal, path))
    if (COUNT < len(usage)):
        print("{:>{}} {:{}}".format("OTHER", 2*digsCount+1, sum(map(lambda pair: pair[1], usage[COUNT:])), digsTotal))
    print("{:>{}} {:{}}".format("TOTAL", 2*digsCount+1, total, digsTotal))
    
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
