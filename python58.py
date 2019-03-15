from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLineEdit,QTextEdit,QDialog,QDialogButtonBox,QGroupBox,QCheckBox,QComboBox,QListWidget,QTabWidget,QLabel,QInputDialog,QMessageBox
import os
import sys
import datetime
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QDialogButtonBox,QTabWidget,QVBoxLayout,QWidget
# import sys
from PyQt5.QtGui import QIcon
import sqlite3
conn=sqlite3.connect('sam1.db')
c=conn.cursor()

class TabbWidget(QDialog):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("window")  
        self.setWindowTitle("SMART FARM DIARY")
        self.setWindowIcon(QIcon("iron.png"))
        self.resize(600, 400)
        tabwidget=QTabWidget()
        tabwidget.addTab(FirstTab(),"Total budget")
        vbox=QVBoxLayout()
        vbox.addWidget(tabwidget)
        self.setLayout(vbox) 
        tabwidget.addTab(SecondTab(),"Daily Expenses")
        tabwidget.addTab(ThirdTab(),"Total Expenditure")
        tabwidget.addTab(FourthTab(),"Initial Budget")
        tabwidget.addTab(FifthTab(),"miscellaneous")
        tabwidget.addTab(sixthTab(),"laon section")
     
        # button.clicked.connect(self.onclick)
class sixthTab(QWidget):
    def __init__(self):
        super().__init__()
        layout=QVBoxLayout()
        label=QLabel("THERE ARE SOME LINKS FROM WHICH WE CAN GET LOAN---->")
        # label=QLabel("কিছু লিঙ্ক আছে যা থেকে আপনি ঋণ পেতে পারেন---->")
        layout.addWidget(label)
        Button=QPushButton("NABARD",self)
        Button.clicked.connect(self.button)
        layout.addWidget(Button)
        button2=QPushButton("PAISABAZAR",self)
        button2.clicked.connect(self.button2)
        layout.addWidget(button2)
        button3=QPushButton("STATE BANK OF INDIA",self)
        button3.clicked.connect(self.button3)
        layout.addWidget(button3)
        button4=QPushButton("ICICI",self)
        button4.clicked.connect(self.button4)
        layout.addWidget(button4)
        button5=QPushButton("PUNJAB NATIONAL BANK",self)
        button5.clicked.connect(self.button5)
        layout.addWidget(button5)
        self.setLayout(layout)
    def button(self):
        webbrowser.open_new_tab("https://www.nabard.org/interestrate.aspx?cid=502&id=24") 
    def button2(self):
        webbrowser.open_new_tab("https://www.paisabazaar.com/personal-loan/agriculture-loan-interest-rates/?%7D?utm_title=Personalloan_seopage&utm_source=google&utm_medium=ppc0paisabazaar&utm_term=&utm_campaign=PL_DSA_Top_City-Top00PL_seo_page&utm_title=Personalloan_seopage&utm_source=google&utm_medium=ppc0paisabazaar&utm_term=&utm_campaign=PL_DSA_Top_City00PL_Main_Page&gclid=Cj0KCQiApvbhBRDXARIsALnNoK2xHR39l2odXXcuJq6THY3vHOLqNv-CRsVxSdKjbB76-A9wE8-RegUaAjKxEALw_wcB")       
    def button3(self):
        webbrowser.open_new_tab("https://www.sbi.co.in/portal/web/agriculture-banking")
    def button4(self):
        webbrowser.open_new_tab("https://www.icicibank.com/rural/loans/farmer-finance/index.page")
    def button5(self):
        webbrowser.open_new_tab("https://www.pnbindia.in/agriculture-credit-schemes.html")        
