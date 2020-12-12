# PyNote

PyNote is a Python module that makes it easier to write or read from a text document.

---

Start by importing the module.
```python
import pynote
```

Prepare your `.txt` document. Don't forget to provide path to the file, if it's not existing in the same directory.
```python
import pynote

txtDocument = "mydocument.txt"
otherDocument = "myfolder/otherdocument.txt"

```
PyNote has currently available **4 functions**:
* `pynote.read()`
* `pynote.write()`
* `pynote.overwrite()`
* `pynote.linecount()`

---

## Read

Returns entire document as a string.

```python
import pynote

txtDocument = "mydocument.txt"

print(pynote.read(txtDocument))
```

## Write

Appends text to the document. Function will create a new file if the specified file does not exist.

```python
import pynote

txtDocument = "mydocument.txt"
textToWrite = "I love PyNote!"

pynote.write(txtDocument, textToWrite)

# Append to the new line:
pynote.write(txtDocument, "\n" + textToWrite)
```

## Overwrite

Overwrites the entire document. Function will create a new file if the specified file does not exist.

```python
import pynote

txtDocument = "mydocument.txt"
textToOverWrite = "Yeet :)"

pynote.overwrite(txtDocument, textToOverWrite)
```

You can also use this function as a eraser.

```python
import pynote

txtDocument = "mydocument.txt"

pynote.overwrite(txtDocument, "")
```

## Line Count

Returns number of lines in a document as a integer.

```python
import pynote

txtDocument = "mydocument.txt"

print(pynote.linecount(txtDocument))
```

---

## Notes

* PyNote use **UTF-8** encoding. 
* Every function will close after it's done.

---

## Coming soon

* Supporting Python dictionaries, JSON files

---

## License

Copyright (c) 2020 David Malášek
Licensed under the [MIT License](LICENSE).