# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\home\Desktop\IndoorPosition\Interfaces\ViewState.ui'
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 290, 768))
        self.label.setStyleSheet("background-image: url(null);\n"
"background-color:#2F3C71;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1366, 44))
        self.label_2.setStyleSheet("background-image: url(null);\n"
"background-color:#222222;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.navManageState = QtWidgets.QPushButton(self.frame)
        self.navManageState.setGeometry(QtCore.QRect(1075, 120, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navManageState.setFont(font)
        self.navManageState.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navManageState.setStyleSheet("QPushButton\n"
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
        icon.addPixmap(QtGui.QPixmap(":/images/manageArmory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navManageState.setIcon(icon)
        self.navManageState.setIconSize(QtCore.QSize(25, 25))
        self.navManageState.setObjectName("navManageState")
        self.navViewPunishment = QtWidgets.QPushButton(self.frame)
        self.navViewPunishment.setGeometry(QtCore.QRect(10, 558, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewPunishment.setFont(font)
        self.navViewPunishment.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewPunishment.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/punishment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewPunishment.setIcon(icon1)
        self.navViewPunishment.setIconSize(QtCore.QSize(25, 25))
        self.navViewPunishment.setFlat(False)
        self.navViewPunishment.setObjectName("navViewPunishment")
        self.navViewImpKey = QtWidgets.QPushButton(self.frame)
        self.navViewImpKey.setGeometry(QtCore.QRect(10, 294, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewImpKey.setFont(font)
        self.navViewImpKey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewImpKey.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/impKey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewImpKey.setIcon(icon2)
        self.navViewImpKey.setIconSize(QtCore.QSize(25, 25))
        self.navViewImpKey.setFlat(False)
        self.navViewImpKey.setObjectName("navViewImpKey")
        self.navViewGenKey = QtWidgets.QPushButton(self.frame)
        self.navViewGenKey.setGeometry(QtCore.QRect(10, 338, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewGenKey.setFont(font)
        self.navViewGenKey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewGenKey.setStyleSheet("QPushButton \n"
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
        icon3.addPixmap(QtGui.QPixmap(":/images/genKey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewGenKey.setIcon(icon3)
        self.navViewGenKey.setIconSize(QtCore.QSize(25, 25))
        self.navViewGenKey.setFlat(False)
        self.navViewGenKey.setObjectName("navViewGenKey")
        self.navViewVisitor = QtWidgets.QPushButton(self.frame)
        self.navViewVisitor.setGeometry(QtCore.QRect(10, 382, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewVisitor.setFont(font)
        self.navViewVisitor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewVisitor.setStyleSheet("QPushButton \n"
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
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/visitor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewVisitor.setIcon(icon4)
        self.navViewVisitor.setIconSize(QtCore.QSize(25, 25))
        self.navViewVisitor.setFlat(False)
        self.navViewVisitor.setObjectName("navViewVisitor")
        self.navViewTransport = QtWidgets.QPushButton(self.frame)
        self.navViewTransport.setGeometry(QtCore.QRect(10, 426, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewTransport.setFont(font)
        self.navViewTransport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewTransport.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/transport.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewTransport.setIcon(icon5)
        self.navViewTransport.setIconSize(QtCore.QSize(25, 25))
        self.navViewTransport.setFlat(False)
        self.navViewTransport.setObjectName("navViewTransport")
        self.navViewGangway = QtWidgets.QPushButton(self.frame)
        self.navViewGangway.setGeometry(QtCore.QRect(10, 470, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewGangway.setFont(font)
        self.navViewGangway.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewGangway.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/gangway.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewGangway.setIcon(icon6)
        self.navViewGangway.setIconSize(QtCore.QSize(25, 25))
        self.navViewGangway.setFlat(False)
        self.navViewGangway.setObjectName("navViewGangway")
        self.navViewDuty = QtWidgets.QPushButton(self.frame)
        self.navViewDuty.setGeometry(QtCore.QRect(10, 514, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewDuty.setFont(font)
        self.navViewDuty.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewDuty.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/duty.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewDuty.setIcon(icon7)
        self.navViewDuty.setIconSize(QtCore.QSize(25, 25))
        self.navViewDuty.setFlat(False)
        self.navViewDuty.setObjectName("navViewDuty")
        self.navViewNight = QtWidgets.QPushButton(self.frame)
        self.navViewNight.setGeometry(QtCore.QRect(10, 646, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewNight.setFont(font)
        self.navViewNight.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewNight.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/night.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewNight.setIcon(icon8)
        self.navViewNight.setIconSize(QtCore.QSize(25, 25))
        self.navViewNight.setFlat(False)
        self.navViewNight.setObjectName("navViewNight")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 245, 270, 2))
        self.label_4.setStyleSheet("background-color:#4154A0;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.navViewMOB = QtWidgets.QPushButton(self.frame)
        self.navViewMOB.setGeometry(QtCore.QRect(10, 110, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewMOB.setFont(font)
        self.navViewMOB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewMOB.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/mob.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewMOB.setIcon(icon9)
        self.navViewMOB.setIconSize(QtCore.QSize(32, 32))
        self.navViewMOB.setFlat(False)
        self.navViewMOB.setObjectName("navViewMOB")
        self.navViewLocation = QtWidgets.QPushButton(self.frame)
        self.navViewLocation.setGeometry(QtCore.QRect(10, 22, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewLocation.setFont(font)
        self.navViewLocation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewLocation.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/locate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewLocation.setIcon(icon10)
        self.navViewLocation.setIconSize(QtCore.QSize(25, 25))
        self.navViewLocation.setFlat(False)
        self.navViewLocation.setObjectName("navViewLocation")
        self.navViewMangement = QtWidgets.QPushButton(self.frame)
        self.navViewMangement.setGeometry(QtCore.QRect(10, 66, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewMangement.setFont(font)
        self.navViewMangement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewMangement.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/personnel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewMangement.setIcon(icon11)
        self.navViewMangement.setIconSize(QtCore.QSize(32, 32))
        self.navViewMangement.setFlat(False)
        self.navViewMangement.setObjectName("navViewMangement")
        self.navViewPPE = QtWidgets.QPushButton(self.frame)
        self.navViewPPE.setGeometry(QtCore.QRect(10, 690, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewPPE.setFont(font)
        self.navViewPPE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewPPE.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/armPPE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewPPE.setIcon(icon12)
        self.navViewPPE.setIconSize(QtCore.QSize(25, 25))
        self.navViewPPE.setFlat(False)
        self.navViewPPE.setObjectName("navViewPPE")
        self.navViewOOD = QtWidgets.QPushButton(self.frame)
        self.navViewOOD.setGeometry(QtCore.QRect(10, 602, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewOOD.setFont(font)
        self.navViewOOD.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewOOD.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/oodObserve.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewOOD.setIcon(icon13)
        self.navViewOOD.setIconSize(QtCore.QSize(25, 25))
        self.navViewOOD.setFlat(False)
        self.navViewOOD.setObjectName("navViewOOD")
        self.navViewCMS = QtWidgets.QPushButton(self.frame)
        self.navViewCMS.setGeometry(QtCore.QRect(10, 154, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewCMS.setFont(font)
        self.navViewCMS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewCMS.setStyleSheet("QPushButton \n"
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
"QPushButton:pressed\n"
"{\n"
"    background-color: #384889;\n"
"     border-width: 3px;\n"
"    border-color: #5C70BC;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/sreCall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewCMS.setIcon(icon14)
        self.navViewCMS.setIconSize(QtCore.QSize(25, 25))
        self.navViewCMS.setFlat(False)
        self.navViewCMS.setObjectName("navViewCMS")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(1069, 5, 271, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" text-align: right;\n"
"    color: #ffffff;\n"
"    background-color:#222222;")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/armoryState.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon15)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(306, 680, 100, 80))
        self.pushButton_2.setStyleSheet(" border:1px solid #fff;\n"
"    border-radius:4px;\n"
"    outline:none;")
        self.pushButton_2.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/logoMTIP.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon16)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_2.setObjectName("pushButton_2")
        self.navViewPersonnel = QtWidgets.QPushButton(self.frame)
        self.navViewPersonnel.setGeometry(QtCore.QRect(10, 250, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewPersonnel.setFont(font)
        self.navViewPersonnel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewPersonnel.setStyleSheet("QPushButton \n"
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
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/personnelData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewPersonnel.setIcon(icon17)
        self.navViewPersonnel.setIconSize(QtCore.QSize(25, 25))
        self.navViewPersonnel.setFlat(False)
        self.navViewPersonnel.setObjectName("navViewPersonnel")
        self.navViewState = QtWidgets.QPushButton(self.frame)
        self.navViewState.setGeometry(QtCore.QRect(10, 198, 270, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewState.setFont(font)
        self.navViewState.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewState.setStyleSheet("QPushButton \n"
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
"QPushButton:active\n"
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
        self.navViewState.setIcon(icon15)
        self.navViewState.setIconSize(QtCore.QSize(25, 25))
        self.navViewState.setFlat(False)
        self.navViewState.setObjectName("navViewState")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(316, 110, 141, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_18.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(306, 132, 681, 125))
        self.label_16.setStyleSheet("    background-color:#ffff;\n"
"    border-width: 1px;\n"
"    border-color: #A0A0A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(331, 203, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.lblTotalEnlisted = QtWidgets.QLabel(self.frame)
        self.lblTotalEnlisted.setGeometry(QtCore.QRect(490, 143, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblTotalEnlisted.setFont(font)
        self.lblTotalEnlisted.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTotalEnlisted.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblTotalEnlisted.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTotalEnlisted.setObjectName("lblTotalEnlisted")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(331, 173, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(331, 143, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.lblSailorsEnlisted = QtWidgets.QLabel(self.frame)
        self.lblSailorsEnlisted.setGeometry(QtCore.QRect(490, 203, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblSailorsEnlisted.setFont(font)
        self.lblSailorsEnlisted.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblSailorsEnlisted.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblSailorsEnlisted.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSailorsEnlisted.setObjectName("lblSailorsEnlisted")
        self.lblOfficersEnlisted = QtWidgets.QLabel(self.frame)
        self.lblOfficersEnlisted.setGeometry(QtCore.QRect(490, 173, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblOfficersEnlisted.setFont(font)
        self.lblOfficersEnlisted.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblOfficersEnlisted.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblOfficersEnlisted.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblOfficersEnlisted.setObjectName("lblOfficersEnlisted")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(306, 287, 681, 125))
        self.label_17.setStyleSheet("    background-color:#ffff;\n"
"    border-width: 1px;\n"
"    border-color: #A0A0A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(331, 298, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(331, 358, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(316, 265, 141, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_19.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(331, 328, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_20.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.lblOfficersPresent = QtWidgets.QLabel(self.frame)
        self.lblOfficersPresent.setGeometry(QtCore.QRect(490, 328, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblOfficersPresent.setFont(font)
        self.lblOfficersPresent.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblOfficersPresent.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblOfficersPresent.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblOfficersPresent.setObjectName("lblOfficersPresent")
        self.lblSailorsPresent = QtWidgets.QLabel(self.frame)
        self.lblSailorsPresent.setGeometry(QtCore.QRect(490, 358, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblSailorsPresent.setFont(font)
        self.lblSailorsPresent.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblSailorsPresent.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblSailorsPresent.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSailorsPresent.setObjectName("lblSailorsPresent")
        self.lblTotalPresent = QtWidgets.QLabel(self.frame)
        self.lblTotalPresent.setGeometry(QtCore.QRect(490, 298, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblTotalPresent.setFont(font)
        self.lblTotalPresent.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTotalPresent.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblTotalPresent.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTotalPresent.setObjectName("lblTotalPresent")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(306, 442, 681, 186))
        self.label_21.setStyleSheet("    background-color:#ffff;\n"
"    border-width: 1px;\n"
"    border-color: #A0A0A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(377, 483, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.lblShifaOfficers = QtWidgets.QLabel(self.frame)
        self.lblShifaOfficers.setGeometry(QtCore.QRect(536, 483, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblShifaOfficers.setFont(font)
        self.lblShifaOfficers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblShifaOfficers.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblShifaOfficers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblShifaOfficers.setObjectName("lblShifaOfficers")
        self.lblCasualOfficers = QtWidgets.QLabel(self.frame)
        self.lblCasualOfficers.setGeometry(QtCore.QRect(536, 513, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblCasualOfficers.setFont(font)
        self.lblCasualOfficers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblCasualOfficers.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblCasualOfficers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblCasualOfficers.setObjectName("lblCasualOfficers")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(331, 453, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_23.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(316, 420, 121, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_24.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(377, 513, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_25.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.lblAwayOfficers = QtWidgets.QLabel(self.frame)
        self.lblAwayOfficers.setGeometry(QtCore.QRect(490, 453, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblAwayOfficers.setFont(font)
        self.lblAwayOfficers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblAwayOfficers.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblAwayOfficers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblAwayOfficers.setObjectName("lblAwayOfficers")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(377, 543, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_26.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.lblPersonalOfficers = QtWidgets.QLabel(self.frame)
        self.lblPersonalOfficers.setGeometry(QtCore.QRect(536, 543, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblPersonalOfficers.setFont(font)
        self.lblPersonalOfficers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblPersonalOfficers.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblPersonalOfficers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblPersonalOfficers.setObjectName("lblPersonalOfficers")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(377, 573, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_27.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.lblSickOfficers = QtWidgets.QLabel(self.frame)
        self.lblSickOfficers.setGeometry(QtCore.QRect(536, 573, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblSickOfficers.setFont(font)
        self.lblSickOfficers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblSickOfficers.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblSickOfficers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSickOfficers.setObjectName("lblSickOfficers")
        self.lblSickSailors = QtWidgets.QLabel(self.frame)
        self.lblSickSailors.setGeometry(QtCore.QRect(921, 573, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblSickSailors.setFont(font)
        self.lblSickSailors.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblSickSailors.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblSickSailors.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSickSailors.setObjectName("lblSickSailors")
        self.lblPersonalSailors = QtWidgets.QLabel(self.frame)
        self.lblPersonalSailors.setGeometry(QtCore.QRect(921, 543, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblPersonalSailors.setFont(font)
        self.lblPersonalSailors.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblPersonalSailors.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblPersonalSailors.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblPersonalSailors.setObjectName("lblPersonalSailors")
        self.lblShifaSailors = QtWidgets.QLabel(self.frame)
        self.lblShifaSailors.setGeometry(QtCore.QRect(921, 483, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblShifaSailors.setFont(font)
        self.lblShifaSailors.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblShifaSailors.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblShifaSailors.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblShifaSailors.setObjectName("lblShifaSailors")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(762, 573, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_28.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(762, 513, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_29.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(762, 543, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_30.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(716, 453, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_31.setFont(font)
        self.label_31.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_31.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.lblCasualSailors = QtWidgets.QLabel(self.frame)
        self.lblCasualSailors.setGeometry(QtCore.QRect(921, 513, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblCasualSailors.setFont(font)
        self.lblCasualSailors.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblCasualSailors.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblCasualSailors.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblCasualSailors.setObjectName("lblCasualSailors")
        self.lblAwaySailors = QtWidgets.QLabel(self.frame)
        self.lblAwaySailors.setGeometry(QtCore.QRect(875, 453, 41, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblAwaySailors.setFont(font)
        self.lblAwaySailors.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblAwaySailors.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblAwaySailors.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblAwaySailors.setObjectName("lblAwaySailors")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(762, 483, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_32.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(641, 450, 1, 171))
        self.label_33.setStyleSheet("background-color:#A0A0A0;")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.label_2.raise_()
        self.label.raise_()
        self.navManageState.raise_()
        self.navViewPunishment.raise_()
        self.navViewImpKey.raise_()
        self.navViewGenKey.raise_()
        self.navViewVisitor.raise_()
        self.navViewTransport.raise_()
        self.navViewGangway.raise_()
        self.navViewDuty.raise_()
        self.navViewNight.raise_()
        self.label_4.raise_()
        self.navViewMOB.raise_()
        self.navViewLocation.raise_()
        self.navViewMangement.raise_()
        self.navViewPPE.raise_()
        self.navViewOOD.raise_()
        self.navViewCMS.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.navViewPersonnel.raise_()
        self.navViewState.raise_()
        self.label_16.raise_()
        self.label_18.raise_()
        self.label_11.raise_()
        self.lblTotalEnlisted.raise_()
        self.label_10.raise_()
        self.label_12.raise_()
        self.lblSailorsEnlisted.raise_()
        self.lblOfficersEnlisted.raise_()
        self.label_17.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.lblOfficersPresent.raise_()
        self.lblSailorsPresent.raise_()
        self.lblTotalPresent.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.lblShifaOfficers.raise_()
        self.lblCasualOfficers.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.lblAwayOfficers.raise_()
        self.label_26.raise_()
        self.lblPersonalOfficers.raise_()
        self.label_27.raise_()
        self.lblSickOfficers.raise_()
        self.lblSickSailors.raise_()
        self.lblPersonalSailors.raise_()
        self.lblShifaSailors.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.lblCasualSailors.raise_()
        self.lblAwaySailors.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(306, 100, 1040, 1))
        self.label_13.setStyleSheet("background-color:#A0A0A0;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(306, 60, 221, 31))
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
        self.navManageState.setText(_translate("MainWindow", "Manage Armory State"))
        self.navViewPunishment.setText(_translate("MainWindow", "Punishment Book"))
        self.navViewImpKey.setText(_translate("MainWindow", "Important Key Book"))
        self.navViewGenKey.setText(_translate("MainWindow", "General Key Book"))
        self.navViewVisitor.setText(_translate("MainWindow", "Visitor Book"))
        self.navViewTransport.setText(_translate("MainWindow", "Transport Book"))
        self.navViewGangway.setText(_translate("MainWindow", "Gangway Book"))
        self.navViewDuty.setText(_translate("MainWindow", "Duty Book"))
        self.navViewNight.setText(_translate("MainWindow", "Night Round Book"))
        self.navViewMOB.setText(_translate("MainWindow", "Man Over Board"))
        self.navViewLocation.setText(_translate("MainWindow", "Personnel Location"))
        self.navViewMangement.setText(_translate("MainWindow", "Personnel Management System"))
        self.navViewPPE.setText(_translate("MainWindow", "Small Arm and PPE Book"))
        self.navViewOOD.setText(_translate("MainWindow", "OOD Observation Book"))
        self.navViewCMS.setText(_translate("MainWindow", "SRE Call Management System"))
        self.pushButton.setText(_translate("MainWindow", "Armory State Management System"))
        self.navViewPersonnel.setText(_translate("MainWindow", "Personnel Data Book"))
        self.navViewState.setText(_translate("MainWindow", "Armory State Management System"))
        self.label_18.setText(_translate("MainWindow", "Personnel Enlisted"))
        self.label_11.setText(_translate("MainWindow", "CPO/ Sailors:"))
        self.lblTotalEnlisted.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Officers:"))
        self.label_12.setText(_translate("MainWindow", "Total:"))
        self.lblSailorsEnlisted.setText(_translate("MainWindow", "0"))
        self.lblOfficersEnlisted.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "Total:"))
        self.label_15.setText(_translate("MainWindow", "CPO/ Sailors:"))
        self.label_19.setText(_translate("MainWindow", "Present Personnel"))
        self.label_20.setText(_translate("MainWindow", "Officers:"))
        self.lblOfficersPresent.setText(_translate("MainWindow", "0"))
        self.lblSailorsPresent.setText(_translate("MainWindow", "0"))
        self.lblTotalPresent.setText(_translate("MainWindow", "0"))
        self.label_22.setText(_translate("MainWindow", "Shifa:"))
        self.lblShifaOfficers.setText(_translate("MainWindow", "0"))
        self.lblCasualOfficers.setText(_translate("MainWindow", "0"))
        self.label_23.setText(_translate("MainWindow", "Away Officers:"))
        self.label_24.setText(_translate("MainWindow", "Away Personnel"))
        self.label_25.setText(_translate("MainWindow", "Casual Leave:"))
        self.lblAwayOfficers.setText(_translate("MainWindow", "0"))
        self.label_26.setText(_translate("MainWindow", "Personal Leave:"))
        self.lblPersonalOfficers.setText(_translate("MainWindow", "0"))
        self.label_27.setText(_translate("MainWindow", "Sick Leave:"))
        self.lblSickOfficers.setText(_translate("MainWindow", "0"))
        self.lblSickSailors.setText(_translate("MainWindow", "0"))
        self.lblPersonalSailors.setText(_translate("MainWindow", "0"))
        self.lblShifaSailors.setText(_translate("MainWindow", "0"))
        self.label_28.setText(_translate("MainWindow", "Sick Leave:"))
        self.label_29.setText(_translate("MainWindow", "Casual Leave:"))
        self.label_30.setText(_translate("MainWindow", "Personal Leave:"))
        self.label_31.setText(_translate("MainWindow", "Away CPO/ Sailors:"))
        self.lblCasualSailors.setText(_translate("MainWindow", "0"))
        self.lblAwaySailors.setText(_translate("MainWindow", "0"))
        self.label_32.setText(_translate("MainWindow", "Shifa:"))
        self.label_6.setText(_translate("MainWindow", "Armory State Details"))
import IconResource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
