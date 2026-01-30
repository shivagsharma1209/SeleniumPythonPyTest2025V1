import sys
from tkinter.messagebox import showerror

from PythonSeleniumCource.Day10.Package1.Module1 import display

sys.path.append("PythonSeleniumCource/Day10/Package1/__init__.py")

import Module1
import Module2
Module1.display()
Module2.show()

