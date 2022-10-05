import sys
import os
from file_details import FileDetails

USAGE = "code-metrics <filename>"

def presentFileDetails(filepath):
    details = FileDetails(filepath)
    mimetype = details.mimeType()

    print("\n---", filepath, "---")
    print("Type:", details.prettyType())

    if "text" in mimetype:
        print("Line count:", details.lineCount())
        print("Character count:", details.characterCount())
    else:
        print("Byte count:", details.byteCount())
    print()

def presentDirectoryDetails(dirpath):
    contents = os.listdir(dirpath)
    print("\n***", dirpath, "***")
    print("Contains", len(contents), "items")
    print()
    for objname in contents:
        if objname[0] != ".": # Ignore hidden files (those starting with '.')
            presentObjectDetails(os.path.join(dirpath, objname))

def presentObjectDetails(path):
    if os.path.isdir(path):
        presentDirectoryDetails(path)
    else:
        presentFileDetails(path)

if len(sys.argv) < 1: # Checks if filename is omitted
    print("Must provide file or directory path!")
    print(USAGE)
    exit(1) # Exits program with error status (exit code 1)
### Not tested on Windows

# First command line argument is assumed to be
# the object in question's path
objpath = sys.argv[1]

presentObjectDetails(objpath)