class FirstTab(QWidget):
    def __init__(self):
        super().__init__()
        layout=QVBoxLayout()

        budget=QLabel("TOTAL BUDGET")
        # budgetEdit=QLineEdit()
        self.budgetEdit=QLineEdit(self)
        
        # budgetEdit.setText(total)
        layout.addWidget(budget)
        # layout.addWidget(a)
        layout.addWidget(self.budgetEdit)
        button = QPushButton("ADD TOTAL BUDGET",self)
        button.clicked.connect(self.buttonclick)
        button.setToolTip("CLICK TO ADD TOTAL BUDGET")
        layout.addWidget(button)
        # budgetEdit.resize(200,30)
        dob=QLabel('SEED')
        self.dobEdit=QLineEdit(self)
        # layout=QVBoxLayout()
        layout.addWidget(dob)
        layout.addWidget(self.dobEdit)
       
        age=QLabel('FERTILIZER')
        # age.te
        self.ageEdit=QLineEdit()
        layout.addWidget(age)
        layout.addWidget(self.ageEdit)
        
        phone=QLabel('PESTICIDES')
        self.phoneEdit=QLineEdit()
        layout.addWidget(phone)
        layout.addWidget(self.phoneEdit)
    
        labour=QLabel('LABOUR')
        self.labourEdit=QLineEdit(self)
        layout.addWidget(labour)
        layout.addWidget(self.labourEdit)
        # 
        machine=QLabel('MACHINERY CHARGES')
        self.machineEdit=QLineEdit(self)
        layout.addWidget(machine)
        layout.addWidget(self.machineEdit)
       
        electric=QLabel('ELECTRICITY BILLS')
        self.electricEdit=QLineEdit(self)
        layout.addWidget(electric)
        layout.addWidget(self.electricEdit)
      
        others=QLabel('OTHERS')
        self.othersEdit=QLineEdit(self)
        layout.addWidget(others)
        layout.addWidget(self.othersEdit)
        button8 = QPushButton("ADD BUDGET",self)
        button8.setToolTip("CLICK TO ADD")
        button8.clicked.connect(self.button2click)
        # button.clicked.connect(self.button8click)
        layout.addWidget(button8)
        self.setLayout(layout)
       
    def create_table1():
        c.execute("CREATE TABLE IF NOT EXISTS app9(seed REAL,fertilizer REAL,pesticide REAL,labour REAL,machineryCharges REAL,electricityBills REAL,others REAL,key TEXT)")
    def create_table2():
        c.execute("CREATE TABLE IF NOT EXISTS app12 (total REAL,key TEXT)")  

   
    def buttonclick(self):
        textValue=self.budgetEdit.text()
        totall=textValue
        key="python"

        c.execute("INSERT INTO app12 (total,key) VALUES(?,?)",(totall,key))
        conn.commit()
        self.budgetEdit.clear()
        # c.close()
        # conn.close()

    def button2click(self):
        textValue=self.dobEdit.text()
        seed=textValue
        textValue2=self.ageEdit.text()
        fertilizer=textValue2
        textValue3=self.phoneEdit.text()
        pesticide=textValue3
        textValue4=self.labourEdit.text()
        labour=textValue4
        textValue5=self.machineEdit.text()
        machine=textValue5
        textValue6=self.electricEdit.text()
        electric=textValue6
        textValue7=self.othersEdit.text()
        others=textValue7
        key="python"

        c.execute("INSERT INTO app9 (seed ,fertilizer ,pesticide ,labour ,machineryCharges ,electricityBills ,others,key ) VALUES(?,?,?,?,?,?,?,?)",(seed,fertilizer,pesticide,labour,machine,electric,others,key))
        conn.commit()
        self.dobEdit.clear()
        self.ageEdit.clear()
        self.phoneEdit.clear()
        self.labourEdit.clear()
        self.machineEdit.clear()
        self.electricEdit.clear()
        self.othersEdit.clear()
   
    #     conn.close()                            
    create_table1()
    create_table2()
    # dynamic_data_entry('self')
