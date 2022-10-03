import sys

if len(sys.argv) < 1: # Checks if filename is omitted
    print("Must provide filename!")
    exit() # Exits program

filename = sys.argv[1] # First command line argument

fh = open(filename, "r")
x = len(fh.readlines())
print(x)
fh.close()
import pathlib
file_extension = pathlib.Path(filename).suffix
print("File Extension: ", file_extension)
