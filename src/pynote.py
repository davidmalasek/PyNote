import json

def read(fileName):
    with open(fileName, encoding="utf-8") as document:
        if fileName.lower().endswith(".json"):
            return json.load(document)
        elif fileName.lower().endswith(".txt"):
            lineArray = []
            for i in range(count(fileName)):
                currentLine = document.readline()
                lineArray.append(currentLine.replace("\n", ""))
            return " ".join(lineArray)

def write(fileName, content, overWrite = False):
    if type(content) is str:
        if (overWrite):
            with open(fileName, "w", encoding="utf-8") as document:
                document.write(content)
        else:
            with open(fileName, "a", encoding="utf-8") as document:
                document.write(content)
    elif type(content) is dict:
        jsonLoaded = read(fileName)
        jsonLoaded.update(content)

        with open(fileName, "w", encoding="utf-8") as jsonDocument:
            json.dump(jsonLoaded, jsonDocument, ensure_ascii=False)

def count(fileName):
    with open(fileName, encoding="utf-8") as document:
        if fileName.lower().endswith(".json"):
            return len(json.load(document))
        elif fileName.lower().endswith(".txt"):
            lineCount = 0
            for i in document:
                lineCount += 1
            return lineCount