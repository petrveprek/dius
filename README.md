# Welcome to *dius*

__*dius*__ -- **_di_**sk **_us_**age

# Usage

```
>dius.py --help
Disk Usage 0.2
usage: dius.py [-h] [-c COUNT] [directory]

positional arguments:
  directory             top directory to analyze
                        [C:\Users\Admin\Documents\GitHub\dius]

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        number of largest directories to show [20]
```

# Example

```
>dius.py \Windows -c 10
Disk Usage 0.2
Analyzing \Windows
 1/24,644   8.5GiB \Windows\Installer
 2/24,644   2.0GiB \Windows\System32
 3/24,644   1.2GiB \Windows\SysWOW64
 4/24,644 498.5MiB \Windows\Installer\$PatchCache$\Managed\00004109D30000000000000000F01FEC\14.0.4763
 5/24,644 398.2MiB \Windows\Fonts
 6/24,644 365.6MiB \Windows\System32\DriverStore\FileRepository\nvlti.inf_amd64_338da84652515de3
 7/24,644 307.5MiB \Windows\System32\DriverStore\FileRepository\igdlh64.inf_amd64_41faaf35503f8252
 8/24,644 244.1MiB \Windows\System32\DriverStore\FileRepository\hdxrt.inf_amd64_951ddfb196f08e73
 9/24,644 214.2MiB \Windows\System32\DriverStore\FileRepository\hdxnecma.inf_amd64_7db117052649a003
10/24,644 212.4MiB \Windows\System32\DriverStore\FileRepository\hdxsgma4.inf_amd64_0db9f6ff73368555
    OTHER  20.1GiB
    TOTAL  34.0GiB
```

Copyright (c) 2016 Petr Vepřek

MIT License, see [`LICENSE`](./LICENSE) for further details.
