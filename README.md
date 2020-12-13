# PyNote

PyNote is a simple Python module that makes it easier to write or read from a TXT or JSON files.

---

## Functions

|  Name   |    Return    | Description                                                                                                             |
| :-----: | :----------: | ----------------------------------------------------------------------------------------------------------------------- |
| `read`  | `str`/`dict` | Returns a `str` or `dict` in UTF-8 depending on a file type.                                                            |
| `write` |      -       | Writes to a TXT or JSON file in UTF-8. This function can also be used to overwrite a document (**TXT documents only**). |
| `count` |    `int`     | Returns number of lines or items depending on a file type.                                                              |

---

## Read

|  Argument  | Optional | Description           |
| :--------: | :------: | --------------------- |
| `fileName` |    No    | File path + File name |

### Example

```python
import pynote

# Create dictionary from JSON file
jsonDictionary = pynote.read("folder/test.json")

# Print value of the key "name"
print(jsonDictionary["name"])
>>> "Juan"

print(pynote.read("folder/test.txt"))
>>> "I love PyNote!"
```

---

## Write

|  Argument   | Optional | Description                                                                                                      |
| :---------: | :------: | ---------------------------------------------------------------------------------------------------------------- |
| `fileName`  |    No    | File path + File name                                                                                            |
|  `content`  |    No    | Content (`str`/`dict`), that will be added to the file.                                                          |
| `overWrite` |   Yes    | By default is set to `False`. When `True`, function will overwrite the entire document (**TXT documents only**). |

### Example

```python
import pynote

# Update value of the key "name" + Add a new item
pynote.write("folder/test.json", {"name": "Harold", "age": 25})

# Write a meaningful message
pynote.write("folder/test.txt", "I ain't never seen two pretty best friends.")

# Erase an entire document with overWrite set to True
pynote.write("folder/test.txt", "", True)
```

When reading a JSON file, you can simply work with the result as with a Python dictionary. Every change will be updated through the `content` argument.

---

## Count

|  Argument  | Optional | Description           |
| :--------: | :------: | --------------------- |
| `fileName` |    No    | File path + File name |

### Example

```python
import pynote

# Count number of lines in a TXT document
txtLines = pynote.count("folder/test.txt")
print(txtLines + 69)
>>> 420

# Count number of items in a root position in a JSON document
print(pynote.count("folder/test.json"))
>>> 3
```

---

## License

Licensed under the [MIT License](LICENSE).
