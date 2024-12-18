import sys
from pathlib import Path
from tkinter import filedialog as fd
sys.path.insert(1, str(Path(__file__).resolve().parent.parent) + "\\src")
import bineasy
file = fd.askopenfilename()
fileread = bineasy.readfrom.file(file)
print("File read Using module: " + fileread.readbits(0, 32).ConvertToStr())
with open(file, "rb") as f:
    bytes = f.read()
print("File read not using module: " + str(bytes[0:4], "UTF-8"))
if str(bytes[0:4], "UTF-8") == fileread.readbits(0, 32).ConvertToStr():
    print("Test 1 Passed")
