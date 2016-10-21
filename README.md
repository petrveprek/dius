# Welcome to *dius*

__*dius*__ -- **_di_**sk **_us_**age

# Usage

```
>dius.py --help
Disk Usage 1.4
usage: dius.py [-h] [-c COUNT] [-s] [-w <12,180>] [directory]

Prints `COUNT` largest directories found under top `directory`.

positional arguments:
  directory             set top directory to analyze
                        [C:\Users\Admin\Documents\GitHub\dius]

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        set number of largest directories to print [20]
  -s, --silent          suppress progress messages [false]
  -w <12,180>, --width <12,180>
                        set console width for progress indicator [180]
```

# Example

```
>dius.py \Windows -c 10
Disk Usage 1.4
Analyzing \Windows
Found 24,706 directories with 120,988 files in 37 seconds (667.7 directories/s, 3,269.9 files/s)
 1/24,706   8.9GiB \Windows\Installer
 2/24,706   2.1GiB \Windows\System32
 3/24,706   1.2GiB \Windows\SysWOW64
 4/24,706 498.5MiB \Windows\Installer\$PatchCache$\Managed\00004109D30000000000000000F01FEC\14.0.4763
 5/24,706 410.8MiB \Windows\System32\DriverStore\FileRepository\nvdmwu.inf_amd64_26aa6356770b2e86
 6/24,706 407.9MiB \Windows\System32\DriverStore\FileRepository\nvltwu.inf_amd64_7abb66182eb8ed83
 7/24,706 407.4MiB \Windows\System32\DriverStore\FileRepository\nvmiwu.inf_amd64_bd786fe53bff67f7
 8/24,706 406.3MiB \Windows\System32\DriverStore\FileRepository\nvamwu.inf_amd64_d4715679184092a8
 9/24,706 406.0MiB \Windows\System32\DriverStore\FileRepository\nvcvwu.inf_amd64_ed9974b2e149bbb9
10/24,706 405.7MiB \Windows\System32\DriverStore\FileRepository\nvblwu.inf_amd64_31f54e2d1ba058d5
    Other  34.0GiB
    Total  49.0GiB
```

Copyright (c) 2016 Petr Vepřek

MIT License, see [`LICENSE`](./LICENSE) for further details.
