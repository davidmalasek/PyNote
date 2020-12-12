def read(filename):
    with open(filename, encoding="utf-8") as document:
        lineArray = []
        for i in range(linecount(filename)):
            currentLine = document.readline()
            lineArray.append(currentLine.replace("\n", ""))
    return " ".join(lineArray)


def write(filename, textToWrite):
    with open(filename, "a", encoding="utf-8") as document:
        document.write(textToWrite)


def overwrite(filename, textToWrite):
    with open(filename, "w", encoding="utf-8") as document:
        document.write(textToWrite)


def linecount(filename):
    with open(filename, encoding="utf-8") as document:
        lineCount = 0
        for i in document:
            lineCount += 1
    return lineCount
