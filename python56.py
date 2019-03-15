from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLineEdit,QTextEdit,QInputDialog,QLabel
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip,QPushButton,QMessageBox
import os
# from form import Ui_otherwindow
import sys
import sqlite3
import time
import random
# from python46 import TabbWidget
# import datetime
# import matplotlib.pyplot as plt
# from matplotlib import style
# style.use('fivethirtyeight')
conn=sqlite3.connect('sam1.db')
c=conn.cursor()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "SMART FARM DIARY"        
        self.top = 100        
        self.left = 100        
        self.width = 680        
        self.height = 500
        # registerButton=input("write register ")
        button=QPushButton("register",self)
        button.move(200,200)
        # signinButton=input("write signin")
        button2=QPushButton("signinButton",self)
        button2.move(300,200)
        button.clicked.connect(self.dynamic_data_entry)
        # self.lineEdit.clear()
        # self.lineEdit2.clear()
        button2.clicked.connect(self.read_from_db)
        # forgetPassword=input("write forget password")
        button3=QPushButton("forgetPassword",self)
        button3.move(220,250)
        button3.resize(150,40)
        button3.clicked.connect(self.click_button)

        # MainWindow=QtWidgets.QMainWindow()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("iron.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.lineEdit=QLineEdit(self)
        self.lineEdit.move(100,100)
        self.lineEdit.resize(280,40)
        self.lineEdit.setPlaceholderText("enter username")
        self.lineEdit2=QLineEdit(self)
        self.lineEdit2.move(100,300)
        self.lineEdit2.resize(280,40)
        MainWindow=QtWidgets.QMainWindow()
        self.lineEdit2.setPlaceholderText("enter password")
        self.lineEdit2.setEchoMode(QLineEdit.Password)
        self.label=QLabel("NOTE:-IF YOU FIRST TIME SIGN IN ANSWER THE SECURITY QUESTION IN FIFTH TAB",self)
        self.label.resize(500,30)
        self.label.move(20,400)
        self.show()
    def create_table():
        c.execute("CREATE TABLE IF NOT EXISTS stuffTooPlot(keyword TEXT, value BLOB)")

    def dynamic_data_entry(self):
      
        keyword=self.lineEdit.text()
        value=self.lineEdit2.text()
       
        c.execute("INSERT INTO stuffTooPlot(keyword,value) VALUES(?,?)",(keyword,value))
        conn.commit()
        self.lineEdit.clear()
        self.lineEdit2.clear()
        # c.close()
        # conn.close()
    def anotherWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=TabWidget
              
    def read_from_db(self):
        keyword=self.lineEdit.text()
        value=self.lineEdit2.text()
       
        a=("SELECT value  FROM stuffTooPlot WHERE keyword = ? AND value = ? ")
        c.execute(a,[(keyword),(value)])
        self.lineEdit.clear()
        self.lineEdit2.clear()
        data=c.fetchall()
        if data:
            for i in data:
                from python44 import Window
                # from form import Ui_otherwindow
                # from python58 import TabbWidget2
               
        else:
            QMessageBox.information(self,"game","excess denied",QMessageBox.Ok,QMessageBox.Ok)

    def click_button(self):
        text,ok=QInputDialog.getText(self,"input id","what is your favourite book?")
       
        if ok:
            key=text
            a=("SELECT key  FROM app11 WHERE key = ? ")
            c.execute(a,[(key)])
            data=c.fetchall()
            if data:
                for text in data:
                    c.execute("SELECT keyword,value FROM stuffTooPlot LIMIT 1")
                    data2=c.fetchall()
                    for i in data2:
                        # print(i)
                        QMessageBox.information(self,"game",f"username and password is {i}",QMessageBox.Ok,QMessageBox.Ok)
            else:
                QMessageBox.information(self,"game","better luck next time",QMessageBox.Ok,QMessageBox.Ok)
        else:

            QMessageBox.information(self,"game","you dont have any username and password",QMessageBox.Ok,QMessageBox.Ok)              
    create_table()
# from python46 import TabbWidget    
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
