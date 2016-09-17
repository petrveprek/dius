# Welcome to *dius*

__*dius*__ -- **_di_**sk **_us_**age

# Usage

```
>dius.py --help
Disk Usage 1.3
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
Disk Usage 1.3
Analyzing \Windows
Found 26,038 directories with 131,556 files in 93 seconds (280.0 directories/s, 1,414.6 files/s)
 1/26,038   8.8GiB \Windows\Installer
 2/26,038   2.0GiB \Windows\System32
 3/26,038   1.2GiB \Windows\SysWOW64
 4/26,038 498.5MiB \Windows\Installer\$PatchCache$\Managed\00004109D30000000000000000F01FEC\14.0.4763
 5/26,038 398.2MiB \Windows\Fonts
 6/26,038 365.6MiB \Windows\System32\DriverStore\FileRepository\nvlti.inf_amd64_338da84652515de3
 7/26,038 307.5MiB \Windows\System32\DriverStore\FileRepository\igdlh64.inf_amd64_41faaf35503f8252
 8/26,038 244.1MiB \Windows\System32\DriverStore\FileRepository\hdxrt.inf_amd64_951ddfb196f08e73
 9/26,038 214.2MiB \Windows\System32\DriverStore\FileRepository\hdxnecma.inf_amd64_7db117052649a003
10/26,038 212.4MiB \Windows\System32\DriverStore\FileRepository\hdxsgma4.inf_amd64_0db9f6ff73368555
    Other  20.1GiB
    Total  34.4GiB
```

Copyright (c) 2016 Petr Vepřek

MIT License, see [`LICENSE`](./LICENSE) for further details.
