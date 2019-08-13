# -*- coding: utf-8 -*-
import json
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

   
def addItems( model, elements):

    for text, children in elements:
        item = QStandardItem(text)
        model.appendRow(item)
        if children:
           addItems(item, children)

def hello(thr_no):
  time.sleep(2.5)
  print(thr_no)

def setTree(win):
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
    
def hello1(win):
  
    dayarr=["月曜日","火曜日","水曜日","木曜日","金曜日","土曜日","日曜日"]
    now = datetime.datetime.now()
    str1=now.strftime("%Y/%m/%d")
    str2=now.strftime("%H:%M:%S")
    str3=dayarr[now.weekday()]
    #win.label.setText("Hello Japan.")
    win.label_2.setText(str1+str3+str2)
    #hello("hello1")

    #目標時刻
    f = open('data/targetdate.json', 'r')
    jsonData = json.load(f)
    f.close()
    dt1 = datetime.datetime(int(jsonData["year"]), int(jsonData["month"]),int(jsonData["day"]),int(jsonData["hour"]))
    win.label.setText(jsonData["mes"])    
    #日カウント
    tdt=dt1-now
    #時間カウント
    str4=str(tdt)
    win.label_3.setText(str4)
    #t = threading.Timer(1, hello1(win))
    #t.start()

def hello2():
  while True:
    time.sleep(3)
    hello("hello2")
  
def setTable(win):
    headers = ["内容", "重要度", "優先度"]
    # ファイルをオープンする
    #test_data = open("data/tabledata.json", "r")
    # すべての内容を読み込む
    #contents = test_data.read()
    # ファイルをクローズする
    #test_data.close()
    f = open('data/tabledata.json', 'r')
    jsonData = json.load(f)
    f.close()
    #tableData0=contents
    tableData0=jsonData
    model = MyTableModel(tableData0,headers)
    win.tableView.setModel(model)	
    header = win.tableView.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    win.tableView.resizeColumnToContents(1)
    win.tableView.resizeColumnToContents(2)
    
           
def setTree01(win):
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
    
def setTree02(win):
    data = [
    ("解析速報", [
        ("緊急", []),
        ("重大", [
            ("Cellphone", [])
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
 
