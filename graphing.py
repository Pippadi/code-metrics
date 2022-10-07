from file_details import FileDetails
import matplotlib.pyplot as plt
import os

def plotByLineCount(directory):
    lineCountMap = assembleLineCountMap(directory)
    sizes = list(lineCountMap.values())
    files = [os.path.basename(name) for name in lineCountMap.keys()]
    files, sizes = sortOneByTheOther(files, sizes)
    files = files[-10:] # Limiting sizes so that the graph isn't too big
    sizes = sizes[-10:]
    plt.xlabel("Line Count")
    plt.ylabel("File")
    bars = plt.barh(files, sizes)
    plt.bar_label(bars)
    plt.show()

def sortOneByTheOther(one, theOther):
    for i in range(1, len(theOther)):
        j = 0
        while j != i and theOther[i] > theOther[j]:
            j += 1
        one.insert(j, one[i])
        theOther.insert(j, theOther[i])
        del one[i+1]
        del theOther[i+1]
    return one, theOther

def assembleLineCountMap(objpath):
    lineCounts = {}
    for child in [c for c in os.listdir(objpath) if c[0] != "."]:
        childpath = os.path.join(objpath, child)
        if os.path.isfile(childpath):
            d = FileDetails(childpath)
            if d.isText():
                lineCounts[child] = d.lineCount()
        else:
            lineCounts.update(assembleLineCountMap(childpath))
    return lineCounts
