import sys
import os
from file_details import FileDetails
import graphing
import users
import config

USAGE = """code-metrics <ACTION> [ARGS]...
    get <filename|dirname>...
    create-user
    delete-user
    list-users"""
INDENT_STRING = "|    "
CONFIG_PATH = os.path.expanduser("~/.code-metrics-rc")

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
    iprint(indent, "Contains", len(contents), "item" if len(contents) == 0 else "items")
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

if len(sys.argv) == 1: # Checks if action is omitted
    print("Must provide action!")
    print(USAGE)
    exit(1) # Exits program with error status (exit code 1)

if not config.exists_at(CONFIG_PATH):
    config.persist_to_file(config.read_from_user(), CONFIG_PATH)

cfg = config.read_from_file(CONFIG_PATH)

# The first command line argument
action = sys.argv[1]

# Optional arguments for the action
args = sys.argv[2:]

match action:
    case "get":
        username = input("Username: ")
        password = input("Password: ")
        if users.authorize(username, password, cfg):
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
        users.create(username, password, cfg)

    case "delete-user":
        username = input("Username: ")
        password = input("Password: ")
        if users.authorize(username, password, cfg):
            users.delete(username, cfg)
        else:
            print("Deletion failed.")

    case "list-users":
        for name in users.list(cfg):
            print(name)

    case "reconfigure":
        config.persist_to_file(config.read_from_user(), CONFIG_PATH)

    case other:
        print(USAGE)
