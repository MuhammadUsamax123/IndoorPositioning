# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\home\Desktop\IndoorPosition\Interfaces\ViewState.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class PersonnelLocation(object):
    def setup_PersonnelLocation(self, MainWindow):
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
        self.label.setGeometry(QtCore.QRect(0, 0, 310, 768))
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
        self.navViewPunishment = QtWidgets.QPushButton(self.frame)
        self.navViewPunishment.setGeometry(QtCore.QRect(10, 587, 290, 44))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/punishment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewPunishment.setIcon(icon)
        self.navViewPunishment.setIconSize(QtCore.QSize(25, 25))
        self.navViewPunishment.setFlat(False)
        self.navViewPunishment.setObjectName("navViewPunishment")
        self.navViewImpKey = QtWidgets.QPushButton(self.frame)
        self.navViewImpKey.setGeometry(QtCore.QRect(10, 323, 290, 44))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/impKey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewImpKey.setIcon(icon1)
        self.navViewImpKey.setIconSize(QtCore.QSize(25, 25))
        self.navViewImpKey.setFlat(False)
        self.navViewImpKey.setObjectName("navViewImpKey")
        self.navViewGenKey = QtWidgets.QPushButton(self.frame)
        self.navViewGenKey.setGeometry(QtCore.QRect(10, 367, 290, 44))
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
        icon2.addPixmap(QtGui.QPixmap(":/images/genKey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewGenKey.setIcon(icon2)
        self.navViewGenKey.setIconSize(QtCore.QSize(25, 25))
        self.navViewGenKey.setFlat(False)
        self.navViewGenKey.setObjectName("navViewGenKey")
        self.navViewVisitor = QtWidgets.QPushButton(self.frame)
        self.navViewVisitor.setGeometry(QtCore.QRect(10, 411, 290, 44))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/visitor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewVisitor.setIcon(icon3)
        self.navViewVisitor.setIconSize(QtCore.QSize(25, 25))
        self.navViewVisitor.setFlat(False)
        self.navViewVisitor.setObjectName("navViewVisitor")
        self.navViewTransport = QtWidgets.QPushButton(self.frame)
        self.navViewTransport.setGeometry(QtCore.QRect(10, 455, 290, 44))
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/transport.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewTransport.setIcon(icon4)
        self.navViewTransport.setIconSize(QtCore.QSize(25, 25))
        self.navViewTransport.setFlat(False)
        self.navViewTransport.setObjectName("navViewTransport")
        self.navViewGangway = QtWidgets.QPushButton(self.frame)
        self.navViewGangway.setGeometry(QtCore.QRect(10, 499, 290, 44))
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/gangway.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewGangway.setIcon(icon5)
        self.navViewGangway.setIconSize(QtCore.QSize(25, 25))
        self.navViewGangway.setFlat(False)
        self.navViewGangway.setObjectName("navViewGangway")
        self.navViewDuty = QtWidgets.QPushButton(self.frame)
        self.navViewDuty.setGeometry(QtCore.QRect(10, 543, 290, 44))
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/duty.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewDuty.setIcon(icon6)
        self.navViewDuty.setIconSize(QtCore.QSize(25, 25))
        self.navViewDuty.setFlat(False)
        self.navViewDuty.setObjectName("navViewDuty")
        self.navViewNight = QtWidgets.QPushButton(self.frame)
        self.navViewNight.setGeometry(QtCore.QRect(10, 675, 290, 44))
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/night.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewNight.setIcon(icon7)
        self.navViewNight.setIconSize(QtCore.QSize(25, 25))
        self.navViewNight.setFlat(False)
        self.navViewNight.setObjectName("navViewNight")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 272, 290, 2))
        self.label_4.setStyleSheet("background-color:#4154A0;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.navViewMOB = QtWidgets.QPushButton(self.frame)
        self.navViewMOB.setGeometry(QtCore.QRect(10, 91, 290, 44))
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/mob.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewMOB.setIcon(icon8)
        self.navViewMOB.setIconSize(QtCore.QSize(32, 32))
        self.navViewMOB.setFlat(False)
        self.navViewMOB.setObjectName("navViewMOB")
        self.navViewLocation = QtWidgets.QPushButton(self.frame)
        self.navViewLocation.setGeometry(QtCore.QRect(10, 3, 290, 44))
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/locate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewLocation.setIcon(icon9)
        self.navViewLocation.setIconSize(QtCore.QSize(25, 25))
        self.navViewLocation.setFlat(False)
        self.navViewLocation.setObjectName("navViewLocation")
        self.navViewManagement = QtWidgets.QPushButton(self.frame)
        self.navViewManagement.setGeometry(QtCore.QRect(10, 47, 290, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewManagement.setFont(font)
        self.navViewManagement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewManagement.setStyleSheet("QPushButton \n"
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
        icon10.addPixmap(QtGui.QPixmap(":/images/personnel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewManagement.setIcon(icon10)
        self.navViewManagement.setIconSize(QtCore.QSize(32, 32))
        self.navViewManagement.setFlat(False)
        self.navViewManagement.setObjectName("navViewManagement")
        self.navViewPPE = QtWidgets.QPushButton(self.frame)
        self.navViewPPE.setGeometry(QtCore.QRect(10, 719, 290, 44))
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
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/armPPE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewPPE.setIcon(icon11)
        self.navViewPPE.setIconSize(QtCore.QSize(25, 25))
        self.navViewPPE.setFlat(False)
        self.navViewPPE.setObjectName("navViewPPE")
        self.navViewOOD = QtWidgets.QPushButton(self.frame)
        self.navViewOOD.setGeometry(QtCore.QRect(10, 631, 290, 44))
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
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/oodObserve.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewOOD.setIcon(icon12)
        self.navViewOOD.setIconSize(QtCore.QSize(25, 25))
        self.navViewOOD.setFlat(False)
        self.navViewOOD.setObjectName("navViewOOD")
        self.navViewCMS = QtWidgets.QPushButton(self.frame)
        self.navViewCMS.setGeometry(QtCore.QRect(10, 135, 290, 44))
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
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/sreCall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewCMS.setIcon(icon13)
        self.navViewCMS.setIconSize(QtCore.QSize(25, 25))
        self.navViewCMS.setFlat(False)
        self.navViewCMS.setObjectName("navViewCMS")
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
        self.pushButton.setIcon(icon9)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(316, 680, 100, 80))
        self.pushButton_2.setStyleSheet(" border:1px solid #fff;\n"
"    border-radius:4px;\n"
"    outline:none;")
        self.pushButton_2.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/logoMTIP.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon14)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_2.setObjectName("pushButton_2")
        self.navViewPersonnel = QtWidgets.QPushButton(self.frame)
        self.navViewPersonnel.setGeometry(QtCore.QRect(10, 279, 290, 44))
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
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/personnelData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewPersonnel.setIcon(icon15)
        self.navViewPersonnel.setIconSize(QtCore.QSize(25, 25))
        self.navViewPersonnel.setFlat(False)
        self.navViewPersonnel.setObjectName("navViewPersonnel")
        self.navViewStatePersonnel = QtWidgets.QPushButton(self.frame)
        self.navViewStatePersonnel.setGeometry(QtCore.QRect(10, 179, 290, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewStatePersonnel.setFont(font)
        self.navViewStatePersonnel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewStatePersonnel.setStyleSheet("QPushButton \n"
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
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/armoryState.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewStatePersonnel.setIcon(icon16)
        self.navViewStatePersonnel.setIconSize(QtCore.QSize(25, 25))
        self.navViewStatePersonnel.setFlat(False)
        self.navViewStatePersonnel.setObjectName("navViewStatePersonnel")
        self.navViewStateArmory = QtWidgets.QPushButton(self.frame)
        self.navViewStateArmory.setGeometry(QtCore.QRect(10, 223, 290, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewStateArmory.setFont(font)
        self.navViewStateArmory.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewStateArmory.setStyleSheet("QPushButton \n"
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
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/images/armory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewStateArmory.setIcon(icon31)
        self.navViewStateArmory.setIconSize(QtCore.QSize(25, 25))
        self.navViewStateArmory.setFlat(False)
        self.navViewStateArmory.setObjectName("navViewStateArmory")
        self.btnLogout = QtWidgets.QPushButton(self.frame)
        self.btnLogout.setGeometry(QtCore.QRect(326, 0, 111, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnLogout.setFont(font)
        self.btnLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogout.setStyleSheet("QPushButton \n"
"{\n"
"    color: #ffffff;\n"
"    background-color:#EF7901;\n"
"    border-width: 1px;\n"
"    border-color: #F35305;\n"
"    border-style: solid;\n"
"    padding: 3px;\n"
"    font-size: 11pt;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#FE9730;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #EF7901;\n"
"     border-width: 3px;\n"
"    border-color: #FE9730;\n"
"    border-style: solid;\n"
"\n"
"}")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogout.setIcon(icon32)
        self.btnLogout.setIconSize(QtCore.QSize(32, 32))
        self.btnLogout.setFlat(False)
        self.btnLogout.setObjectName("btnLogout")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(325, 60, 1025, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1023, 549))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.btnshipImage = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnshipImage.setGeometry(QtCore.QRect(-10, -10, 1040, 569))
        self.btnshipImage.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btnshipImage.setStyleSheet("border:1px solid #fff;\n"
"outline:none;\n"
"background-color:#AADAFF;\n"
"color:#AADAFF;")
        self.btnshipImage.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/shipDefault.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnshipImage.setIcon(icon17)
        self.btnshipImage.setIconSize(QtCore.QSize(1040, 520))
        self.btnshipImage.setObjectName("btnshipImage")
        self.btnZoomIn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnZoomIn.setGeometry(QtCore.QRect(974, 6, 44, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnZoomIn.setFont(font)
        self.btnZoomIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnZoomIn.setStyleSheet("QPushButton\n"
"{\n"
"    color: #000000;\n"
"    background-color:#ffffff;\n"
"    border-width: 1px;\n"
"    border-color: #A5A5A5;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 11pt;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#E5E5E5\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #D1D1D1;\n"
"     border-width: 3px;\n"
"    border-color: #E5E5E5;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        self.btnZoomIn.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/images/zoomIn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnZoomIn.setIcon(icon18)
        self.btnZoomIn.setIconSize(QtCore.QSize(25, 25))
        self.btnZoomIn.setObjectName("btnZoomIn")
        self.btnZoomOut = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnZoomOut.setGeometry(QtCore.QRect(974, 56, 44, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnZoomOut.setFont(font)
        self.btnZoomOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnZoomOut.setStyleSheet("QPushButton\n"
"{\n"
"    color: #000000;\n"
"    background-color:#ffffff;\n"
"    border-width: 1px;\n"
"    border-color: #A5A5A5;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 11pt;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#E5E5E5\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #D1D1D1;\n"
"     border-width: 3px;\n"
"    border-color: #E5E5E5;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        self.btnZoomOut.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/images/zoomOut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnZoomOut.setIcon(icon19)
        self.btnZoomOut.setIconSize(QtCore.QSize(25, 25))
        self.btnZoomOut.setObjectName("btnZoomOut")
        self.btnMoveRight = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMoveRight.setGeometry(QtCore.QRect(974, 500, 44, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMoveRight.setFont(font)
        self.btnMoveRight.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMoveRight.setStyleSheet("QPushButton\n"
"{\n"
"    color: #000000;\n"
"    background-color:#ffffff;\n"
"    border-width: 1px;\n"
"    border-color: #A5A5A5;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 11pt;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#E5E5E5\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #D1D1D1;\n"
"     border-width: 3px;\n"
"    border-color: #E5E5E5;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        self.btnMoveRight.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/images/moveRight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMoveRight.setIcon(icon20)
        self.btnMoveRight.setIconSize(QtCore.QSize(25, 25))
        self.btnMoveRight.setObjectName("btnMoveRight")
        self.btnMoveLeft = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMoveLeft.setGeometry(QtCore.QRect(924, 500, 44, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMoveLeft.setFont(font)
        self.btnMoveLeft.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMoveLeft.setStyleSheet("QPushButton\n"
"{\n"
"    color: #000000;\n"
"    background-color:#ffffff;\n"
"    border-width: 1px;\n"
"    border-color: #A5A5A5;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 11pt;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#E5E5E5\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #D1D1D1;\n"
"     border-width: 3px;\n"
"    border-color: #E5E5E5;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        self.btnMoveLeft.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/images/moveLeft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMoveLeft.setIcon(icon21)
        self.btnMoveLeft.setIconSize(QtCore.QSize(25, 25))
        self.btnMoveLeft.setObjectName("btnMoveLeft")
        self.btnMarker2Room2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMarker2Room2.setGeometry(QtCore.QRect(570, 163, 51, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMarker2Room2.setFont(font)
        self.btnMarker2Room2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMarker2Room2.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color:transparent;\n"
"\n"
"}")
        self.btnMarker2Room2.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/images/markerRoom3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMarker2Room2.setIcon(icon22)
        self.btnMarker2Room2.setIconSize(QtCore.QSize(75, 75))
        self.btnMarker2Room2.setObjectName("btnMarker2Room2")
        self.btnMarker1Room2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMarker1Room2.setGeometry(QtCore.QRect(531, 163, 51, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMarker1Room2.setFont(font)
        self.btnMarker1Room2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMarker1Room2.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color:transparent;\n"
"\n"
"}")
        self.btnMarker1Room2.setText("")
        self.btnMarker1Room2.setIcon(icon22)
        self.btnMarker1Room2.setIconSize(QtCore.QSize(75, 75))
        self.btnMarker1Room2.setObjectName("btnMarker1Room2")
        self.btnMarker3Room1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMarker3Room1.setGeometry(QtCore.QRect(476, 163, 51, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMarker3Room1.setFont(font)
        self.btnMarker3Room1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMarker3Room1.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color:transparent;\n"
"\n"
"}")
        self.btnMarker3Room1.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/images/markerRoom2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMarker3Room1.setIcon(icon23)
        self.btnMarker3Room1.setIconSize(QtCore.QSize(75, 75))
        self.btnMarker3Room1.setObjectName("btnMarker3Room1")
        self.btnMarker2Room1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMarker2Room1.setGeometry(QtCore.QRect(413, 240, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMarker2Room1.setFont(font)
        self.btnMarker2Room1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMarker2Room1.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color:transparent;\n"
"\n"
"}")
        self.btnMarker2Room1.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/images/markerRoomLeft2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMarker2Room1.setIcon(icon24)
        self.btnMarker2Room1.setIconSize(QtCore.QSize(75, 75))
        self.btnMarker2Room1.setObjectName("btnMarker2Room1")
        self.btnMarker1Room3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMarker1Room3.setGeometry(QtCore.QRect(520, 298, 51, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMarker1Room3.setFont(font)
        self.btnMarker1Room3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMarker1Room3.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color:transparent;\n"
"\n"
"}")
        self.btnMarker1Room3.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/images/markerRoom1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMarker1Room3.setIcon(icon25)
        self.btnMarker1Room3.setIconSize(QtCore.QSize(75, 75))
        self.btnMarker1Room3.setObjectName("btnMarker1Room3")
        self.btnMarker2Room3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMarker2Room3.setGeometry(QtCore.QRect(560, 298, 51, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMarker2Room3.setFont(font)
        self.btnMarker2Room3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMarker2Room3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btnMarker2Room3.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color:transparent;\n"
"\n"
"}")
        self.btnMarker2Room3.setText("")
        self.btnMarker2Room3.setIcon(icon25)
        self.btnMarker2Room3.setIconSize(QtCore.QSize(75, 75))
        self.btnMarker2Room3.setObjectName("btnMarker2Room3")
        self.btnMarker1Room1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMarker1Room1.setGeometry(QtCore.QRect(476, 258, 51, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMarker1Room1.setFont(font)
        self.btnMarker1Room1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMarker1Room1.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color:transparent;\n"
"\n"
"}")
        self.btnMarker1Room1.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/images/markerRoomDown2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMarker1Room1.setIcon(icon26)
        self.btnMarker1Room1.setIconSize(QtCore.QSize(75, 75))
        self.btnMarker1Room1.setObjectName("btnMarker1Room1")
        self.btnMarker3Room3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMarker3Room3.setGeometry(QtCore.QRect(583, 286, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMarker3Room3.setFont(font)
        self.btnMarker3Room3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMarker3Room3.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color:transparent;\n"
"\n"
"}")
        self.btnMarker3Room3.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/images/markerRoomRight1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMarker3Room3.setIcon(icon27)
        self.btnMarker3Room3.setIconSize(QtCore.QSize(75, 75))
        self.btnMarker3Room3.setObjectName("btnMarker3Room3")
        self.btnMarker3Room2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMarker3Room2.setGeometry(QtCore.QRect(583, 240, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMarker3Room2.setFont(font)
        self.btnMarker3Room2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMarker3Room2.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color:transparent;\n"
"\n"
"}")
        self.btnMarker3Room2.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/images/markerRoomRight3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMarker3Room2.setIcon(icon28)
        self.btnMarker3Room2.setIconSize(QtCore.QSize(75, 75))
        self.btnMarker3Room2.setObjectName("btnMarker3Room2")
        self.btnMobError = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.btnMobError.setEnabled(True)
        self.btnMobError.setGeometry(QtCore.QRect(6, 482, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnMobError.setFont(font)
        self.btnMobError.setStyleSheet("border:1px solid  #FF5555;\n"
"background-color: #FF5555;\n"
"outline:none;\n"
"color: #FFFFFF;")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/images/notification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMobError.setIcon(icon29)
        self.btnMobError.setIconSize(QtCore.QSize(32, 32))
        self.btnMobError.setObjectName("btnMobError")
        self.btnshipImage.raise_()
        self.btnMarker2Room2.raise_()
        self.btnMarker1Room2.raise_()
        self.btnMarker3Room1.raise_()
        self.btnMarker2Room1.raise_()
        self.btnMarker1Room3.raise_()
        self.btnMarker2Room3.raise_()
        self.btnMarker1Room1.raise_()
        self.btnMarker3Room3.raise_()
        self.btnMarker3Room2.raise_()
        self.btnMoveLeft.raise_()
        self.btnMoveRight.raise_()
        self.btnZoomIn.raise_()
        self.btnZoomOut.raise_()
        self.btnMobError.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.label_2.raise_()
        self.label.raise_()
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
        self.navViewManagement.raise_()
        self.navViewPPE.raise_()
        self.navViewOOD.raise_()
        self.navViewCMS.raise_()
        self.navViewStateArmory.raise_()
        self.btnLogout.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.navViewPersonnel.raise_()
        self.navViewStatePersonnel.raise_()
        self.scrollArea.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.navViewManagement.setText(_translate("MainWindow", "Personnel Management System"))
        self.navViewPPE.setText(_translate("MainWindow", "Small Arm and PPE Book"))
        self.navViewOOD.setText(_translate("MainWindow", "OOD Observation Book"))
        self.navViewCMS.setText(_translate("MainWindow", "SRE Call Management System"))
        self.navViewStateArmory.setText(_translate("MainWindow", "Armory State Management System"))
        self.btnLogout.setText(_translate("MainWindow", "Logout"))
        self.pushButton.setText(_translate("MainWindow", "Personnel Location"))
        self.navViewPersonnel.setText(_translate("MainWindow", "Personnel Data Book"))
        self.navViewStatePersonnel.setText(_translate("MainWindow", "Personnel State Management System"))
        self.btnMobError.setText(_translate("MainWindow", "Alert! Man Overboard!"))


#----------------------------------------backend for Personnel Location Interface----------------------------------------------
      
        disableHideMarkers(self)


def disableHideMarkers(self):
            self.btnMarker1Room1.hide()
            self.btnMarker2Room1.hide()
            self.btnMarker3Room1.hide()
            self.btnMarker1Room2.hide()
            self.btnMarker2Room2.hide()
            self.btnMarker3Room2.hide()
            self.btnMarker1Room3.hide()
            self.btnMarker2Room3.hide()
            self.btnMarker3Room3.hide()

            self.btnMarker1Room1.setEnabled(False)
            self.btnMarker2Room1.setEnabled(False)
            self.btnMarker3Room1.setEnabled(False)
            self.btnMarker1Room2.setEnabled(False)
            self.btnMarker2Room2.setEnabled(False)
            self.btnMarker3Room2.setEnabled(False)
            self.btnMarker1Room3.setEnabled(False)
            self.btnMarker2Room3.setEnabled(False)
            self.btnMarker3Room3.setEnabled(False)
            
def enableShowMarkers(self):
            self.btnMarker1Room1.show()
            self.btnMarker2Room1.show()
            self.btnMarker3Room1.show()
            self.btnMarker1Room2.show()
            self.btnMarker2Room2.show()
            self.btnMarker3Room2.show()
            self.btnMarker1Room3.show()
            self.btnMarker2Room3.show()
            self.btnMarker3Room3.show()

            self.btnMarker1Room1.setEnabled(True)
            self.btnMarker2Room1.setEnabled(True)
            self.btnMarker3Room1.setEnabled(True)
            self.btnMarker1Room2.setEnabled(True)
            self.btnMarker2Room2.setEnabled(True)
            self.btnMarker3Room2.setEnabled(True)
            self.btnMarker1Room3.setEnabled(True)
            self.btnMarker2Room3.setEnabled(True)
            self.btnMarker3Room3.setEnabled(True)


import IconResource_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PersonnelLocation()
    ui.setup_PersonnelLocation(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
