# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\home\Desktop\IndoorPosition\Interfaces\Example.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cBoxStatus = QtWidgets.QComboBox(self.frame)
        self.cBoxStatus.setGeometry(QtCore.QRect(50, 75, 101, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxStatus.setFont(font)
        self.cBoxStatus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxStatus.setStyleSheet("QComboBox{ border-width: 1px;\n"
" border-color: #aaa;\n"
" border-style: solid;\n"
"border-radius:6; \n"
"}\n"
"\n"
"QComboBox::drop-down:button{\n"
"background-color:transparent;\n"
"}\n"
"QComboBox::down-arrow {\n"
" \n"
"    image: url(C:/Users/home/Desktop/IndoorPoistionInterfaces/InterfaceIcons/dropDown.png);\n"
"    width: 25px;\n"
"    height: 9px;\n"
"}\n"
"QComboBox:hover{\n"
"     border:1px solid #000;    \n"
"     transition:.3s;\n"
"}\n"
"  QComboBox:focus{\n"
"    border-color:dodgerBlue;\n"
"    box-shadow:0 0 8px 0 dodgerBlue;\n"
"  }\n"
"")
        self.cBoxStatus.setEditable(False)
        self.cBoxStatus.setFrame(True)
        self.cBoxStatus.setObjectName("cBoxStatus")
        self.cBoxStatus.addItem("")
        self.cBoxStatus.addItem("")
        self.cBoxStatus.addItem("")
        self.cBoxStatus.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cBoxStatus.setItemText(0, _translate("MainWindow", "Shifa"))
        self.cBoxStatus.setItemText(1, _translate("MainWindow", "Casual Leave"))
        self.cBoxStatus.setItemText(2, _translate("MainWindow", "Personal Leave"))
        self.cBoxStatus.setItemText(3, _translate("MainWindow", "Sick Leave"))
