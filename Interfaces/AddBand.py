# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\home\Desktop\IndoorPosition\Interfaces\AddBand.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 765)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.frame.setStyleSheet("background-color: #ffffff")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1366, 44))
        self.label_2.setStyleSheet("background-color:#222222;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.btnEditLogin = QtWidgets.QPushButton(self.frame)
        self.btnEditLogin.setGeometry(QtCore.QRect(564, 210, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnEditLogin.setFont(font)
        self.btnEditLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEditLogin.setStyleSheet("QPushButton\n"
"{\n"
"    color: #ffffff;\n"
"    background-color:#4154A0;\n"
"    border-width: 1px;\n"
"    border-color: #4154A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 11pt;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#384889\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditLogin.setIcon(icon)
        self.btnEditLogin.setIconSize(QtCore.QSize(25, 25))
        self.btnEditLogin.setObjectName("btnEditLogin")
        self.lblDataEntrySuccessful = QtWidgets.QLabel(self.frame)
        self.lblDataEntrySuccessful.setEnabled(True)
        self.lblDataEntrySuccessful.setGeometry(QtCore.QRect(331, 189, 361, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblDataEntrySuccessful.setFont(font)
        self.lblDataEntrySuccessful.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblDataEntrySuccessful.setStyleSheet("color: green;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblDataEntrySuccessful.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblDataEntrySuccessful.setObjectName("lblDataEntrySuccessful")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(1080, 5, 260, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" text-align: right;\n"
"    color: #ffffff;\n"
"    background-color:#222222;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/smartWatch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(331, 680, 100, 80))
        self.pushButton_2.setStyleSheet(" border:1px solid #fff;\n"
"    border-radius:4px;\n"
"    outline:none;")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/logoMTIP.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_2.setObjectName("pushButton_2")
        self.edtBandNo = QtWidgets.QLineEdit(self.frame)
        self.edtBandNo.setGeometry(QtCore.QRect(490, 140, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtBandNo.setFont(font)
        self.edtBandNo.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"
"    box-sizing:border-box;\n"
"    transition:.3s;\n"
"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"
"     transition:.3s;\n"
"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"
"    box-shadow:0 0 8px 0 dodgerBlue;\n"
"  }")
        self.edtBandNo.setObjectName("edtBandNo")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(331, 138, 151, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 310, 768))
        self.label.setStyleSheet("background-image: url(null);\n"
"background-color:#2F3C71;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.navViewLoginSettings = QtWidgets.QPushButton(self.frame)
        self.navViewLoginSettings.setGeometry(QtCore.QRect(10, 3, 290, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewLoginSettings.setFont(font)
        self.navViewLoginSettings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewLoginSettings.setStyleSheet("QPushButton \n"
"{\n"
"    text-align: left;\n"
"    color: #ffffff;\n"
"    background-color:#2F3C71;\n"
"    border-width: 1px;\n"
"    border-color: #2F3C71;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 11pt;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#4154A0;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewLoginSettings.setIcon(icon3)
        self.navViewLoginSettings.setIconSize(QtCore.QSize(25, 25))
        self.navViewLoginSettings.setFlat(False)
        self.navViewLoginSettings.setObjectName("navViewLoginSettings")
        self.navViewBandSettings = QtWidgets.QPushButton(self.frame)
        self.navViewBandSettings.setGeometry(QtCore.QRect(10, 47, 290, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewBandSettings.setFont(font)
        self.navViewBandSettings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewBandSettings.setStyleSheet("QPushButton \n"
"{\n"
"    text-align: left;\n"
"    color: #ffffff;\n"
"    background-color:#2F3C71;\n"
"    border-width: 1px;\n"
"    border-color: #2F3C71;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 11pt;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"QPushButton:active\n"
"{\n"
"    background-color:#4154A0;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#4154A0;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        self.navViewBandSettings.setIcon(icon1)
        self.navViewBandSettings.setIconSize(QtCore.QSize(32, 32))
        self.navViewBandSettings.setFlat(False)
        self.navViewBandSettings.setObjectName("navViewBandSettings")
        self.label_2.raise_()
        self.lblDataEntrySuccessful.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.edtBandNo.raise_()
        self.label_9.raise_()
        self.label.raise_()
        self.btnEditLogin.raise_()
        self.navViewBandSettings.raise_()
        self.navViewLoginSettings.raise_()
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(316, 100, 1020, 1))
        self.label_13.setStyleSheet("background-color:#A0A0A0;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(316, 60, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnEditLogin.setText(_translate("MainWindow", "Add New Band"))
        self.lblDataEntrySuccessful.setText(_translate("MainWindow", "Details Saved Successfully!"))
        self.pushButton.setText(_translate("MainWindow", "Band Settings"))
        self.label_9.setText(_translate("MainWindow", "Band No."))
        self.navViewLoginSettings.setText(_translate("MainWindow", "Login Settings"))
        self.navViewBandSettings.setText(_translate("MainWindow", "Band Settings"))
        self.label_6.setText(_translate("MainWindow", "Enter Band Details"))
import IconResource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
