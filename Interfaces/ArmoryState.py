class ArmoryStateManagement(object):
    def setup_ArmoryStateManagement(self, MainWindow):
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
        self.label.setStyleSheet("\n"
"background-color:#2F3C71;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1366, 44))
        self.label_2.setStyleSheet("\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 11pt;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 11pt;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"    outline:none;\n"
"}\n"
"QPushButton:active\n"
"{\n"
"    background-color:#4154A0;\n"
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
"    outline:none;\n"
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
"    outline:none;\n"
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
        self.pushButton.setGeometry(QtCore.QRect(1049, 5, 291, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" text-align: right;\n"
"    color: #ffffff;\n"
"    background-color:#222222;")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/armory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(316, 680, 100, 80))
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
"    outline:none;\n"
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
"    outline:none;\n"
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
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/armoryState.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navViewStatePersonnel.setIcon(icon17)
        self.navViewStatePersonnel.setIconSize(QtCore.QSize(25, 25))
        self.navViewStatePersonnel.setFlat(False)
        self.navViewStatePersonnel.setObjectName("navViewStatePersonnel")
        self.navAddAmmo = QtWidgets.QPushButton(self.frame)
        self.navAddAmmo.setGeometry(QtCore.QRect(1065, 160, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navAddAmmo.setFont(font)
        self.navAddAmmo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navAddAmmo.setStyleSheet("QPushButton\n"
"{\n"
"    color: #ffffff;\n"
"    background-color:#4154A0;\n"
"    border-width: 1px;\n"
"    border-color: #4154A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    outline:none;\n"
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
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navAddAmmo.setIcon(icon18)
        self.navAddAmmo.setIconSize(QtCore.QSize(25, 25))
        self.navAddAmmo.setObjectName("navViewSmallPPEDetails")
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
"    outline:none;\n"
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
        self.navViewStateArmory.setIcon(icon14)
        self.navViewStateArmory.setIconSize(QtCore.QSize(25, 25))
        self.navViewStateArmory.setFlat(False)
        self.navViewStateArmory.setObjectName("navViewStateArmory")
        self.navViewAddSmallPPE = QtWidgets.QPushButton(self.frame)
        self.navViewAddSmallPPE.setGeometry(QtCore.QRect(1065, 110, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navViewAddSmallPPE.setFont(font)
        self.navViewAddSmallPPE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navViewAddSmallPPE.setStyleSheet("QPushButton\n"
"{\n"
"    color: #ffffff;\n"
"    background-color:#4154A0;\n"
"    border-width: 1px;\n"
"    border-color: #4154A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    outline:none;\n"
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
        self.navViewAddSmallPPE.setIcon(icon18)
        self.navViewAddSmallPPE.setIconSize(QtCore.QSize(25, 25))
        self.navViewAddSmallPPE.setObjectName("navViewAddSmallPPE")
        self.navAddEquipment = QtWidgets.QPushButton(self.frame)
        self.navAddEquipment.setGeometry(QtCore.QRect(1065, 210, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navAddEquipment.setFont(font)
        self.navAddEquipment.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navAddEquipment.setStyleSheet("QPushButton\n"
"{\n"
"    color: #ffffff;\n"
"    background-color:#4154A0;\n"
"    border-width: 1px;\n"
"    border-color: #4154A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    outline:none;\n"
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
        self.navAddEquipment.setIcon(icon18)
        self.navAddEquipment.setIconSize(QtCore.QSize(25, 25))
        self.navAddEquipment.setObjectName("navViewSmallPPEDetails_2")
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
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.navViewPersonnel.raise_()
        self.navViewStatePersonnel.raise_()
        self.navAddAmmo.raise_()
        self.navViewStateArmory.raise_()
        self.navViewAddSmallPPE.raise_()
        self.navAddEquipment.raise_()
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(316, 100, 1020, 1))
        self.label_13.setStyleSheet("background-color:#A0A0A0;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(316, 60, 391, 31))
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
        self.lblTotalAmmo = QtWidgets.QLabel(self.centralwidget)
        self.lblTotalAmmo.setGeometry(QtCore.QRect(631, 140, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblTotalAmmo.setFont(font)
        self.lblTotalAmmo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTotalAmmo.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblTotalAmmo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTotalAmmo.setObjectName("lblTotalAmmo")
        self.lblTotalEquipment = QtWidgets.QLabel(self.centralwidget)
        self.lblTotalEquipment.setGeometry(QtCore.QRect(845, 140, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblTotalEquipment.setFont(font)
        self.lblTotalEquipment.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTotalEquipment.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblTotalEquipment.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTotalEquipment.setObjectName("lblTotalEquipment")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(331, 108, 141, 44))
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
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(346, 141, 81, 44))
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
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(550, 140, 81, 44))
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
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(754, 140, 91, 44))
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
        self.lblTotalWeapons = QtWidgets.QLabel(self.centralwidget)
        self.lblTotalWeapons.setGeometry(QtCore.QRect(427, 141, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblTotalWeapons.setFont(font)
        self.lblTotalWeapons.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTotalWeapons.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblTotalWeapons.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTotalWeapons.setObjectName("lblTotalWeapons")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(321, 130, 681, 65))
        self.label_16.setStyleSheet("    background-color:#ffff;\n"
"    border-width: 1px;\n"
"    border-color: #A0A0A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(330, 208, 141, 44))
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
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(345, 241, 159, 44))
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
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(320, 230, 681, 111))
        self.label_20.setStyleSheet("    background-color:#ffff;\n"
"    border-width: 1px;\n"
"    border-color: #A0A0A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.lblReturnedWeapons = QtWidgets.QLabel(self.centralwidget)
        self.lblReturnedWeapons.setGeometry(QtCore.QRect(630, 284, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblReturnedWeapons.setFont(font)
        self.lblReturnedWeapons.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblReturnedWeapons.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblReturnedWeapons.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblReturnedWeapons.setObjectName("lblReturnedWeapons")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(345, 285, 81, 44))
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
        self.lblNotReturnedWeapons = QtWidgets.QLabel(self.centralwidget)
        self.lblNotReturnedWeapons.setGeometry(QtCore.QRect(862, 284, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblNotReturnedWeapons.setFont(font)
        self.lblNotReturnedWeapons.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblNotReturnedWeapons.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblNotReturnedWeapons.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblNotReturnedWeapons.setObjectName("lblNotReturnedWeapons")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(549, 284, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_17.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(753, 284, 101, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_21.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.lblIssuedWeapon = QtWidgets.QLabel(self.centralwidget)
        self.lblIssuedWeapon.setGeometry(QtCore.QRect(426, 285, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblIssuedWeapon.setFont(font)
        self.lblIssuedWeapon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblIssuedWeapon.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblIssuedWeapon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblIssuedWeapon.setObjectName("lblIssuedWeapon")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(321, 376, 681, 111))
        self.label_22.setStyleSheet("    background-color:#ffff;\n"
"    border-width: 1px;\n"
"    border-color: #A0A0A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.lblAmmoQuantity = QtWidgets.QLabel(self.centralwidget)
        self.lblAmmoQuantity.setGeometry(QtCore.QRect(427, 431, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblAmmoQuantity.setFont(font)
        self.lblAmmoQuantity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblAmmoQuantity.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblAmmoQuantity.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblAmmoQuantity.setObjectName("lblAmmoQuantity")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(346, 387, 159, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_24.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(331, 354, 141, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_25.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(550, 430, 81, 44))
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
        self.lblConsumedAmmo = QtWidgets.QLabel(self.centralwidget)
        self.lblConsumedAmmo.setGeometry(QtCore.QRect(631, 430, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblConsumedAmmo.setFont(font)
        self.lblConsumedAmmo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblConsumedAmmo.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblConsumedAmmo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblConsumedAmmo.setObjectName("lblConsumedAmmo")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(346, 431, 81, 44))
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
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(321, 516, 681, 111))
        self.label_23.setStyleSheet("    background-color:#ffff;\n"
"    border-width: 1px;\n"
"    border-color: #A0A0A0;\n"
"    border-style: solid;\n"
"    border-radius: 6;")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(751, 570, 101, 44))
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
        self.lblIssuedEquipment = QtWidgets.QLabel(self.centralwidget)
        self.lblIssuedEquipment.setGeometry(QtCore.QRect(427, 571, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblIssuedEquipment.setFont(font)
        self.lblIssuedEquipment.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblIssuedEquipment.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblIssuedEquipment.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblIssuedEquipment.setObjectName("lblIssuedEquipment")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(331, 494, 141, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_29.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(346, 527, 111, 44))
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
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(550, 570, 81, 44))
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
        self.lblReturnedEquipment = QtWidgets.QLabel(self.centralwidget)
        self.lblReturnedEquipment.setGeometry(QtCore.QRect(631, 570, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblReturnedEquipment.setFont(font)
        self.lblReturnedEquipment.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblReturnedEquipment.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblReturnedEquipment.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblReturnedEquipment.setObjectName("lblReturnedEquipment")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(346, 571, 81, 44))
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
        self.lblNotReturnedEquipment = QtWidgets.QLabel(self.centralwidget)
        self.lblNotReturnedEquipment.setGeometry(QtCore.QRect(863, 570, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblNotReturnedEquipment.setFont(font)
        self.lblNotReturnedEquipment.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblNotReturnedEquipment.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblNotReturnedEquipment.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblNotReturnedEquipment.setObjectName("lblNotReturnedEquipment")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(753, 240, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_33.setFont(font)
        self.label_33.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_33.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.lblTotalWeapon = QtWidgets.QLabel(self.centralwidget)
        self.lblTotalWeapon.setGeometry(QtCore.QRect(862, 240, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblTotalWeapon.setFont(font)
        self.lblTotalWeapon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTotalWeapon.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblTotalWeapon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTotalWeapon.setObjectName("lblTotalWeapon")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(752, 526, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_34.setFont(font)
        self.label_34.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_34.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.lblTotalWeaponEquipments = QtWidgets.QLabel(self.centralwidget)
        self.lblTotalWeaponEquipments.setGeometry(QtCore.QRect(861, 526, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblTotalWeaponEquipments.setFont(font)
        self.lblTotalWeaponEquipments.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTotalWeaponEquipments.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblTotalWeaponEquipments.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTotalWeaponEquipments.setObjectName("lblTotalWeaponEquipments")
        self.lblTotalAmmos = QtWidgets.QLabel(self.centralwidget)
        self.lblTotalAmmos.setGeometry(QtCore.QRect(862, 386, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblTotalAmmos.setFont(font)
        self.lblTotalAmmos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTotalAmmos.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblTotalAmmos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTotalAmmos.setObjectName("lblTotalAmmos")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(753, 386, 81, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_35.setFont(font)
        self.label_35.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_35.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.cBoxWeaponType = QtWidgets.QComboBox(self.centralwidget)
        self.cBoxWeaponType.setGeometry(QtCore.QRect(460, 243, 241, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxWeaponType.setFont(font)
        self.cBoxWeaponType.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxWeaponType.setStyleSheet("QComboBox{ border-width: 1px;\n"
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
        self.cBoxWeaponType.setEditable(False)
        self.cBoxWeaponType.setFrame(True)
        self.cBoxWeaponType.setObjectName("cBoxWeaponType")
        self.cBoxAmmoType = QtWidgets.QComboBox(self.centralwidget)
        self.cBoxAmmoType.setGeometry(QtCore.QRect(460, 390, 241, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxAmmoType.setFont(font)
        self.cBoxAmmoType.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxAmmoType.setStyleSheet("QComboBox{ border-width: 1px;\n"
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
        self.cBoxAmmoType.setEditable(False)
        self.cBoxAmmoType.setFrame(True)
        self.cBoxAmmoType.setObjectName("cBoxAmmoType")
        self.cBoxEquipmentType = QtWidgets.QComboBox(self.centralwidget)
        self.cBoxEquipmentType.setGeometry(QtCore.QRect(460, 530, 241, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxEquipmentType.setFont(font)
        self.cBoxEquipmentType.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxEquipmentType.setStyleSheet("QComboBox{ border-width: 1px;\n"
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
        self.cBoxEquipmentType.setEditable(False)
        self.cBoxEquipmentType.setFrame(True)
        self.cBoxEquipmentType.setObjectName("cBoxEquipmentType")
        self.btnLogout = QtWidgets.QPushButton(self.frame)
        self.btnLogout.setGeometry(QtCore.QRect(326, 0, 111, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnLogout.setFont(font)
        self.btnLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogout.setStyleSheet("QPushButton \n"
"{\n"
"    outline:none;\n"
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
        
        self.frame.raise_()
        self.label_13.raise_()
        self.label_6.raise_()
        self.label_16.raise_()
        self.label_18.raise_()
        self.lblTotalAmmo.raise_()
        self.label_12.raise_()
        self.lblTotalEquipment.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.lblTotalWeapons.raise_()
        self.label_20.raise_()
        self.label_14.raise_()
        self.label_19.raise_()
        self.lblReturnedWeapons.raise_()
        self.label_15.raise_()
        self.lblNotReturnedWeapons.raise_()
        self.label_17.raise_()
        self.label_21.raise_()
        self.lblIssuedWeapon.raise_()
        self.label_22.raise_()
        self.lblAmmoQuantity.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.lblConsumedAmmo.raise_()
        self.label_27.raise_()
        self.label_23.raise_()
        self.label_28.raise_()
        self.lblIssuedEquipment.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.lblReturnedEquipment.raise_()
        self.label_32.raise_()
        self.lblNotReturnedEquipment.raise_()
        self.label_33.raise_()
        self.lblTotalWeapon.raise_()
        self.label_34.raise_()
        self.lblTotalWeaponEquipments.raise_()
        self.lblTotalAmmos.raise_()
        self.btnLogout.raise_()
        self.label_35.raise_()
        self.cBoxWeaponType.raise_()
        self.cBoxAmmoType.raise_()
        self.cBoxEquipmentType.raise_()
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
        self.pushButton.setText(_translate("MainWindow", "Armory State Management System"))
        self.navViewPersonnel.setText(_translate("MainWindow", "Personnel Data Book"))
        self.navViewStatePersonnel.setText(_translate("MainWindow", "Personnel State Management System"))
        self.navAddAmmo.setText(_translate("MainWindow", "Add Ammo.      "))
        self.navViewStateArmory.setText(_translate("MainWindow", "Armory State Management System"))
        self.navViewAddSmallPPE.setText(_translate("MainWindow", "Add Weapons    "))
        self.navAddEquipment.setText(_translate("MainWindow", "Add Equipment"))
        self.label_6.setText(_translate("MainWindow", "Armory State Details"))
        self.lblTotalAmmo.setText(_translate("MainWindow", "0"))
        self.lblTotalEquipment.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "Total Armory"))
        self.label_12.setText(_translate("MainWindow", "Weapons:"))
        self.label_10.setText(_translate("MainWindow", "Ammo:"))
        self.label_11.setText(_translate("MainWindow", "Equipment:"))
        self.lblTotalWeapons.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "Weapons"))
        self.label_14.setText(_translate("MainWindow", "Weapon Type"))
        self.lblReturnedWeapons.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "Issued:"))
        self.lblNotReturnedWeapons.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "Returned:"))
        self.label_21.setText(_translate("MainWindow", "Not Returned:"))
        self.lblIssuedWeapon.setText(_translate("MainWindow", "0"))
        self.lblAmmoQuantity.setText(_translate("MainWindow", "0"))
        self.label_24.setText(_translate("MainWindow", "Ammo. Type"))
        self.label_25.setText(_translate("MainWindow", "Ammo."))
        self.label_26.setText(_translate("MainWindow", "Consumed:"))
        self.lblConsumedAmmo.setText(_translate("MainWindow", "0"))
        self.label_27.setText(_translate("MainWindow", "Quanity:"))
        self.label_28.setText(_translate("MainWindow", "Not Returned:"))
        self.lblIssuedEquipment.setText(_translate("MainWindow", "0"))
        self.label_29.setText(_translate("MainWindow", "Equipment"))
        self.label_30.setText(_translate("MainWindow", "Equipment Type"))
        self.label_31.setText(_translate("MainWindow", "Returned:"))
        self.lblReturnedEquipment.setText(_translate("MainWindow", "0"))
        self.label_32.setText(_translate("MainWindow", "Issued:"))
        self.lblNotReturnedEquipment.setText(_translate("MainWindow", "0"))
        self.label_33.setText(_translate("MainWindow", "Total:"))
        self.lblTotalWeapon.setText(_translate("MainWindow", "0"))
        self.label_34.setText(_translate("MainWindow", "Total:"))
        self.lblTotalWeaponEquipments.setText(_translate("MainWindow", "0"))
        self.lblTotalAmmos.setText(_translate("MainWindow", "0"))
        self.label_35.setText(_translate("MainWindow", "Total:"))
        self.btnLogout.setText(_translate("MainWindow", "Logout"))