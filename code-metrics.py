import sys
import os
from file_details import FileDetails

USAGE = "code-metrics <filename>"

def presentFileDetails(file):
    details = FileDetails(file)
    print("MIME type:", file.mimeType())
    print("Line count:", file.lineCount())
    print("Character count:", file.characterCount())

if len(sys.argv) < 1: # Checks if filename is omitted
    print("Must provide file or directory path!")
    print(USAGE)
    exit(1) # Exits program with error status (exit code 1)
### Not tested on Windows

# First command line argument is assumed to be
# the object in question's path
objpath = sys.argv[1]

if os.is_file(objpath):
    presentFileDetails(objpath)
