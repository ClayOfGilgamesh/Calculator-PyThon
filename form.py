##########################################################
#form này được xây dựng dựa trên Qt5 framework           
#sử dụng Qt5 designer để thiết kế
#
#
##########################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument,QTextOption
import math
import re
#########################################################
class Ui_MainWindow(object): ## Khởi tạo đối tượng Ui_MainWindow để lưu trữ toàn bộ  các phần tử trên UI
    ## Hàm setupUi dưới đây sẽ khởi tạo và thiết lập các thuộc tính cho MainWindow và các phần tử con của nó
    ## Ở đây sẽ gồm có 2 frame: frame & frame_2
    ## frame sẽ chưa một label như một màn hình hiển thị cho máy tính
    ## frame_2 sẽ chứa các button là các phím chức năng của máy tính
    ## Đoạn code dưới đây được tạo tự động bởi Qtdesign
    ## file thiết kế vào form.ui
    ##chuyển từ form.ui sang form.py bằng câu lệnh: "pyuic5 form.ui -o form.py"
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") # tên là MainWindow
        MainWindow.resize(470, 862) #kích thước 
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);") #màu nền cho MainWindow
        # Cài đặt icon cho ứng dụng
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\PythonProject\z4289657383758_9fa3271fe1a1557fa57160509f959e09 (1).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        # tạo một wiget trung tâm để chứa các phần tử con khác
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # layout sắp xếp theo chiều dọc gồm frame và frame_2 như đã đề cặp ở trên
        # setup các thuộc tính
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(453, 250))
        self.frame.setMaximumSize(QtCore.QSize(453, 250))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(116, 235, 213, 1), stop:1 rgba(172, 182, 229, 1));\n"
"border-Radius : 10px\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
      
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label.setText("")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)# căng dưới
        self.label.setStyleSheet("font-size: 20pt;") 
        self.verticalLayout_2.addWidget(self.label)
        self.label.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(116, 235, 213, 1), stop:1 rgba(172, 182, 229, 1));\n"
"border-Radius : 10px\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        
###################################################################
#
#                     Cấu hình các phím
#
###################################################################

 ######### phím 1
        self.phim1 = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("1"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phim1.sizePolicy().hasHeightForWidth())
        self.phim1.setSizePolicy(sizePolicy)
        self.phim1.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phim1.setObjectName("phim1")
        self.gridLayout.addWidget(self.phim1, 0, 0, 1, 1)
        
######### phím 2  #########################################
        self.phim2 = QtWidgets.QPushButton(self.frame_2, clicked=lambda:self.Press_it("2") ) # sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phim2.sizePolicy().hasHeightForWidth())
        self.phim2.setSizePolicy(sizePolicy)
        self.phim2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phim2.setObjectName("phim2")
        self.gridLayout.addWidget(self.phim2, 0, 1, 1, 1)
        
######### phím 3  ##########################################
        self.phim3 = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("3"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phim3.sizePolicy().hasHeightForWidth())
        self.phim3.setSizePolicy(sizePolicy)
        self.phim3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phim3.setObjectName("phim3")
        self.gridLayout.addWidget(self.phim3, 0, 2, 1, 1)
        
######### phím 4  ##########################################
        self.phim4 = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("4"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phim4.sizePolicy().hasHeightForWidth())
        self.phim4.setSizePolicy(sizePolicy)
        self.phim4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phim4.setObjectName("phim4")
        self.gridLayout.addWidget(self.phim4, 1, 0, 1, 1)
        
######### phím 5  #########################################
        self.phim5 = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("5"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phim5.sizePolicy().hasHeightForWidth())
        self.phim5.setSizePolicy(sizePolicy)
        self.phim5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phim5.setObjectName("phim5")
        self.gridLayout.addWidget(self.phim5, 1, 1, 1, 1)
        
######### phím 6  #######################################
        self.phim6 = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("6"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phim6.sizePolicy().hasHeightForWidth())
        self.phim6.setSizePolicy(sizePolicy)
        self.phim6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phim6.setObjectName("phim6")
        self.gridLayout.addWidget(self.phim6, 1, 2, 1, 1)
        