class SecondTab(QWidget):
    def __init__(self):
        super().__init__()
        layout=QVBoxLayout()
        dob=QLabel('SEED')
        self.dobEdit=QLineEdit(self)
        # layout=QVBoxLayout()
        layout.addWidget(dob)
        layout.addWidget(self.dobEdit)
     
        age=QLabel('FERTILIZER')
        self.ageEdit=QLineEdit()
        layout.addWidget(age)
        layout.addWidget(self.ageEdit)
     
        phone=QLabel('PESTICIDES')
        self.phoneEdit=QLineEdit()
        layout.addWidget(phone)
        layout.addWidget(self.phoneEdit)
       
        labour=QLabel('LABOUR')
        self.labourEdit=QLineEdit(self)
        layout.addWidget(labour)
        layout.addWidget(self.labourEdit)
       
        machine=QLabel('MACHINERY CHARGES')
        self.machineEdit=QLineEdit(self)
        layout.addWidget(machine)
        layout.addWidget(self.machineEdit)
      
        electric=QLabel('ELECTRICITY BILLS')
        self.electricEdit=QLineEdit(self)
        layout.addWidget(electric)
        layout.addWidget(self.electricEdit)
       
        others=QLabel('OTHERS')
        self.othersEdit=QLineEdit(self)
        layout.addWidget(others)
        layout.addWidget(self.othersEdit)
        button8 = QPushButton("ADD TODAY SPEND MONEY",self)
        button8.setToolTip("CLICK TO ADD")
        button8.clicked.connect(self.button3click)
        # button.clicked.connect(self.button8click)
        layout.addWidget(button8)
        self.setLayout(layout)
    def create_table1():
        c.execute("CREATE TABLE IF NOT EXISTS app10 (date TEXT,seed REAL ,fertilizer REAL ,pesticide REAL ,labour REAL ,machineryCharges REAL ,electricityBills REAL ,others REAL ,key TEXT)")  
    def button3click(self):
        textValue=self.dobEdit.text()
        seed=textValue
        textValue2=self.ageEdit.text()
        fertilizer=textValue2
        textValue3=self.phoneEdit.text()
        pesticide=textValue3
        textValue4=self.labourEdit.text()
        labour=textValue4
        textValue5=self.machineEdit.text()
        machine=textValue5
        textValue6=self.electricEdit.text()
        electric=textValue6
        textValue7=self.othersEdit.text()
        others=textValue7
        key="python"
        unix=time.time()
        date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

        c.execute("INSERT INTO app10 (date,seed ,fertilizer ,pesticide ,labour ,machineryCharges ,electricityBills ,others,key ) VALUES(?,?,?,?,?,?,?,?,?)",(date,seed,fertilizer,pesticide,labour,machine,electric,others,key))
        conn.commit()
        self.dobEdit.clear()
        self.ageEdit.clear()
        self.phoneEdit.clear()
        self.labourEdit.clear()
        self.machineEdit.clear()
        self.electricEdit.clear()
        self.othersEdit.clear()
   
        
        # c.close()
        # conn.close()   
    create_table1()       

