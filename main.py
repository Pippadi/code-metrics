import sys
import pathlib

USAGE = "code-metrics <filename|dirname>"

if len(sys.argv) < 1: # Checks if filename is omitted
    print("Must provide filename!")
    print(USAGE)
    exit(1) # Exits program with error status (exit code 1)
### Not tested on Windows

# First command line argument is assumed to be filename
filename = sys.argv[1]

fh = open(filename, "r")
x = len(fh.readlines())
print("Line Count:", x)
fh.close()

file_extension = pathlib.Path(filename).suffix
print("File Extension:", file_extension)