######### phím 7  ######################################
        self.phim7 = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("7"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phim7.sizePolicy().hasHeightForWidth())
        self.phim7.setSizePolicy(sizePolicy)
        self.phim7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phim7.setObjectName("phim7")
        self.gridLayout.addWidget(self.phim7, 2, 0, 1, 1)
        
######### phím 8  #####################################
        self.phim8 = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("8"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phim8.sizePolicy().hasHeightForWidth())
        self.phim8.setSizePolicy(sizePolicy)
        self.phim8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phim8.setObjectName("phim8")
        self.gridLayout.addWidget(self.phim8, 2, 1, 1, 1)
        
######### phím 9  #########################################
        self.phim9 = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("9"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phim9.sizePolicy().hasHeightForWidth())
        self.phim9.setSizePolicy(sizePolicy)
        self.phim9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phim9.setObjectName("phim9")
        self.gridLayout.addWidget(self.phim9, 2, 2, 1, 1)
        
######### phím 0  #######################################
        self.phim0 = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("0"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phim0.sizePolicy().hasHeightForWidth())
        self.phim0.setSizePolicy(sizePolicy)
        self.phim0.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phim0.setObjectName("phim0")
        self.gridLayout.addWidget(self.phim0, 3, 0, 1, 1)
        
######### phím DEL  ########################################
        self.phimdel = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimdel.sizePolicy().hasHeightForWidth())
        self.phimdel.setSizePolicy(sizePolicy)
        self.phimdel.setStyleSheet("\n"
"background-color: rgb(255, 0, 127);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimdel.setObjectName("phimdel")
        self.gridLayout.addWidget(self.phimdel, 3, 1, 1, 1)
        
######### phím AC ##########################################
        self.phimac = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimac.sizePolicy().hasHeightForWidth())
        self.phimac.setSizePolicy(sizePolicy)
        self.phimac.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimac.setObjectName("phimac")
        self.gridLayout.addWidget(self.phimac, 3, 2, 1, 1)
        
######### phím .  ##########################################
        self.phimcham = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("."))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimcham.sizePolicy().hasHeightForWidth())
        self.phimcham.setSizePolicy(sizePolicy)
        self.phimcham.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimcham.setObjectName("phimcham")
        self.gridLayout.addWidget(self.phimcham, 4, 0, 1, 1)
        
######### phím +  ##########################################
        self.phimcong = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("+"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimcong.sizePolicy().hasHeightForWidth())
        self.phimcong.setSizePolicy(sizePolicy)
        self.phimcong.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimcong.setObjectName("phimcong")
        self.gridLayout.addWidget(self.phimcong, 4, 1, 1, 1)
        
######### phím -  ##########################################
        self.phimtru = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("-"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimtru.sizePolicy().hasHeightForWidth())
        self.phimtru.setSizePolicy(sizePolicy)
        self.phimtru.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimtru.setObjectName("phimtru")
        self.gridLayout.addWidget(self.phimtru, 4, 2, 1, 1)
        
######### phím **  ##########################################
        self.phimbinhphuong = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("^"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimbinhphuong.sizePolicy().hasHeightForWidth())
        self.phimbinhphuong.setSizePolicy(sizePolicy)
        self.phimbinhphuong.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimbinhphuong.setObjectName("phimbinhphuong")
        self.gridLayout.addWidget(self.phimbinhphuong, 5, 0, 1, 1)
        
######### phím X  ##########################################
        self.phimnhan = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("x"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimnhan.sizePolicy().hasHeightForWidth())
        self.phimnhan.setSizePolicy(sizePolicy)
        self.phimnhan.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimnhan.setObjectName("phimnhan")
        self.gridLayout.addWidget(self.phimnhan, 5, 1, 1, 1)
        
######### phím /  ##########################################
        self.phimchia = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("÷"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimchia.sizePolicy().hasHeightForWidth())
        self.phimchia.setSizePolicy(sizePolicy)
        self.phimchia.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimchia.setObjectName("phimchia")
        self.gridLayout.addWidget(self.phimchia, 5, 2, 1, 1)
        
