import sys
import os
from file_details import FileDetails

USAGE = "code-metrics <filename>"

def iprint(indentLevel, *args, **kwargs):
    print("|\t" * indentLevel, *args, **kwargs)

def presentFileDetails(filepath, indent=0):
    details = FileDetails(filepath)
    mimetype = details.mimeType()

    iprint(indent)
    iprint(indent, "---", filepath, "---")
    iprint(indent, "Type:", details.prettyType())

    if "text" in mimetype: # Checking whether file is text file or not
        iprint(indent, "Line count:", details.lineCount())
        iprint(indent, "Character count:", details.characterCount())
    else:
        iprint(indent, "Byte count:", details.byteCount())
    iprint(indent)

def presentDirectoryDetails(dirpath, indent=0):
    contents = os.listdir(dirpath)
    iprint(indent, "\n***", dirpath, "***")
    iprint(indent, "Contains", len(contents), "items")
    iprint(indent)
    for objname in contents:
        if objname[0] != ".": # Ignore hidden files (those starting with '.')
            # Recursively iprint details of directory contents
            presentObjectDetails(os.path.join(dirpath, objname), indent + 1)

def presentObjectDetails(path, indent=0):
    if os.path.isdir(path):
        presentDirectoryDetails(path, indent)
    else:
        presentFileDetails(path, indent)

if len(sys.argv) < 1: # Checks if filename is omitted
    print("Must provide file or directory path!")
    print(USAGE)
    exit(1) # Exits program with error status (exit code 1)
### Not tested on Windows ###

# First command line argument is assumed to be
# the object in question's path
objpath = sys.argv[1]

presentObjectDetails(objpath)
