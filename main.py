from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from form import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    
  

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.clickevent(self)
        self.ui.animation(self)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)# tắt nút maxsize
        self.result = 0 ##khai báo hai biến thành viên lưu kết quả và biểu thức
        self.exp = "" 
############################################################
#
#  Xử lý sự kiện nhập từ bàn phím
#
############################################################
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_1:
            self.ui.label.setText(self.ui.label.text()+"1")
        elif event.key() == QtCore.Qt.Key_2:
            self.ui.label.setText(self.ui.label.text()+"2")
        elif event.key() == QtCore.Qt.Key_3:
            self.ui.label.setText(self.ui.label.text()+"3")
        elif event.key() == QtCore.Qt.Key_4:
            self.ui.label.setText(self.ui.label.text()+"4")
        elif event.key() == QtCore.Qt.Key_5:
            self.ui.label.setText(self.ui.label.text()+"5")
        elif event.key() == QtCore.Qt.Key_6:
            self.ui.label.setText(self.ui.label.text()+"6")
        elif event.key() == QtCore.Qt.Key_7:
            self.ui.label.setText(self.ui.label.text()+"7")
        elif event.key() == QtCore.Qt.Key_8:
            self.ui.label.setText(self.ui.label.text()+"8")
        elif event.key() == QtCore.Qt.Key_9:
            self.ui.label.setText(self.ui.label.text()+"9")
        elif event.key() == QtCore.Qt.Key_0:
            self.ui.label.setText(self.ui.label.text()+"0")
        elif event.key() == QtCore.Qt.Key_Equal:
             self.ui.skpbang()
        elif event.key() == QtCore.Qt.Key_Return:
             self.ui.skpbang()
        elif event.key() == QtCore.Qt.Key_X:
            self.ui.label.setText(self.ui.label.text()+"x")
        elif event.key() == QtCore.Qt.Key_Asterisk:
            self.ui.label.setText(self.ui.label.text()+"*")
        elif event.key() == QtCore.Qt.Key_Slash:
            self.ui.label.setText(self.ui.label.text()+"/")
        elif event.key() == QtCore.Qt.Key_Minus:
            self.ui.label.setText(self.ui.label.text()+"-")
        elif event.key() == QtCore.Qt.Key_Plus:
            self.ui.label.setText(self.ui.label.text()+"+")
        elif event.key() == QtCore.Qt.Key_Backspace:
            self.ui.skpdel()
        elif event.key() == QtCore.Qt.Key_Delete:
            self.ui.skpac()
        elif event.key() == QtCore.Qt.Key_Exclam:
            self.ui.label.setText(self.ui.label.text() + "!")
        elif event.key() == QtCore.Qt.Key_ParenLeft:
            self.ui.label.setText(self.ui.label.text() + "(")
        elif event.key() == QtCore.Qt.Key_ParenRight:
            self.ui.label.setText(self.ui.label.text() + ")")
        elif event.key() == QtCore.Qt.Key_Period:
            self.ui.label.setText(self.ui.label.text() + ".")
        elif event.key() == QtCore.Qt.Key_AsciiCircum:
            self.ui.label.setText(self.ui.label.text()+"^")
        elif event.key()== QtCore.Qt.Key_Escape:
            sys.exit(app.exec_())
            
############################################################
#
#                         MAIN
#
############################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