######### phím )  ##########################################
        self.phimmongoac = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("("))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimmongoac.sizePolicy().hasHeightForWidth())
######### phím )  ##########################################
        self.phimmongoac.setSizePolicy(sizePolicy)
        self.phimmongoac.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimmongoac.setObjectName("phimmongoac")
        self.gridLayout.addWidget(self.phimmongoac, 6, 0, 1, 1)
        
        self.dongngoac = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it(")"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dongngoac.sizePolicy().hasHeightForWidth())
        self.dongngoac.setSizePolicy(sizePolicy)
        self.dongngoac.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.dongngoac.setObjectName("dongngoac")
        self.gridLayout.addWidget(self.dongngoac, 6, 1, 1, 1)
        
######### phím !   ##########################################
        self.phimgiaithua = QtWidgets.QPushButton(self.frame_2,clicked=lambda:self.Press_it("!"))# sự kiện khi ấn phím
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimgiaithua.sizePolicy().hasHeightForWidth())
        self.phimgiaithua.setSizePolicy(sizePolicy)
        self.phimgiaithua.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimgiaithua.setObjectName("phimgiaithua")
        self.gridLayout.addWidget(self.phimgiaithua, 7, 0, 1, 1)
        
######### phím Ans   ##########################################
        self.phimans = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimans.sizePolicy().hasHeightForWidth())
        self.phimans.setSizePolicy(sizePolicy)
        self.phimans.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.phimans.setObjectName("phimans")
        self.gridLayout.addWidget(self.phimans, 7, 1, 1, 1)
        
######### phím =   ##########################################
        self.phimbang = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phimbang.sizePolicy().hasHeightForWidth())
        self.phimbang.setSizePolicy(sizePolicy)
        self.phimbang.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(172, 182, 229, 1), stop:1 rgba(116, 235, 213, 1));\n"
"")
        self.phimbang.setObjectName("phimbang")
        self.gridLayout.addWidget(self.phimbang, 6, 2, 2, 1)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
###################################################################
#
#           Cài đặt lại phần hiển thị cho các phím
#
###################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.phim1.setText(_translate("MainWindow", "1"))
        self.phim2.setText(_translate("MainWindow", "2"))
        self.phim3.setText(_translate("MainWindow", "3"))
        self.phim4.setText(_translate("MainWindow", "4"))
        self.phim5.setText(_translate("MainWindow", "5"))
        self.phim6.setText(_translate("MainWindow", "6"))
        self.phim7.setText(_translate("MainWindow", "7"))
        self.phim8.setText(_translate("MainWindow", "8"))
        self.phim9.setText(_translate("MainWindow", "9"))
        self.phim0.setText(_translate("MainWindow", "0"))
        self.phimdel.setText(_translate("MainWindow", "DEL"))
        self.phimac.setText(_translate("MainWindow", "AC"))
        self.phimcham.setText(_translate("MainWindow", "."))
        self.phimcong.setText(_translate("MainWindow", "+"))
        self.phimtru.setText(_translate("MainWindow", "-"))
        self.phimbinhphuong.setText(_translate("MainWindow", "x²"))
        self.phimnhan.setText(_translate("MainWindow", "x"))
        self.phimchia.setText(_translate("MainWindow", "÷"))
        self.phimmongoac.setText(_translate("MainWindow", "("))
        self.dongngoac.setText(_translate("MainWindow", ")"))
        self.phimgiaithua.setText(_translate("MainWindow", "!"))
        self.phimans.setText(_translate("MainWindow", "Ans"))
        self.phimbang.setText(_translate("MainWindow", "="))
###################################################################
#
#                     Xử lý các sự kiện phím
#
###################################################################
# đối với các phím số và phép toán
    def Press_it(self,pressed):
        self.label.setText(self.label.text()+pressed)
# đối  với 1 số phím đặc biệt 
 
