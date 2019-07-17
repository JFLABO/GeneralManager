from PyQt5 import QtWidgets, uic
 
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

class MyTableModel(QAbstractTableModel):
    def __init__(self, list, headers = [], parent = None):
        QAbstractTableModel.__init__(self, parent)
        self.list = list
        self.headers = headers

    def rowCount(self, parent):
        return len(self.list)

    def columnCount(self, parent):
        return len(self.list[0])

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role):
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            return self.list[row][column]

        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.list[row][column]
            return value

    def setData(self, index, value, role = Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            self.list[row][column] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:

            if orientation == Qt.Horizontal:

                if section < len(self.headers):
                    return self.headers[section]
                else:
                    return "not implemented"
            else:
                num=section+1
                return "No. %d" % num
def importData( data, root=None):
    model = QtGui.QStandardItemModel()
    model.setRowCount(0)
    if root is None:
        root = model.invisibleRootItem()
    seen = {}
    values = deque(data)
    print(data)
    while values:
        value = values.popleft()
        if value['level'] == 0:
            parent = root
        else:
            pid = value['parent_ID']
            if pid not in seen:
                values.append(value)
                continue
            parent = seen[pid]
        dbid = value['dbID']
        win.treeView.activated([
            QtGui.QStandardItem(value['short_name']),
            QtGui.QStandardItem(str(dbid)),
            ])
        seen[dbid] = parent.child(parent.rowCount() - 1)
        
def setTree01():
    data = [
    ("アクションメニュー", [
        ("カレンダー", []),
        ("優先順位ノート", [
            ("重要度順ノート", [])
            ])
        ]),
    ("マニュアル", [
        ("設定", [
            ("ノート", []),
            ("メール", [])
            ])
        ])
    ]
    
    model = QtGui.QStandardItemModel()
    model.setHorizontalHeaderLabels(['Name'])
    #win.treeView.header().setDefaultSectionSize(180)
    addItems(model, data)
    #win.treeView.setModel(model)
    #d=importData(data)
    #win.treeView.addItems(model, data)
    win.treeView.setModel(model)
    win.treeView.expandAll()
    
def setTree02():
    data = [
    ("解析速報", [
        ("緊急", []),
        ("重大", [
            ("未来につながる明るい話", [])
            ])
        ]),
    ("問題", [
        ("重要", [
            ("依頼", []),
            ("問い合わせ", [])
            ])
        ])
    ]
    
    model = QtGui.QStandardItemModel()
    model.setHorizontalHeaderLabels(['Name　(AI) AutoDetect'])
    #model.setHorizontalHeaderLabels(['Name', 'dbID'])
    #win.treeView.header().setDefaultSectionSize(180)
    addItems(model, data)
    #win.treeView.setModel(model)
    #d=importData(data)
    #win.treeView.addItems(model, data)
    win.treeView_2.setModel(model)
    win.treeView_2.expandAll()
    
def addItems( model, elements):

    for text, children in elements:
        item = QStandardItem(text)
        model.appendRow(item)
        if children:
           addItems(item, children)

def hello(thr_no):
  time.sleep(2.5)
  print(thr_no)

def setTree():
    l1 = QTreeWidgetItem(["S重要視すること", "安全性", "30万Node"])
    l2 = QTreeWidgetItem(["経費", "profit", "factor"])
    for i in range(3):
        l1_child = QTreeWidgetItem(["コンセプト" + str(i), "Child B" + str(i), "Child C" + str(i)])
        l1.addChild(l1_child)

    for j in range(2):
        l2_child = QTreeWidgetItem(["Child AA" + str(j), "Child BB" + str(j), "Child CC" + str(j)])
        l2.addChild(l2_child)
    tw=win.treeWidget
    #tw.resize(500, 200)
    tw.setColumnCount(3)
    tw.setHeaderLabels(["Column 1", "Column 2", "Column 3"])
    tw.addTopLevelItem(l1)
    tw.addTopLevelItem(l2)
    
def hello1():
    t = threading.Timer(1, hello1)
    t.start()
    dayarr=["月曜日","火曜日","水曜日","木曜日","金曜日","土曜日","月曜日"]
    now = datetime.datetime.now()
    str1=now.strftime("%Y/%m/%d")
    str2=now.strftime("%H:%M:%S")
    str3=dayarr[now.weekday()]
    #win.label.setText("Hello Japan.")
    win.label_2.setText(str1+str3+str2)
    #hello("hello1")

def hello2():
  while True:
    time.sleep(3)
    hello("hello2")
  
def setTable():
    headers = ["内容", "重要度", "優先度"]
    tableData0 = [
                 ['来年までにやりたいことについて話してみよう',100,200],
                 ['今日の予定を確認してみよう',130,260],
                 ['重要なことは何か整理してみよう',190,300],
                 ['必要なもの欲しいものの一覧を書いてみよう',700,500],
                 ['応答期限が迫っているイベントを確認しよう',700,500],
                 ['今やるべきことは何か整理しよう',700,500],
                 ['訓練　時間をかけて鍛えたい技能について',700,500],
                 ['いつかやりたいことを書いてみよう',800,900]
                 ]

    model = MyTableModel(tableData0, headers)
    win.tableView.setModel(model)
    header = win.tableView.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    win.tableView.resizeColumnToContents(1)
    win.tableView.resizeColumnToContents(2)
    
app = QtWidgets.QApplication([])
 
win = uic.loadUi("ui/ChiMeRa.ui") #specify the location of your .ui file
setTable()
win.resize(1024,700)
win.show()

setTree()
setTree01()
setTree02()

t1 = threading.Thread(target=hello1)
t1.start()
  
sys.exit(app.exec())

