# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\home\Desktop\IndoorPosition\Interfaces\AddImpKey.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


def connectDB():
        conn=sqlite3.connect('IndoorPositionDatabase.DB')
        return conn
def createTable():
        conn=connectDB()
        c=conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS ImportantKeyBook(keyNumber TEXT, keyName TEXT, IssuingPNO TEXT, IssuingName TEXT, IssuingRank TEXT, TimeOut TEXT, TimeIn TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS GeneralKeyBook(keyNumber TEXT, keyName TEXT, IssuingPNO TEXT, IssuingName TEXT, IssuingRank TEXT, TimeOut TEXT, TimeIn TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS PersonnelDataBook(personnelIDNo TEXT, personnelPNo TEXT,personnelRank TEXT,personnelName TEXT, personnelDepartment TEXT, personnelBloodGroup TEXT) ")
        return conn
def insertData(self,query):
        try:
                conn=createTable()
                c=conn.cursor()
                c.execute(query)
                conn.commit()
                c.close()
                conn.close()
                self.lblDataEntrySuccessful.show()
        except:
                self.lblDataEntrySuccessful.setStyleSheet("color: red;\n""background-color:#ffffff;\n""font-size: 11pt")
                self.lblDataEntrySuccessful.setText("Details could not be saved!")
                self.lblDataEntrySuccessful.show()
def fillComboBoxData(query):
        try:    
                comboBoxList=[]
                conn=createTable()
                c=conn.cursor()
                c.execute(query)
                tempcomboBoxBuffer=c.fetchall()
                for i in range(len(tempcomboBoxBuffer)):
                        comboBoxList.append(tempcomboBoxBuffer[i][0])
                c.close()
                conn.close()
                return comboBoxList
        except:
               return 
def resetKeysGUI(self):
        self.edtKeyNumber.clear()
        self.edtKeyName.clear()
        self.cBoxIssuingPNo.clear()
        self.cBoxIssuingName.clear()
        self.cBoxImpRank.clear()
        cbIssuingPNo=fillComboBoxData("SELECT personnelPNo FROM PersonnelDataBook")
        if(cbIssuingPNo!=0):
                self.cBoxIssuingPNo.addItems(cbIssuingPNo)
        else:
                print("no PNO")

        cbIssuingName=fillComboBoxData("SELECT personnelName FROM PersonnelDataBook")
        if(cbIssuingName!=0):
                self.cBoxIssuingName.addItems(cbIssuingName)
        else:
                print("no Name")

        cbRank=fillComboBoxData("Select personnelRank FROM PersonnelDataBook")
        if(cbRank!=0):
                self.cBoxImpRank.addItems(cbRank)
        else:
                print("no Rank")    
def resetPersonnelDataGUI(self):
        self.edtID.clear()
        self.edtPNO.clear()
        self.edtRank.clear()
        self.edtName.clear()
        self.edtDepartment.clear()
        self.edtBloodGroup.clear()
################################################################### App Class ##########################################################################

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.addpersonneldata= AddPersonnelDataWidget()
        self.addimportantkey= AddImportantKeyWidget()
        self.addgeneralkey= AddGeneralKeyWidget()

        self.stacked = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked)
        self.stacked.addWidget(self.addpersonneldata)
        self.stacked.addWidget(self.addimportantkey)
        self.stacked.addWidget(self.addgeneralkey)
    def change_view(self, option):
        if(option==1):
            resetPersonnelDataGUI(self.addpersonneldata)
            self.addpersonneldata.lblDataEntrySuccessful.hide()
            self.stacked.setCurrentWidget(self.addpersonneldata)
        elif(option==2):
            self.addimportantkey.lblDataEntrySuccessful.hide()
            resetKeysGUI(self.addimportantkey)
            self.stacked.setCurrentWidget(self.addimportantkey)
        elif(option==3):
            self.addgeneralkey.lblDataEntrySuccessful.hide()
            (self.addgeneralkey)
            self.stacked.setCurrentWidget(self.addgeneralkey)
            


################################################################### Add Important Key Interface ##########################################################################
class AddImportantKey(object):
    def setup_AddImportantKey(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.frame.setStyleSheet("background-color: #ffffff")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 280, 768))
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
        self.navViewImpKeyDetails = QtWidgets.QPushButton(self.frame)
        self.navViewImpKeyDetails.setGeometry(QtCore.QRect(1075, 668, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewImpKeyDetails.setFont(font)
        self.navViewImpKeyDetails.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewImpKeyDetails.setStyleSheet("QPushButton\n"
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
        icon.addPixmap(QtGui.QPixmap(":/images/viewDetails.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewImpKeyDetails.setIcon(icon)
        self.navViewImpKeyDetails.setIconSize(QtCore.QSize(25, 25))
        self.navViewImpKeyDetails.setObjectName("navViewImpKeyDetails")
        self.navViewPunishment = QtWidgets.QPushButton(self.frame)
        self.navViewPunishment.setGeometry(QtCore.QRect(10, 512, 260, 44))
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
        self.navViewImpKey.setGeometry(QtCore.QRect(10, 248, 260, 44))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/impKey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewImpKey.setIcon(icon2)
        self.navViewImpKey.setIconSize(QtCore.QSize(25, 25))
        self.navViewImpKey.setFlat(False)
        self.navViewImpKey.setObjectName("navViewImpKey")
        self.navViewGenKey = QtWidgets.QPushButton(self.frame)
        self.navViewGenKey.setGeometry(QtCore.QRect(10, 292, 260, 44))
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
        self.navViewVisitor.setGeometry(QtCore.QRect(10, 336, 260, 44))
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
        self.navViewTransport.setGeometry(QtCore.QRect(10, 380, 260, 44))
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
        self.navViewGangway.setGeometry(QtCore.QRect(10, 424, 260, 44))
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
        self.navViewDuty.setGeometry(QtCore.QRect(10, 468, 260, 44))
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
        self.navViewNight.setGeometry(QtCore.QRect(10, 600, 260, 44))
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
        self.label_4.setGeometry(QtCore.QRect(10, 199, 260, 2))
        self.label_4.setStyleSheet("background-color:#4154A0;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.navViewMOB = QtWidgets.QPushButton(self.frame)
        self.navViewMOB.setGeometry(QtCore.QRect(10, 108, 260, 44))
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
        self.navViewLocation.setGeometry(QtCore.QRect(10, 20, 260, 44))
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
        self.navViewMangement.setGeometry(QtCore.QRect(10, 64, 260, 44))
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
        self.navViewPPE.setGeometry(QtCore.QRect(10, 644, 260, 44))
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
        self.navViewOOD.setGeometry(QtCore.QRect(10, 556, 260, 44))
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
        self.navViewCMS.setGeometry(QtCore.QRect(10, 152, 260, 44))
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
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(331, 152, 191, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.edtKeyNumber = QtWidgets.QLineEdit(self.frame)
        self.edtKeyNumber.setGeometry(QtCore.QRect(522, 154, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtKeyNumber.setFont(font)
        self.edtKeyNumber.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"

"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"
"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"  }")
        self.edtKeyNumber.setObjectName("edtKeyNumber")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(331, 196, 191, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.edtKeyName = QtWidgets.QLineEdit(self.frame)
        self.edtKeyName.setGeometry(QtCore.QRect(522, 198, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtKeyName.setFont(font)
        self.edtKeyName.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"  }")
        self.edtKeyName.setObjectName("edtKeyName")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(331, 240, 191, 44))
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
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(331, 284, 191, 44))
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
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(331, 328, 191, 44))
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
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(331, 372, 191, 44))
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
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(331, 416, 191, 44))
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
        self.tmOut = QtWidgets.QTimeEdit(self.frame)
        self.tmOut.setGeometry(QtCore.QRect(522, 374, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tmOut.setFont(font)
        self.tmOut.setStyleSheet("QTimeEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:6px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QTimeEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QTimeEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"border-radius: 6;\n"
"  }\n"
"    QTimeEdit::up-button{\n"
" subcontrol-origin: border;\n"
"subcontrol-position: top right;\n"
"width: 25px;\n"
" border: none;\n"
"image: url(:/images/dropUpTime.png);\n"
"}\n"
"QTimeEdit::down-button {\n"
" subcontrol-origin: border;\n"
" subcontrol-position: bottom right;\n"
" width: 25px;\n"
" border: none;\n"
"\n"
"image: url(:/images/dropDownTime.png);\n"
"\n"
"}\n"
"QTimeEdit::down-button:hover {\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
" border-right: 1px solid rgb(0, 0, 0);\n"
"background-color:#e6e6e6;\n"
"    \n"
"}\n"
"QTimeEdit::up-button:hover {\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-top: 1px solid rgb(0, 0, 0);\n"
" border-right: 1px solid rgb(0, 0, 0);\n"
"background-color:#e6e6e6;\n"
"\n"
"}\n"
"QTimeEdit::up-button:focus{\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-top: 1px solid dodgerBlue;\n"
" border-right: 1px solid dodgerBlue;\n"
"\n"
"}\n"
"QTimeEdit::down-button:focus{\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-bottom: 1px solid dodgerBlue;\n"
" border-right: 1px solid dodgerBlue;\n"
"\n"
"}")
        self.tmOut.setCalendarPopup(False)
        self.tmOut.setObjectName("tmOut")
        self.tmIn = QtWidgets.QTimeEdit(self.frame)
        self.tmIn.setGeometry(QtCore.QRect(522, 418, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tmIn.setFont(font)
        self.tmIn.setStyleSheet("QTimeEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:6px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QTimeEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QTimeEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"border-radius: 6;\n"
"  }\n"
"    QTimeEdit::up-button{\n"
" subcontrol-origin: border;\n"
"subcontrol-position: top right;\n"
"width: 25px;\n"
" border: none;\n"
"image: url(:/images/dropUpTime.png);\n"
"}\n"
"QTimeEdit::down-button {\n"
" subcontrol-origin: border;\n"
" subcontrol-position: bottom right;\n"
" width: 25px;\n"
" border: none;\n"
"\n"
"image: url(:/images/dropDownTime.png);\n"
"\n"
"}\n"
"QTimeEdit::down-button:hover {\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
" border-right: 1px solid rgb(0, 0, 0);\n"
"background-color:#e6e6e6;\n"
"    \n"
"}\n"
"QTimeEdit::up-button:hover {\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-top: 1px solid rgb(0, 0, 0);\n"
" border-right: 1px solid rgb(0, 0, 0);\n"
"background-color:#e6e6e6;\n"
"\n"
"}\n"
"QTimeEdit::up-button:focus{\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-top: 1px solid dodgerBlue;\n"
" border-right: 1px solid dodgerBlue;\n"
"\n"
"}\n"
"QTimeEdit::down-button:focus{\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-bottom: 1px solid dodgerBlue;\n"
" border-right: 1px solid dodgerBlue;\n"
"\n"
"}")
        self.tmIn.setCalendarPopup(False)
        self.tmIn.setObjectName("tmIn")
        self.lblDataEntrySuccessful = QtWidgets.QLabel(self.frame)
        self.lblDataEntrySuccessful.setEnabled(True)
        self.lblDataEntrySuccessful.setGeometry(QtCore.QRect(331, 470, 361, 44))
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
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(296, 627, 251, 181))
        self.pushButton_2.setStyleSheet(" border:1px solid #fff;\n"
"    border-radius:4px;\n"
"    outline:none;")
        self.pushButton_2.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/logoMTIP.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon15)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_2.setObjectName("pushButton_2")
        self.navViewPersonnel = QtWidgets.QPushButton(self.frame)
        self.navViewPersonnel.setGeometry(QtCore.QRect(10, 204, 260, 44))
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
        icon16.addPixmap(QtGui.QPixmap(":/images/personnelData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewPersonnel.setIcon(icon16)
        self.navViewPersonnel.setIconSize(QtCore.QSize(25, 25))
        self.navViewPersonnel.setFlat(False)
        self.navViewPersonnel.setObjectName("navViewPersonnel")
        self.cBoxIssuingName = QtWidgets.QComboBox(self.frame)
        self.cBoxIssuingName.setGeometry(QtCore.QRect(522, 286, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxIssuingName.setFont(font)
        self.cBoxIssuingName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxIssuingName.setStyleSheet("QComboBox{ border-width: 1px;\n"
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

"}\n"
"  QComboBox:focus{\n"
"    border-color:dodgerBlue;\n"

"  }\n"
"")
        self.cBoxIssuingName.setFrame(True)
        self.cBoxIssuingName.setObjectName("cBoxIssuingName")
        self.cBoxIssuingPNo = QtWidgets.QComboBox(self.frame)
        self.cBoxIssuingPNo.setGeometry(QtCore.QRect(522, 242, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxIssuingPNo.setFont(font)
        self.cBoxIssuingPNo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxIssuingPNo.setStyleSheet("QComboBox{ border-width: 1px;\n"
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

"}\n"
"  QComboBox:focus{\n"
"    border-color:dodgerBlue;\n"

"  }\n"
"")
        self.cBoxIssuingPNo.setFrame(True)
        self.cBoxIssuingPNo.setObjectName("cBoxIssuingPNo")
        self.cBoxImpRank = QtWidgets.QComboBox(self.frame)
        self.cBoxImpRank.setGeometry(QtCore.QRect(522, 330, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxImpRank.setFont(font)
        self.cBoxImpRank.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxImpRank.setStyleSheet("QComboBox{ border-width: 1px;\n"
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

"}\n"
"  QComboBox:focus{\n"
"    border-color:dodgerBlue;\n"

"  }\n"
"")
        self.cBoxImpRank.setFrame(True)
        self.cBoxImpRank.setObjectName("cBoxImpRank")
        self.label_2.raise_()
        self.label.raise_()
        self.navViewImpKeyDetails.raise_()
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
        self.label_7.raise_()
        self.edtKeyNumber.raise_()
        self.label_8.raise_()
        self.edtKeyName.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_14.raise_()
        self.tmOut.raise_()
        self.tmIn.raise_()
        self.lblDataEntrySuccessful.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.navViewPersonnel.raise_()
        self.cBoxIssuingName.raise_()
        self.cBoxIssuingPNo.raise_()
        self.cBoxImpRank.raise_()
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(296, 100, 1050, 1))
        self.label_13.setStyleSheet("background-color:#A0A0A0;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(296, 60, 221, 31))
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
        self.btnAddImpKey = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddImpKey.setGeometry(QtCore.QRect(592, 490, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnAddImpKey.setFont(font)
        self.btnAddImpKey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddImpKey.setStyleSheet("QPushButton\n"
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
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddImpKey.setIcon(icon17)
        self.btnAddImpKey.setIconSize(QtCore.QSize(25, 25))
        self.btnAddImpKey.setObjectName("btnAddImpKey")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
      

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Important Key"))
        self.navViewImpKeyDetails.setText(_translate("MainWindow", "View Important Key Details"))
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
        self.label_7.setText(_translate("MainWindow", "Key Number"))
        self.label_8.setText(_translate("MainWindow", "Key Name"))
        self.label_9.setText(_translate("MainWindow", "Issuing Person P.No/ O.No"))
        self.label_10.setText(_translate("MainWindow", "Name"))
        self.label_11.setText(_translate("MainWindow", "Rank/ Rate"))
        self.label_12.setText(_translate("MainWindow", "Time out"))
        self.label_14.setText(_translate("MainWindow", "Time in"))
        self.lblDataEntrySuccessful.setText(_translate("MainWindow", "Details Saved Successfully!"))
        self.pushButton.setText(_translate("MainWindow", "Important Key Book"))
        self.navViewPersonnel.setText(_translate("MainWindow", "Personnel Data Book"))
        self.label_6.setText(_translate("MainWindow", "Enter Important Key Details"))
        self.btnAddImpKey.setText(_translate("MainWindow", "Add New Important Key Entry"))

#----------------------------------------Backened for Add Important Key Interface----------------------------------------------
        resetKeysGUI(self)
        self.navViewPersonnel.clicked.connect(self.navViewPersonnelMethod)
        self.navViewGenKey.clicked.connect(self.navViewGeneralKeyMethod)
        self.lblDataEntrySuccessful.hide()
        self.tmOut.setTime( QtCore.QTime.currentTime())
        self.tmIn.setTime( QtCore.QTime.currentTime())
        self.btnAddImpKey.clicked.connect(self.addImportantKeyEntry)
        self.edtKeyNumber.textEdited.connect(self.resetSuccess)
        self.edtKeyName.textEdited.connect(self.resetSuccess)
        self.cBoxIssuingPNo.activated.connect(self.resetSuccess)
        self.cBoxIssuingName.activated.connect(self.resetSuccess)
        self.cBoxImpRank.activated.connect(self.resetSuccess)
    def addImportantKeyEntry(self):
            keyNumber=self.edtKeyNumber.text()
            keyName=self.edtKeyName.text()
            issuingPNo=self.cBoxIssuingPNo.currentText()
            issuingName=self.cBoxIssuingName.currentText()
            issuingRank=self.cBoxImpRank.currentText()
            timeOut=self.tmOut.time().toString("h:mm:ss ap")
            timeIn=self.tmOut.time().toString("h:mm:ss ap")
            queryString="INSERT INTO ImportantKeyBook VALUES('"+keyNumber+"',"+"'"+keyName+"',"+"'"+issuingPNo+"',"+"'"+issuingName+"',"+"'"+issuingRank+"',"+"'"+timeOut+"',"+"'"+timeIn+"')"
            print(queryString)
            insertData(self,queryString)
            if(self.lblDataEntrySuccessful.text()!="Details could not be saved!"):
                    self.edtkeyNumber.clear()
                    self.edtKeyName.clear()
                    resetKeysGUI(self)
                    self.tmOut.setTime( QtCore.QTime.currentTime())
                    self.tmIn.setTime( QtCore.QTime.currentTime())      

    def resetSuccess(self):
                self.lblDataEntrySuccessful.hide()
                self.lblDataEntrySuccessful.setStyleSheet("color: green;\n""background-color:#ffffff;\n""font-size: 11pt")

    def navViewPersonnelMethod(self):
             w.change_view(1)    

    def navViewGeneralKeyMethod(self):
             w.change_view(3)    

class AddImportantKeyWidget(QtWidgets.QMainWindow,AddImportantKey ):
    def __init__(self, parent=None):
        super(AddImportantKeyWidget, self).__init__(parent)
        self.setup_AddImportantKey(self)
################################################################### Add Personnel Data Interface ##########################################################################

class AddPersonnelData(object):
    def setup_AddPersonnelData(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.frame.setStyleSheet("background-color: #ffffff")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 280, 768))
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
        self.navViewPersonnelDetails = QtWidgets.QPushButton(self.frame)
        self.navViewPersonnelDetails.setGeometry(QtCore.QRect(1075, 668, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewPersonnelDetails.setFont(font)
        self.navViewPersonnelDetails.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewPersonnelDetails.setStyleSheet("QPushButton\n"
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
        icon.addPixmap(QtGui.QPixmap(":/images/viewDetails.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewPersonnelDetails.setIcon(icon)
        self.navViewPersonnelDetails.setIconSize(QtCore.QSize(25, 25))
        self.navViewPersonnelDetails.setObjectName("navViewPersonnelDetails")
        self.navViewPunishment = QtWidgets.QPushButton(self.frame)
        self.navViewPunishment.setGeometry(QtCore.QRect(10, 512, 260, 44))
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
        self.navViewImpKey.setGeometry(QtCore.QRect(10, 248, 260, 44))
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
        self.navViewGenKey.setGeometry(QtCore.QRect(10, 292, 260, 44))
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
        self.navViewVisitor.setGeometry(QtCore.QRect(10, 336, 260, 44))
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
        self.navViewTransport.setGeometry(QtCore.QRect(10, 380, 260, 44))
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
        self.navViewGangway.setGeometry(QtCore.QRect(10, 424, 260, 44))
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
        self.navViewDuty.setGeometry(QtCore.QRect(10, 468, 260, 44))
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
        self.navViewNight.setGeometry(QtCore.QRect(10, 600, 260, 44))
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
        self.label_4.setGeometry(QtCore.QRect(10, 199, 260, 2))
        self.label_4.setStyleSheet("background-color:#4154A0;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.navViewMOB = QtWidgets.QPushButton(self.frame)
        self.navViewMOB.setGeometry(QtCore.QRect(10, 108, 260, 44))
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
        self.navViewLocation.setGeometry(QtCore.QRect(10, 20, 260, 44))
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
        self.navViewMangement.setGeometry(QtCore.QRect(10, 64, 260, 44))
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
        self.navViewPPE.setGeometry(QtCore.QRect(10, 644, 260, 44))
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
        self.navViewOOD.setGeometry(QtCore.QRect(10, 556, 260, 44))
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
        self.navViewCMS.setGeometry(QtCore.QRect(10, 152, 260, 44))
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
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(331, 152, 191, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.edtID = QtWidgets.QLineEdit(self.frame)
        self.edtID.setGeometry(QtCore.QRect(522, 154, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtID.setFont(font)
        self.edtID.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"  }")
        self.edtID.setObjectName("edtID")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(331, 196, 191, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.edtPNO = QtWidgets.QLineEdit(self.frame)
        self.edtPNO.setGeometry(QtCore.QRect(522, 198, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtPNO.setFont(font)
        self.edtPNO.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"  }")
        self.edtPNO.setObjectName("edtPNO")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(331, 240, 191, 44))
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
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(331, 284, 191, 44))
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
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(331, 328, 191, 44))
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
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(331, 372, 191, 44))
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
        self.lblDataEntrySuccessful = QtWidgets.QLabel(self.frame)
        self.lblDataEntrySuccessful.setEnabled(True)
        self.lblDataEntrySuccessful.setGeometry(QtCore.QRect(331, 426, 361, 44))
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
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/personnelData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon15)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(296, 627, 251, 181))
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
        self.navViewPersonnel.setGeometry(QtCore.QRect(10, 204, 260, 44))
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
        self.navViewPersonnel.setIcon(icon15)
        self.navViewPersonnel.setIconSize(QtCore.QSize(25, 25))
        self.navViewPersonnel.setFlat(False)
        self.navViewPersonnel.setObjectName("navViewPersonnel")
        self.edtRank = QtWidgets.QLineEdit(self.frame)
        self.edtRank.setGeometry(QtCore.QRect(522, 242, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtRank.setFont(font)
        self.edtRank.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"  }")
        self.edtRank.setObjectName("edtRank")
        self.edtName = QtWidgets.QLineEdit(self.frame)
        self.edtName.setGeometry(QtCore.QRect(522, 286, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtName.setFont(font)
        self.edtName.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"  }")
        self.edtName.setObjectName("edtName")
        self.edtDepartment = QtWidgets.QLineEdit(self.frame)
        self.edtDepartment.setGeometry(QtCore.QRect(522, 330, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtDepartment.setFont(font)
        self.edtDepartment.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"  }")
        self.edtDepartment.setObjectName("edtDepartment")
        self.edtBloodGroup = QtWidgets.QLineEdit(self.frame)
        self.edtBloodGroup.setGeometry(QtCore.QRect(522, 374, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtBloodGroup.setFont(font)
        self.edtBloodGroup.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"  }")
        self.edtBloodGroup.setObjectName("edtBloodGroup")
        self.label_2.raise_()
        self.label.raise_()
        self.navViewPersonnelDetails.raise_()
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
        self.label_7.raise_()
        self.edtID.raise_()
        self.label_8.raise_()
        self.edtPNO.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.lblDataEntrySuccessful.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.navViewPersonnel.raise_()
        self.edtRank.raise_()
        self.edtName.raise_()
        self.edtDepartment.raise_()
        self.edtBloodGroup.raise_()
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(296, 100, 1050, 1))
        self.label_13.setStyleSheet("background-color:#A0A0A0;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(296, 60, 221, 31))
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
        self.btnAddPersonnelEntry = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddPersonnelEntry.setGeometry(QtCore.QRect(592, 446, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnAddPersonnelEntry.setFont(font)
        self.btnAddPersonnelEntry.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddPersonnelEntry.setStyleSheet("QPushButton\n"
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
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddPersonnelEntry.setIcon(icon17)
        self.btnAddPersonnelEntry.setIconSize(QtCore.QSize(25, 25))
        self.btnAddPersonnelEntry.setObjectName("btnAddPersonnelEntry")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Personnel Data"))
        self.navViewPersonnelDetails.setText(_translate("MainWindow", "View Personnel Details"))
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
        self.label_7.setText(_translate("MainWindow", "ID.No"))
        self.label_8.setText(_translate("MainWindow", "P.No/ O.No"))
        self.label_9.setText(_translate("MainWindow", "Rank/Rate"))
        self.label_10.setText(_translate("MainWindow", "Name"))
        self.label_11.setText(_translate("MainWindow", "Department"))
        self.label_12.setText(_translate("MainWindow", "Blood Group"))
        self.lblDataEntrySuccessful.setText(_translate("MainWindow", "Details Saved Successfully!"))
        self.pushButton.setText(_translate("MainWindow", "Personnel Data Book"))
        self.navViewPersonnel.setText(_translate("MainWindow", "Personnel Data Book"))
        self.label_6.setText(_translate("MainWindow", "Enter Personnel Details"))
        self.btnAddPersonnelEntry.setText(_translate("MainWindow", "Add New Personnel Entry"))

#----------------------------------------Backened for Add Personnel Interface----------------------------------------------
        self.lblDataEntrySuccessful.hide()
        self.navViewImpKey.clicked.connect(self.navViewImportantKeyMethod)
        self.navViewGenKey.clicked.connect(self.navViewGeneralKeyMethod)
        self.btnAddPersonnelEntry.clicked.connect(self.addPersonnelDataEntry)
        self.edtID.textEdited.connect(self.resetSuccess)
        self.edtPNO.textEdited.connect(self.resetSuccess)
        self.edtRank.textEdited.connect(self.resetSuccess)
        self.edtName.textEdited.connect(self.resetSuccess)
        self.edtDepartment.textEdited.connect(self.resetSuccess)
        self.edtDepartment.textEdited.connect(self.resetSuccess)
    def addPersonnelDataEntry(self):
            persID=self.edtID.text()
            persPno=self.edtPNO.text()
            persRank=self.edtRank.text()
            persName=self.edtName.text()
            persDepart=self.edtDepartment.text()
            persBG=self.edtBloodGroup.text()
            queryString="INSERT INTO PersonnelDataBook VALUES('"+persID+"',"+"'"+persPno+"',"+"'"+persRank+"',"+"'"+persName+"',"+"'"+persDepart+"',"+"'"+persBG+"')"
            print(queryString)
            insertData(self,queryString)
            if(self.lblDataEntrySuccessful.text()!="Details could not be saved!"):
                   resetPersonnelDataGUI(self)

    def navViewImportantKeyMethod(self):
            w.change_view(2)
    def navViewGeneralKeyMethod(self):
             w.change_view(3)    
    def resetSuccess(self):
                self.lblDataEntrySuccessful.hide()
                self.lblDataEntrySuccessful.setStyleSheet("color: green;\n""background-color:#ffffff;\n""font-size: 11pt")
class AddPersonnelDataWidget(QtWidgets.QMainWindow,AddPersonnelData):
    def __init__(self, parent=None):
        super(AddPersonnelDataWidget, self).__init__(parent)
        self.setup_AddPersonnelData(self)


################################################################### Add General Key Interface ##########################################################################

class AddGeneralKey(object):
    def setup_AddGeneralKey(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.frame.setStyleSheet("background-color: #ffffff")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 280, 768))
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
        self.navViewGenKeyDetails = QtWidgets.QPushButton(self.frame)
        self.navViewGenKeyDetails.setGeometry(QtCore.QRect(1075, 668, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewGenKeyDetails.setFont(font)
        self.navViewGenKeyDetails.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewGenKeyDetails.setStyleSheet("QPushButton\n"
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
        icon.addPixmap(QtGui.QPixmap(":/images/viewDetails.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewGenKeyDetails.setIcon(icon)
        self.navViewGenKeyDetails.setIconSize(QtCore.QSize(25, 25))
        self.navViewGenKeyDetails.setObjectName("navViewGenKeyDetails")
        self.navViewPunishment = QtWidgets.QPushButton(self.frame)
        self.navViewPunishment.setGeometry(QtCore.QRect(10, 512, 260, 44))
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
        self.navViewImpKey.setGeometry(QtCore.QRect(10, 248, 260, 44))
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
        self.navViewGenKey.setGeometry(QtCore.QRect(10, 292, 260, 44))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/genKey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewGenKey.setIcon(icon3)
        self.navViewGenKey.setIconSize(QtCore.QSize(25, 25))
        self.navViewGenKey.setFlat(False)
        self.navViewGenKey.setObjectName("navViewGenKey")
        self.navViewVisitor = QtWidgets.QPushButton(self.frame)
        self.navViewVisitor.setGeometry(QtCore.QRect(10, 336, 260, 44))
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
        self.navViewTransport.setGeometry(QtCore.QRect(10, 380, 260, 44))
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
        self.navViewGangway.setGeometry(QtCore.QRect(10, 424, 260, 44))
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
        self.navViewDuty.setGeometry(QtCore.QRect(10, 468, 260, 44))
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
        self.navViewNight.setGeometry(QtCore.QRect(10, 600, 260, 44))
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
        self.label_4.setGeometry(QtCore.QRect(10, 199, 260, 2))
        self.label_4.setStyleSheet("background-color:#4154A0;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.navViewMOB = QtWidgets.QPushButton(self.frame)
        self.navViewMOB.setGeometry(QtCore.QRect(10, 108, 260, 44))
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
        self.navViewLocation.setGeometry(QtCore.QRect(10, 20, 260, 44))
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
        self.navViewMangement.setGeometry(QtCore.QRect(10, 64, 260, 44))
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
        self.navViewPPE.setGeometry(QtCore.QRect(10, 644, 260, 44))
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
        self.navViewOOD.setGeometry(QtCore.QRect(10, 556, 260, 44))
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
        self.navViewCMS.setGeometry(QtCore.QRect(10, 152, 260, 44))
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
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(331, 152, 191, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.edtKeyNumber = QtWidgets.QLineEdit(self.frame)
        self.edtKeyNumber.setGeometry(QtCore.QRect(522, 154, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtKeyNumber.setFont(font)
        self.edtKeyNumber.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"  }")
        self.edtKeyNumber.setObjectName("edtKeyNumber")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(331, 196, 191, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.edtKeyName = QtWidgets.QLineEdit(self.frame)
        self.edtKeyName.setGeometry(QtCore.QRect(522, 198, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtKeyName.setFont(font)
        self.edtKeyName.setStyleSheet("QLineEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QLineEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QLineEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"  }")
        self.edtKeyName.setObjectName("edtKeyName")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(331, 240, 191, 44))
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
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(331, 284, 191, 44))
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
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(331, 328, 191, 44))
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
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(331, 372, 191, 44))
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
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(331, 416, 191, 44))
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
        self.tmOut = QtWidgets.QTimeEdit(self.frame)
        self.tmOut.setGeometry(QtCore.QRect(522, 374, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tmOut.setFont(font)
        self.tmOut.setStyleSheet("QTimeEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:6px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QTimeEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QTimeEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"border-radius: 6;\n"
"  }\n"
"    QTimeEdit::up-button{\n"
" subcontrol-origin: border;\n"
"subcontrol-position: top right;\n"
"width: 25px;\n"
" border: none;\n"
"image: url(:/images/dropUpTime.png);\n"
"}\n"
"QTimeEdit::down-button {\n"
" subcontrol-origin: border;\n"
" subcontrol-position: bottom right;\n"
" width: 25px;\n"
" border: none;\n"
"\n"
"image: url(:/images/dropDownTime.png);\n"
"\n"
"}\n"
"QTimeEdit::down-button:hover {\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
" border-right: 1px solid rgb(0, 0, 0);\n"
"background-color:#e6e6e6;\n"
"    \n"
"}\n"
"QTimeEdit::up-button:hover {\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-top: 1px solid rgb(0, 0, 0);\n"
" border-right: 1px solid rgb(0, 0, 0);\n"
"background-color:#e6e6e6;\n"
"\n"
"}\n"
"QTimeEdit::up-button:focus{\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-top: 1px solid dodgerBlue;\n"
" border-right: 1px solid dodgerBlue;\n"
"\n"
"}\n"
"QTimeEdit::down-button:focus{\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-bottom: 1px solid dodgerBlue;\n"
" border-right: 1px solid dodgerBlue;\n"
"\n"
"}")
        self.tmOut.setCalendarPopup(False)
        self.tmOut.setObjectName("tmOut")
        self.tmIn = QtWidgets.QTimeEdit(self.frame)
        self.tmIn.setGeometry(QtCore.QRect(522, 418, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tmIn.setFont(font)
        self.tmIn.setStyleSheet("QTimeEdit{\n"
"    border:1px solid #aaa;\n"
"    border-radius:6px;\n"
"    outline:none;\n"
"    padding:6px;\n"


"  }\n"
"  QTimeEdit:hover{\n"
"     border:1px solid #000;    \n"

"}\n"
"  QTimeEdit:focus{\n"
"    border-color:dodgerBlue;\n"

"border-radius: 6;\n"
"  }\n"
"    QTimeEdit::up-button{\n"
" subcontrol-origin: border;\n"
"subcontrol-position: top right;\n"
"width: 25px;\n"
" border: none;\n"
"image: url(:/images/dropUpTime.png);\n"
"}\n"
"QTimeEdit::down-button {\n"
" subcontrol-origin: border;\n"
" subcontrol-position: bottom right;\n"
" width: 25px;\n"
" border: none;\n"
"\n"
"image: url(:/images/dropDownTime.png);\n"
"\n"
"}\n"
"QTimeEdit::down-button:hover {\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
" border-right: 1px solid rgb(0, 0, 0);\n"
"background-color:#e6e6e6;\n"
"    \n"
"}\n"
"QTimeEdit::up-button:hover {\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-top: 1px solid rgb(0, 0, 0);\n"
" border-right: 1px solid rgb(0, 0, 0);\n"
"background-color:#e6e6e6;\n"
"\n"
"}\n"
"QTimeEdit::up-button:focus{\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-top: 1px solid dodgerBlue;\n"
" border-right: 1px solid dodgerBlue;\n"
"\n"
"}\n"
"QTimeEdit::down-button:focus{\n"
" border: 1px solid rgba(0, 0, 0, 0%);\n"
"border-bottom: 1px solid dodgerBlue;\n"
" border-right: 1px solid dodgerBlue;\n"
"\n"
"}")
        self.tmIn.setCalendarPopup(False)
        self.tmIn.setObjectName("tmIn")
        self.lblDataEntrySuccessful = QtWidgets.QLabel(self.frame)
        self.lblDataEntrySuccessful.setEnabled(True)
        self.lblDataEntrySuccessful.setGeometry(QtCore.QRect(331, 470, 361, 44))
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
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(296, 627, 251, 181))
        self.pushButton_2.setStyleSheet(" border:1px solid #fff;\n"
"    border-radius:4px;\n"
"    outline:none;")
        self.pushButton_2.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/logoMTIP.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon15)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_2.setObjectName("pushButton_2")
        self.navViewPersonnel = QtWidgets.QPushButton(self.frame)
        self.navViewPersonnel.setGeometry(QtCore.QRect(10, 204, 260, 44))
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
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/personnelData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewPersonnel.setIcon(icon16)
        self.navViewPersonnel.setIconSize(QtCore.QSize(25, 25))
        self.navViewPersonnel.setFlat(False)
        self.navViewPersonnel.setObjectName("navViewPersonnel")
        self.cBoxIssuingName = QtWidgets.QComboBox(self.frame)
        self.cBoxIssuingName.setGeometry(QtCore.QRect(522, 286, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxIssuingName.setFont(font)
        self.cBoxIssuingName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxIssuingName.setStyleSheet("QComboBox{ border-width: 1px;\n"
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

"}\n"
"  QComboBox:focus{\n"
"    border-color:dodgerBlue;\n"

"  }\n"
"")
        self.cBoxIssuingName.setFrame(True)
        self.cBoxIssuingName.setObjectName("cBoxIssuingName")
        self.cBoxIssuingPNo = QtWidgets.QComboBox(self.frame)
        self.cBoxIssuingPNo.setGeometry(QtCore.QRect(522, 242, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxIssuingPNo.setFont(font)
        self.cBoxIssuingPNo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxIssuingPNo.setStyleSheet("QComboBox{ border-width: 1px;\n"
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

"}\n"
"  QComboBox:focus{\n"
"    border-color:dodgerBlue;\n"

"  }\n"
"")
        self.cBoxIssuingPNo.setFrame(True)
        self.cBoxIssuingPNo.setObjectName("cBoxIssuingPNo")
        self.cBoxImpRank = QtWidgets.QComboBox(self.frame)
        self.cBoxImpRank.setGeometry(QtCore.QRect(522, 330, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxImpRank.setFont(font)
        self.cBoxImpRank.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxImpRank.setStyleSheet("QComboBox{ border-width: 1px;\n"
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

"}\n"
"  QComboBox:focus{\n"
"    border-color:dodgerBlue;\n"

"  }\n"
"")
        self.cBoxImpRank.setFrame(True)
        self.cBoxImpRank.setObjectName("cBoxImpRank")
        self.label_2.raise_()
        self.label.raise_()
        self.navViewGenKeyDetails.raise_()
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
        self.label_7.raise_()
        self.edtKeyNumber.raise_()
        self.label_8.raise_()
        self.edtKeyName.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_14.raise_()
        self.tmOut.raise_()
        self.tmIn.raise_()
        self.lblDataEntrySuccessful.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.navViewPersonnel.raise_()
        self.cBoxIssuingName.raise_()
        self.cBoxIssuingPNo.raise_()
        self.cBoxImpRank.raise_()
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(296, 100, 1050, 1))
        self.label_13.setStyleSheet("background-color:#A0A0A0;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(296, 60, 221, 31))
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
        self.btnAddGenKey = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddGenKey.setGeometry(QtCore.QRect(592, 490, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnAddGenKey.setFont(font)
        self.btnAddGenKey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddGenKey.setStyleSheet("QPushButton\n"
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
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddGenKey.setIcon(icon17)
        self.btnAddGenKey.setIconSize(QtCore.QSize(25, 25))
        self.btnAddGenKey.setObjectName("btnAddGenKey")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add General Key"))
        self.navViewGenKeyDetails.setText(_translate("MainWindow", "View General Key Details"))
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
        self.label_7.setText(_translate("MainWindow", "Key Number"))
        self.label_8.setText(_translate("MainWindow", "Key Name"))
        self.label_9.setText(_translate("MainWindow", "Issuing Person P.No/ O.No"))
        self.label_10.setText(_translate("MainWindow", "Name"))
        self.label_11.setText(_translate("MainWindow", "Rank/ Rate"))
        self.label_12.setText(_translate("MainWindow", "Time out"))
        self.label_14.setText(_translate("MainWindow", "Time in"))
        self.lblDataEntrySuccessful.setText(_translate("MainWindow", "Details Saved Successfully!"))
        self.pushButton.setText(_translate("MainWindow", "General Key Book"))
        self.navViewPersonnel.setText(_translate("MainWindow", "Personnel Data Book"))
        self.label_6.setText(_translate("MainWindow", "Enter General Key Details"))
        self.btnAddGenKey.setText(_translate("MainWindow", "Add New General Key Entry"))

#----------------------------------------Backened for Add General Key Interface----------------------------------------------
        resetKeysGUI(self)
        self.navViewPersonnel.clicked.connect(self.navViewPersonnelMethod)
        self.navViewImpKey.clicked.connect(self.navViewImportantKeyMethod)
        self.lblDataEntrySuccessful.hide()
        self.tmOut.setTime( QtCore.QTime.currentTime())
        self.tmIn.setTime( QtCore.QTime.currentTime())
        self.btnAddGenKey.clicked.connect(self.addGeneralKeyEntry)
        self.edtKeyNumber.textEdited.connect(self.resetSuccess)
        self.edtKeyName.textEdited.connect(self.resetSuccess)
        self.cBoxIssuingPNo.activated.connect(self.resetSuccess)
        self.cBoxIssuingName.activated.connect(self.resetSuccess)
        self.cBoxImpRank.activated.connect(self.resetSuccess)
    def addGeneralKeyEntry(self):
            keyNumber=self.edtKeyNumber.text()
            keyName=self.edtKeyName.text()
            issuingPNo=self.cBoxIssuingPNo.currentText()
            issuingName=self.cBoxIssuingName.currentText()
            issuingRank=self.cBoxImpRank.currentText()
            timeOut=self.tmOut.time().toString("h:mm:ss ap")
            timeIn=self.tmOut.time().toString("h:mm:ss ap")
            queryString="INSERT INTO GeneralKeyBook VALUES('"+keyNumber+"',"+"'"+keyName+"',"+"'"+issuingPNo+"',"+"'"+issuingName+"',"+"'"+issuingRank+"',"+"'"+timeOut+"',"+"'"+timeIn+"')"
            print(queryString)
            insertData(self,queryString)
            if(self.lblDataEntrySuccessful.text()!="Details could not be saved!"):
                    resetKeysGUI(self)
                    self.tmOut.setTime( QtCore.QTime.currentTime())
                    self.tmIn.setTime( QtCore.QTime.currentTime())      

    def resetSuccess(self):
                self.lblDataEntrySuccessful.hide()
                self.lblDataEntrySuccessful.setStyleSheet("color: green;\n""background-color:#ffffff;\n""font-size: 11pt")

    def navViewPersonnelMethod(self):
             w.change_view(1)   

    def navViewImportantKeyMethod(self):
             w.change_view(2)    
class AddGeneralKeyWidget(QtWidgets.QMainWindow,AddGeneralKey ):
    def __init__(self, parent=None):
        super(AddGeneralKeyWidget, self).__init__(parent)
        self.setup_AddGeneralKey(self)

############################################################# Add Visitor Interface ######################################################################



#----------------------------------------Backened for Add Visitor Interface----------------------------------------------
############################################################# Main ######################################################################

import IconResource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = App()
    w.resize(1366,768)
    w.setWindowState(QtCore.Qt.WindowMaximized)
    w.show()
    w.change_view(1)
    sys.exit(app.exec_())
