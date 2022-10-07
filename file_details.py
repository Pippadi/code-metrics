import os
import math
import magic

_SUFFIXES = ["B", "KiB", "MiB", "GiB", "TiB"]

# A class to represent files, for which metrics can be accessed
class FileDetails:
    def __init__(self, path):
        self.path = path

        self.contents = ""
        mode = "r" if self.isText() else "rb"
        with open(self.path, mode) as f:
            self.contents = f.read()

    def lineCount(self):
        # Count of newlines = Count of lines
        # os.linesep is the default newline character sequence
        # for the host operating system
        # return self.contents.count(os.linesep)
        return self.contents.count(os.linesep)

    def byteCount(self):
        return len(self.contents)

    def prettySize(self):
        log1024 = math.floor(math.log(self.byteCount(), 1024)) if self.byteCount() else 0
        return "%.2f %s" % (self.byteCount() / ((1024 ** log1024) if log1024 else 1.0), _SUFFIXES[log1024])

    def prettyType(self):
        return magic.from_file(self.path)

    def mimeType(self):
        return magic.from_file(self.path, mime=True)

    def isText(self):
        return "text" in self.mimeType()

if __name__ == "__main__":
    f = FileDetails("./main.py")
    print(f.mimeType())
    print(f.lineCount())
    print(f.characterCount())