#Sự kiện phím =            
    def skpbang(self):
        self.exp=self.label.text() # chuyển chuỗi biểu thức vào exp
        ##Xử lý đầu vào
        ## với trường hợp có phép giai thừa ta cần chuyển về dạng có thể sử dụng hàm eval() được
        ## ở đây ta tìm đến chữ số trước ký tự '!' trong chuỗi input_str lưu vào num
        ## cụ thể r"\d+!" tìm kiếm tất cả các chuỗi con trong input_str mà bắt đầu bằng một hoặc nhiều chữ số (\d+) 
        ## và kết thúc bằng dấu chấm than (!).
        ##tính giá trị gai thừa của num rồi lưu vào  factorial
        ## thay thế biểu thứ  =  factorial trong chuỗi input_str sau đó gán nó bằng với exp 
        input_str=self.exp
        pattern = r"\d+!"
        matches = re.findall(pattern, input_str)
        for match in matches:
                num = int(match[:-1])
                factorial = math.factorial(num)
                input_str = input_str.replace(match, str(factorial))
        self.exp=input_str
        ##chuyển các phím '^','x','÷' về '**','*','/' để hàm eval() xử lý được
        self.exp=self.exp.replace("^","**")
        self.exp=self.exp.replace("x","*")
        self.exp=self.exp.replace("÷","/")
        ## xử lý lỗi khi nhập sai biểu thức
        try:
          self.result=eval(self.exp)
          self.label.setText(str(self.result))
        except:
          self.label.setText("Lỗi phép tính!")

#sự kiện phím DEL
    def skpdel(self):
        self.label.setText(self.label.text()[:-1])
        self.exp=self.label.text()
        
#sự kiện phím AC
    def skpac(self):
            self.label.setText('') 
            self.exp=self.label.text()
            
#sự kiện phím Ans
    def skpans(self):
            self.label.setText(str(self.result))
            self.exp=self.label.text()


    def clickevent(self, MainWindow):
        ##################
        ## cài sự kiện click chuột với 1 số phím đặc biệt
        ##################
        self.phimbang.clicked.connect(self.skpbang)
        self.phimdel.clicked.connect(self.skpdel) 
        self.phimac.clicked.connect(self.skpac)  
        self.phimans.clicked.connect(self.skpans)   
        
    def animation(self, MainWindow): 
        ## cài sự kiện  di chuột qua cho các phím 
        ###################
        ##trỏ chuột vào
        self.phimac.enterEvent = lambda event: self.phimac.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n""background-color: rgb(196, 6, 54);") 

        self.phimac.leaveEvent = lambda event: self.phimac.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n""background-color: rgb(255, 0, 127);")
        self.phimdel.enterEvent = lambda event: self.phimdel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n""background-color: rgb(196, 6, 54);")
        self.phimdel.leaveEvent = lambda event: self.phimdel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n""background-color: rgb(255, 0, 127);")
        self.phimans.enterEvent = lambda event: self.phimans.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n""background-color: dodgerblue;")
        self.phimans.leaveEvent = lambda event: self.phimans.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n""background-color: rgb(85, 255, 255);")
        
        phim_list = [self.phim0,self.phim1, self.phim2,self.phim3,self.phim4,self.phim5,self.phim6,self.phim7,self.phim8,self.phim9,self.dongngoac,
                     self.phimmongoac,self.phimbinhphuong,self.phimcong,self.phimtru,self.phimnhan,self.phimchia,self.phimgiaithua,self.phimcham]
        for phim in phim_list:
                phim.enterEvent = lambda event, p=phim: p.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n""background-color: gainsboro")
                phim.leaveEvent = lambda event, p=phim: p.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n""background-color: white")
                
        self.phimbang.enterEvent = lambda event: self.phimbang.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";\n"
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(179, 255, 171, 1), stop:1 rgba(18, 255, 247, 1));\n"
                "")
        self.phimbang.leaveEvent = lambda event: self.phimbang.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";\n"
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(172, 182, 229, 1), stop:1 rgba(116, 235, 213, 1));\n"
                "")

 
