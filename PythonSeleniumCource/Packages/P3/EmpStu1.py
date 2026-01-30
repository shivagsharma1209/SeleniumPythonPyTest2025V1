import sys

from PythonSeleniumCource.Day7.Constructor import Employee

sys.path.append('PythonSeleniumCource/Packages/P1/Emp1.py')
sys.path.append('PythonSeleniumCource/Packages/P2/Student1.py')

from Emp1 import *

empobj = Employee()
empobj.displayemployee(10,'aaa',20000)











