from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QTreeView, \
    QTableWidgetItem
# from PyQt5.QtGui import QStandardItemModel, QImage
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, Qt, QDate

from test import Ui_MainWindow
import sys
import sqlite3
import cv2
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")
# class sql(QWidget):
class test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.sqlConnect()
        # self.initUi()
        self.setupUi(self)
        self.run()
        self.show()

    # def initUi(self):
    #     self.setGeometry(300,300,500,520)
    #     self.setWindowTitle("test")
    #     self.show()

    def sqlConnect(self):
        try:
            self.conn = sqlite3.connect(db_path)

        except:
            print("잘묏된 방식입니다.")
            exit(1)
        print("연결 성공")
        self.cur = self.conn.cursor()

    def run(self):
        self.cmd="SELECT * FROM sqlite_master WHERE type='table';"
        self.cur.execute(self.cmd)
        self.conn.commit()
        print(self.cur.fetchall())
        # pass

    def closeEvent(self,QCloseEvent):
        self.conn.close()

    def startFound(self):
        print("main")
        self.today = QDate.currentDate()
        self.today_year = self.today.year()
        self.today_month = self.today.month()
        self.today_day = self.today.day()
        # print(type(self.today_year))
        # print(self.today_month)
        # print(self.today_day)

        self.cmd = "select chart_index,patient_name,patient_birth_info FROM patient_list where patient_visit_day = '{}.{}.{}'".format(self.today_year,self.today_month,self.today_day)
        self.cur.execute(self.cmd)
        self.conn.commit()
        ar = self.cur.fetchall()

        for i in range(len(ar)):
            self.info.removeRow(len(ar))
            self.info.removeRow(i)
            self.info.insertRow(i)
            self.info.setData(self.info.index(i, 0), ar[i][0])
            self.info.setData(self.info.index(i, 1), ar[i][1])
            self.info.setData(self.info.index(i, 2), ar[i][2])


    def find_patient_image_list(self):
        # self.info_image.modelReset()
        # self.info_image.resetInternalData()
        a = self.patient_list.currentIndex().row()
        # b = self.patient_list.currentIndex().column()
        print(self.info_image)

        self.cmd = "select * FROM patient_list"
        self.cur.execute(self.cmd)
        self.conn.commit()
        ar = self.cur.fetchall()

        # print(ar)
        print(ar[a][1])
        self.patient_name=ar[a][1]

        self.cmd = "select test_day,image_name,etc FROM patient_image where patient_name = '" +self.patient_name+ "'"
        self.cur.execute(self.cmd)
        self.conn.commit()
        ar = self.cur.fetchall()
        # print(ar)

        for i in range(len(ar)):
            self.info_image.removeRow(i)
            self.info_image.insertRow(i)
            self.info_image.setData(self.info_image.index(i, 0), ar[i][0])
            self.info_image.setData(self.info_image.index(i, 1), ar[i][1])
            self.info_image.setData(self.info_image.index(i, 2), ar[i][2])


    def show_patient_image(self):
        self.cmd = "select test_day,image_name,etc FROM patient_image where patient_name = '" + self.patient_name + "'"
        self.cur.execute(self.cmd)
        self.conn.commit()
        ar = self.cur.fetchall()

        a = self.patient_image.currentIndex().row()
        self.patient_image_file = ar[a][1]
        print(self.patient_image_file)

        qPixmapVar = QPixmap()
        qPixmapVar.load('C:/Users/user/Desktop/QT/image/' + self.patient_image_file + '.png')
        qPixmapVar= qPixmapVar.scaled(450, 450, QtCore.Qt.KeepAspectRatio)
        self.image_view.setPixmap(qPixmapVar)
        # self.patient_image = QImage('C:/Users/user/Downloads/' + self.patient_image_file + '.png')
        # if self.patient_image.isNull():
        #     print("Error loading image")
        #     sys.exit(1)
        # self.image_view.setPixmap(QtGui.QPixmap('C:/Users/user/Desktop/QT/image/'+self.patient_image_file+'.png'))

    def calendar_date(self):
        self.info.resetInternalData()
        self.select_day = self.calendarWidget.selectedDate()

        self.day_year = self.select_day.year()
        self.day_month = self.select_day.month()
        self.day_day = self.select_day.day()
        # print(type(self.day_year))
        # print(self.day_month)
        # print(self.day_day)

        self.cmd = "select chart_index,patient_name,patient_birth_info FROM patient_list where patient_visit_day = '{}.{}.{}'".format(
            self.day_year, self.day_month, self.day_day)
        self.cur.execute(self.cmd)
        self.conn.commit()
        ar = self.cur.fetchall()

        for i in range(len(ar)):
            self.info.removeRow(len(ar))
            self.info.removeRow(i)
            self.info.insertRow(i)
            self.info.setData(self.info.index(i, 0), ar[i][0])
            self.info.setData(self.info.index(i, 1), ar[i][1])
            self.info.setData(self.info.index(i, 2), ar[i][2])
        print(len(ar))









app = QApplication(sys.argv)
w = test()
# k = search()
sys.exit(app.exec_())









