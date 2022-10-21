import sys
import os
from file_details import FileDetails
import graphing
import users

USAGE = """code-metrics <ACTION> [ARGS]...
    get <filename|dirname>...
    create-user
    delete-user"""
INDENT_STRING = "|    "

# prints INDENT_STRING replicated indentLevel times
# followed by the other arguments passed
def iprint(indentLevel, *args, **kwargs):
    print(INDENT_STRING * indentLevel, end="")
    print(*args, **kwargs)

def printFileDetails(filepath, indent=0):
    details = FileDetails(filepath)

    iprint(indent)
    iprint(indent, "---", filepath, "---")
    iprint(indent, "Type:", details.prettyType())

    if details.isText():
        iprint(indent, "Line count:", details.lineCount())
    iprint(indent, "Size:", details.prettySize())
    iprint(indent)

def printDirectoryDetails(dirpath, indent=0):
    contents = os.listdir(dirpath)
    iprint(indent)
    iprint(indent, "***", dirpath, "***")
    iprint(indent, "Contains", len(contents), "items")
    iprint(indent)
    for objname in contents:
        if objname[0] != ".": # Ignore hidden files (those starting with '.')
            # Recursively iprint details of directory contents
            printObjectDetails(os.path.join(dirpath, objname), indent + 1)

def printObjectDetails(path, indent=0):
    if os.path.isdir(path):
        printDirectoryDetails(path, indent)
        if indent == 0:
            graphing.plotByLineCount(path)
    else:
        printFileDetails(path, indent)

if len(sys.argv) == 1: # Checks if filename is omitted
    print("Must provide file or directory path!")
    print(USAGE)
    exit(1) # Exits program with error status (exit code 1)
### Not tested on Windows ###

# Command line arguments have the paths to each
# object whose details are to be printed

action = sys.argv[1]
args = sys.argv[2:]

match action:
    case "get":
        username = input("Username: ")
        password = input("Password: ")
        if users.authorization(username, password):
            for p in args:
                printObjectDetails(p)
        else:
            print("Authentication failed.")

    case "create-user":
        username = ""
        password = None
        while username == "" or len(username) > 20:
            print("Username must be at least 1 character long, but no more than 20.")
            username = input("Enter a username: ")
            print()
        while password == None or len(password) > 20:
            print("Password must be no more than 20 characters long.")
            password = input("Enter a password: ")
            print()
        users.createuser(username, password)

    case "delete-user":
        username = input("Username: ")
        password = input("Password: ")
        if users.authorization(username, password):
            users.deleteuser(username)
        else:
            print("Deletion failed.")

    case other:
        print(USAGE)
