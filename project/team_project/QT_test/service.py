import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox

#이벤트 처리 함수
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic
from test import Ui_Form


class Exam(QWidget,Ui_Form):
    def __init__(self):
        #상위 객체 호출
        super().__init__()
        self.setupUi(self)
        self.show()
#모든 Qt5 어플은 아래 오브젝트를 생성해야함
# sys.argv : 파이선 셀스크립트에서 명령줄을 제어하는 부분
app = QApplication(sys.argv)
#객체 생성
w = Exam()

#정상 종료
#app.exec_() 이벤트 처리를 위한 루프실행, 루프실행이 끝나면 sys.exit(종료)가 실행
sys.exit(app.exec_()) 





# import sys

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox

# #이벤트 처리 함수
# from PyQt5.QtCore import QCoreApplication

# class Exam(QWidget):
#     def __init__(self):
#         #상위 객체 호출
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         btn = QPushButton('QUIT',self)
#         btn.resize(btn.sizeHint())
#         #마우스 갖다 대면 팁을 제공
#         btn.setToolTip('툴팁임')
#         btn.move(50,50)
#         #버튼이 클릭될 때 연결될 슬롯?
#         #instance().quit는 어플리케이션이 나가지는것, 프로그램 종료
#         btn.clicked.connect(QCoreApplication.instance().quit)


#         self.resize(500,500)
#         self.setWindowTitle('two')
#         self.show()

#     #종료하면 발생하는 이벤트
#     def closeEvent(self, QCloseEvent):
#         #print('asdasd')
#         ans = QMessageBox.question(self,'종료확인','종료하시겠습니까',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#         print(ans)
#         if ans == QMessageBox.Yes:
#             QCloseEvent.accept()
#         else:
#             QCloseEvent.ignore() 

# #모든 Qt5 어플은 아래 오브젝트를 생성해야함
# # sys.argv : 파이선 셀스크립트에서 명령줄을 제어하는 부분
# app = QApplication(sys.argv)
# #객체 생성
# w = Exam()

# #정상 종료
# #app.exec_() 이벤트 처리를 위한 루프실행, 루프실행이 끝나면 sys.exit(종료)가 실행
# sys.exit(app.exec_()) 
