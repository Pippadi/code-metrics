import os
import magic

# A class to represent files, for which metrics can be accessed
class FileDetails:
    def __init__(self, path):
        self.path = path

        self.contents = ""
        mode = "r" if "text" in self.mimeType() else "rb"
        with open(self.path, mode) as f:
            self.contents = f.read()

    def lineCount(self):
        # Count of newlines = Count of lines
        # os.linesep is the default newline character sequence
        # for the host operating system
        # return self.contents.count(os.linesep)
        return self.contents.count(os.linesep)

    def characterCount(self):
        return len(self.contents)

    def byteCount(self):
        return len(self.contents)

    def prettyType(self):
        return magic.from_file(self.path)

    def mimeType(self):
        return magic.from_file(self.path, mime=True)

if __name__ == "__main__":
    f = FileDetails("./main.py")
    print(f.mimeType())
    print(f.lineCount())
    print(f.characterCount())
