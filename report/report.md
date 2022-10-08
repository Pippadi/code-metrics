# Code Metrics

## What it does

This program displays metrics for given files or folders.

```
~$ python3 code-metrics.py ../IRC/Bots/uptodatebot

*** ../IRC/Bots/uptodatebot/ ***
Contains 10 items

|    
|    *** ../IRC/Bots/uptodatebot/src ***
|    Contains 3 items
|    
|    |    
|    |    *** ../IRC/Bots/uptodatebot/src/configdef ***
|    |    Contains 1 items
|    |    
|    |    |    
|    |    |    --- ../IRC/Bots/uptodatebot/src/configdef/configdef.go ---
|    |    |    Type: ASCII text
|    |    |    Line count: 24
|    |    |    Size: 452.00 B
|    |    |    
|    |    
|    |    *** ../IRC/Bots/uptodatebot/src/utils ***
|    |    Contains 1 items
|    |    
|    |    |    
|    |    |    --- ../IRC/Bots/uptodatebot/src/utils/utils.go ---
|    |    |    Type: ASCII text
|    |    |    Line count: 30
|    |    |    Size: 464.00 B
|    |    |    
|    |    
|    |    *** ../IRC/Bots/uptodatebot/src/msgcache ***
|    |    Contains 1 items
|    |    
|    |    |    
|    |    |    --- ../IRC/Bots/uptodatebot/src/msgcache/msgcache.go ---
|    |    |    Type: ASCII text
|    |    |    Line count: 70
|    |    |    Size: 1.64 KiB
|    |    |    
|    
|    
|    --- ../IRC/Bots/uptodatebot/main.go ---
|    Type: Go source, ASCII text
|    Line count: 89
|    Size: 2.25 KiB
|    
|    
|    --- ../IRC/Bots/uptodatebot/Dockerfile ---
|    Type: ASCII text
|    Line count: 15
|    Size: 419.00 B
|    
|    
|    --- ../IRC/Bots/uptodatebot/uptodatebot ---
|    Type: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked
|    Size: 3.34 MiB
```

![Generated Graph](assets/MatplotlibGraph.png)

## Why we wanted to write this

Keeping track of files can be difficult. We wanted to make the task a little easier by adding graphics to help visualize folder structure and file size.

## How it works

The program gets the file/folder whose details are required from command line arguments given in `sys.argv`.

If the given entity is a file, its details are printed directly. If it is a folder, the program iterates through its contents recursively, displaying details for each entity within it.

File details are consolidated into a class, of which an instance can be created for each file in question.
The class abstracts out the actual file handling code from the rest of the program.

For determining file type, the [`python-magic`](https://pypi.org/project/python-magic/) library is used.
It provides a simple way to get the [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types).
Depending on whether the MIME type contains "text", the contents (as characters or raw bytes) are read to a buffer.
From there, metrics like line count (number of newline characters) or file size can be calculated.

If a directory is specified, the program also displays a graph of the number of lines of each of the top 10 longest files.
Graphing is done with the [`matplotlib`](https://matplotlib.org/) library.
To assemble the data required, a hash map (dictionary) is created with filenames as keys and their line counts as their values.
From there, the keys and values are taken into separate arrays, and sorted by line count.
Finally, the top 10 longest files are taken, and fed to `matplotlib` to plot.
