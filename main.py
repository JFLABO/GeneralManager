# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import signal
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from collections import deque
import datetime
import threading
import time
from lib import functions
 
app = QtWidgets.QApplication([])
 
win = uic.loadUi("ui/ChiMeRa.ui") #specify the location of your .ui file
win.resize(1024,700)
win.show()


functions.setTree(win)
functions.setTree01(win)
functions.setTree02(win)
functions.setTable(win)
#t1 = threading.Thread(target=functions.hello1(win))
#t1 = threading.Timer(1, functions.hello1(win))
#t1.start()

def scheduler():
    t = threading.Timer(1, scheduler)
    t.start()
    #print(time.time())
    functions.hello1(win)

t = threading.Thread(target = scheduler)
t.start()

sys.exit(app.exec())