class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()
        layout=QVBoxLayout()
        budget=QLabel("TOTAL BUDGET")
        # budgetEdit=QLineEdit()
        self.budgetEdit=QLineEdit(self)
        
        # budgetEdit.setText(total)
        layout.addWidget(budget)
        # layout.addWidget(a)
        layout.addWidget(self.budgetEdit)
        button = QPushButton("MY TOTAL BUDGET",self)
        button.clicked.connect(self.buttonclick)
        button.setToolTip("CLICK TO ADD TOTAL BUDGET")
        layout.addWidget(button)
        # budgetEdit.resize(200,30)
        dob=QLabel('SEED')
        self.dobEdit=QLineEdit(self)
        # layout=QVBoxLayout()
        layout.addWidget(dob)
        layout.addWidget(self.dobEdit)
        button2 = QPushButton("TOTAL SPEND ON SEED",self)
        button2.setToolTip("CLICK TO ADD ")
        button2.clicked.connect(self.button2click)
        layout.addWidget(button2)
        age=QLabel('FERTILIZER')
        self.ageEdit=QLineEdit()
        layout.addWidget(age)
        layout.addWidget(self.ageEdit)
        button3 = QPushButton("TOTAL SPEND ON FERTILIZER",self)
        button3.setToolTip("CLICK TO ADD")
        button3.clicked.connect(self.button3click)
        layout.addWidget(button3)
        phone=QLabel('PESTICIDES')
        self.phoneEdit=QLineEdit()
        layout.addWidget(phone)
        layout.addWidget(self.phoneEdit)
        button4 = QPushButton("TOTAL SPEND ON PESTICIDES",self)
        button4.setToolTip("CLICK TO ADD")
        button4.clicked.connect(self.button4click)
        layout.addWidget(button4)
        labour=QLabel('LABOUR')
        self.labourEdit=QLineEdit(self)
        layout.addWidget(labour)
        layout.addWidget(self.labourEdit)
        button5 = QPushButton("TOTAL SPEND ON LABOUR",self)
        button5.setToolTip("CLICK TO ADD")
        button5.clicked.connect(self.button5click)
        layout.addWidget(button5)
        machine=QLabel('MACHINERY CHARGES')
        self.machineEdit=QLineEdit(self)
        layout.addWidget(machine)
        layout.addWidget(self.machineEdit)
        button6 = QPushButton("TOTAL SPEND ON MACHINERY CHARGES",self)
        button6.setToolTip("CLICK TO ADD")
        button6.clicked.connect(self.button6click)
        layout.addWidget(button6)
        electric=QLabel('ELECTRICITY BILLS')
        self.electricEdit=QLineEdit(self)
        layout.addWidget(electric)
        layout.addWidget(self.electricEdit)
        button7 = QPushButton("TOTAL SPEND ON ELECTRICITY BILLS",self)
        button7.setToolTip("CLICK TO ADD")
        button7.clicked.connect(self.button7click)
        layout.addWidget(button7)
        others=QLabel('OTHERS')
        self.othersEdit=QLineEdit(self)
        layout.addWidget(others)
        layout.addWidget(self.othersEdit)
        button8 = QPushButton("TOTAL SPEND ON OTHERS",self)
        button8.setToolTip("CLICK TO ADD")
        # button8.clicked.connect(self.button2click)
        button8.clicked.connect(self.button8click)
        layout.addWidget(button8)
        self.setLayout(layout)

    def buttonclick(self):
        c.execute("SELECT total FROM app12 ")
        data=c.fetchall()
        a=[sum(x) for x in zip(*data)]
        self.budgetEdit.setText(str(a))

    def button2click(self):
        c.execute("SELECT seed FROM app10 ")
        # c.execute("UPDATE app10 SET seed=0 WHERE seed     ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.dobEdit.setText(str(a))

    def button3click(self):
        c.execute("SELECT fertilizer FROM app10 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.ageEdit.setText(str(a))    
    
    def button4click(self):
        c.execute("SELECT pesticide FROM app10 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.phoneEdit.setText(str(a))

    def button5click(self):
        c.execute("SELECT labour FROM app10 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.labourEdit.setText(str(a))  

    def button6click(self):
        c.execute("SELECT machineryCharges FROM app10 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.machineEdit.setText(str(a)) 

    def button7click(self):
        c.execute("SELECT electricityBills FROM app10 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.electricEdit.setText(str(a))  

    def button8click(self):
        c.execute("SELECT others FROM app10 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.othersEdit.setText(str(a))  

class FourthTab(QWidget):
    def __init__(self):
        super().__init__()    

        layout=QVBoxLayout()
        dob=QLabel('SEED')
        self.dobEdit=QLineEdit(self)
        # layout=QVBoxLayout()
        layout.addWidget(dob)
        layout.addWidget(self.dobEdit)
        button2 = QPushButton("TOTAL BUDGET ON SEED",self)
        button2.setToolTip("CLICK TO ADD ")
        button2.clicked.connect(self.button2click)
        layout.addWidget(button2)
        age=QLabel('FERTILIZER')
        self.ageEdit=QLineEdit()
        layout.addWidget(age)
        layout.addWidget(self.ageEdit)
        button3 = QPushButton("TOTAL BUDGET ON FERTILIZER",self)
        button3.setToolTip("CLICK TO ADD")
        button3.clicked.connect(self.button3click)
        layout.addWidget(button3)
        phone=QLabel('PESTICIDES')
        self.phoneEdit=QLineEdit()
        layout.addWidget(phone)
        layout.addWidget(self.phoneEdit)
        button4 = QPushButton("TOTAL BUDGET ON PESTICIDES",self)
        button4.setToolTip("CLICK TO ADD")
        button4.clicked.connect(self.button4click)
        layout.addWidget(button4)
        labour=QLabel('LABOUR')
        self.labourEdit=QLineEdit(self)
        layout.addWidget(labour)
        layout.addWidget(self.labourEdit)
        button5 = QPushButton("TOTAL BUDGET ON LABOUR",self)
        button5.setToolTip("CLICK TO ADD")
        button5.clicked.connect(self.button5click)
        layout.addWidget(button5)
        machine=QLabel('MACHINERY CHARGES')
        self.machineEdit=QLineEdit(self)
        layout.addWidget(machine)
        layout.addWidget(self.machineEdit)
        button6 = QPushButton("TOTAL BUDGET ON MACHINERY CHARGES",self)
        button6.setToolTip("CLICK TO ADD")
        button6.clicked.connect(self.button6click)
        layout.addWidget(button6)
        electric=QLabel('ELECTRICITY BILLS')
        self.electricEdit=QLineEdit(self)
        layout.addWidget(electric)
        layout.addWidget(self.electricEdit)
        button7 = QPushButton("TOTAL BUDGET ON ELECTRICITY BILLS",self)
        button7.setToolTip("CLICK TO ADD")
        button7.clicked.connect(self.button7click)
        layout.addWidget(button7)
        others=QLabel('OTHERS')
        self.othersEdit=QLineEdit(self)
        layout.addWidget(others)
        layout.addWidget(self.othersEdit)
        button8 = QPushButton("TOTAL BUDGET ON OTHERS",self)
        button8.setToolTip("CLICK TO ADD")
        # button8.clicked.connect(self.button2click)
        button8.clicked.connect(self.button8click)
        layout.addWidget(button8)
        self.setLayout(layout)           

    def button2click(self):
        c.execute("SELECT seed FROM app9 ")
        # c.execute("SELECT seed FROM app10 ")
        data2=c.fetchall()
        # data3=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        # b=[sum(x) for x in zip(*data3)]
        self.dobEdit.setText(str(a))
        # self.dobEdit.setText(float(str(a))-float(str(b)))
        # self.dobEdit.setText(str(float(a))-float(b))
        # self.dobEdit.setText(float(tuple(a-b)))

    def button3click(self):
        c.execute("SELECT fertilizer FROM app9 ")
        
        data2=c.fetchall()
        
        a=[sum(x) for x in zip(*data2)]
       
        self.ageEdit.setText(str(a))


        # c.execute("SELECT seed FROM app10 ")
        # c.execute("UPDATE app10 SET seed=0 WHERE seed     ")
        # data3=c.fetchall()
        # b=[sum(x) for x in zip(*data3)]
        # self.dobEdit.setText(str(b))    
    
    def button4click(self):
        c.execute("SELECT pesticide FROM app9 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.phoneEdit.setText(str(a))

    def button5click(self):
        c.execute("SELECT labour FROM app9 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.labourEdit.setText(str(a))  

    def button6click(self):
        c.execute("SELECT machineryCharges FROM app9 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.machineEdit.setText(str(a)) 

    def button7click(self):
        c.execute("SELECT electricityBills FROM app9 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.electricEdit.setText(str(a))  

    def button8click(self):
        c.execute("SELECT others FROM app9 ")
        data2=c.fetchall()
        a=[sum(x) for x in zip(*data2)]
        self.othersEdit.setText(str(a))  

class FifthTab(QWidget):
    def __init__(self):
        super().__init__()
        layout=QVBoxLayout()
        button=QPushButton("SECURITY QUESTION")
        button.setToolTip("SECURITY QUESTION")
        button.clicked.connect(self.button1click)
        layout.addWidget(button)
        button2 = QPushButton("ERASE TOTAL BUDGET",self)
        button2.setToolTip("CLICK TO ADD ")
        button2.clicked.connect(self.button2click)
        layout.addWidget(button2)
        button3 = QPushButton("ERASE TOTAL BUDGET OF ALL",self)
        button3.setToolTip("CLICK TO ADD ")
        button3.clicked.connect(self.button3click)
        layout.addWidget(button3)
        button4 = QPushButton("ERASE SPEND ON ALL",self)
        button4.setToolTip("CLICK TO ADD ")
        button4.clicked.connect(self.button4click)
        layout.addWidget(button4)
        # self.lineEdit=QLineEdit(self)
        # layout.addWidget   
        button5=QPushButton("DATA COLLECTION DATE")
        button5.setToolTip("DATA COLLECTION DATE FROM--TO")
        button5.clicked.connect(self.button5click)
        layout.addWidget(button5)
        self.label=QLabel(self)

        layout.addWidget(self.label)
        self.setLayout(layout)

    def create_table5():
        c.execute("CREATE TABLE IF NOT EXISTS app11 (key TEXT)")  
    

    def button1click(self):
        
        text,ok=QInputDialog.getText(self,"input answer","what is your favourite book?")
        if ok:
            key=text
            c.execute("INSERT INTO app11 (key) VALUES(?)",(key,))
            conn.commit()
            QMessageBox.about(self,"security answer","saved")
        else:
            QMessageBox.about(self,"security answer","If already answered then ignore")

    create_table5()

    def button2click(self):
        c.execute("DELETE  FROM app12 WHERE key= 'python' ")
        conn.commit()  

    def button3click(self):
        c.execute("DELETE  FROM app9 WHERE key= 'python' ")
        conn.commit()

    def button4click(self):
        c.execute("DELETE  FROM app10 WHERE key= 'python' ")
        conn.commit()                       
    def button5click(self):
        c.execute("SELECT date FROM app10 ")
        data2=c.fetchone()
        # for i in data2:
            # print(i)
        data=c.fetchall()
        a=data.pop()
        for i in a:
            # self.label.setText(str(i))
            for l in data2:
                self.label.setText(f" {str(l)} to  {str(i)} ")

App = QApplication(sys.argv)
tabbWidget = TabbWidget()
tabbWidget.show()
App.exec()
# App.exec_()
# App.exit()
# sys.exit(App.exec())
