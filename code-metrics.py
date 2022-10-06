import sys
import os
from file_details import FileDetails

USAGE = "code-metrics <filename|dirname>..."
INDENT_STRING = "|    "

# prints INDENT_STRING replicated indentLevel times
# followed by the other arguments passed
def iprint(indentLevel, *args, **kwargs):
    print(INDENT_STRING * indentLevel, end="")
    print(*args, **kwargs)

def presentFileDetails(filepath, indent=0):
    details = FileDetails(filepath)

    iprint(indent)
    iprint(indent, "---", filepath, "---")
    iprint(indent, "Type:", details.prettyType())

    if details.isText(): # Checking whether file is text file or not
        iprint(indent, "Line count:", details.lineCount())
    iprint(indent, "Size:", details.prettySize())
    iprint(indent)

def presentDirectoryDetails(dirpath, indent=0):
    contents = os.listdir(dirpath)
    iprint(indent)
    iprint(indent, "***", dirpath, "***")
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

# Command line arguments have the paths to each
# object whose details are to be printed
objpaths = sys.argv[1:]

for p in objpaths:
    presentObjectDetails(p)
