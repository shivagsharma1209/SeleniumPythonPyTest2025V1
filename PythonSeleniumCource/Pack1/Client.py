import sys
sys.path.append("PythonSeleniumCource/Pack1/__init__.py")
#Approach 1
# import M1
# import M2
# M1.display1()
# M2.show1()

#Approach 2
# from M1 import display1
# from M2 import show1
# display1()
# show1()

#approach 3
from M1 import *
from M2 import *

display1()
display2()
show1()
show2()


