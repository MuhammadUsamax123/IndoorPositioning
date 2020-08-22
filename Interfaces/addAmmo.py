class AddAmmo(object):
    def setup_AddAmmo(self, MainWindow):
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
        self.pushButton.setGeometry(QtCore.QRect(1059, 5, 281, 35))
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
        self.navAddWeapon = QtWidgets.QPushButton(self.frame)
        self.navAddWeapon.setGeometry(QtCore.QRect(1080, 160, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navAddWeapon.setFont(font)
        self.navAddWeapon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navAddWeapon.setStyleSheet("QPushButton\n"
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
        self.navAddWeapon.setIcon(icon18)
        self.navAddWeapon.setIconSize(QtCore.QSize(25, 25))
        self.navAddWeapon.setObjectName("navAddWeapon")
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
        self.navViewStateArmory.setIcon(icon14)
        self.navViewStateArmory.setIconSize(QtCore.QSize(25, 25))
        self.navViewStateArmory.setFlat(False)
        self.navViewStateArmory.setObjectName("navViewStateArmory")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(331, 164, 191, 44))
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
        self.lblDataEntrySuccessful = QtWidgets.QLabel(self.frame)
        self.lblDataEntrySuccessful.setEnabled(True)
        self.lblDataEntrySuccessful.setGeometry(QtCore.QRect(331, 218, 361, 44))
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
        self.edtAmmoQuantity = QtWidgets.QLineEdit(self.frame)
        self.edtAmmoQuantity.setGeometry(QtCore.QRect(522, 166, 345, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtAmmoQuantity.setFont(font)
        self.edtAmmoQuantity.setStyleSheet("QLineEdit{\n"
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
        self.edtAmmoQuantity.setObjectName("edtAmmoQuantity")
        self.btnAddAmmo = QtWidgets.QPushButton(self.frame)
        self.btnAddAmmo.setGeometry(QtCore.QRect(600, 241, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnAddAmmo.setFont(font)
        self.btnAddAmmo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddAmmo.setStyleSheet("QPushButton\n"
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
        self.btnAddAmmo.setIcon(icon18)
        self.btnAddAmmo.setIconSize(QtCore.QSize(25, 25))
        self.btnAddAmmo.setObjectName("btnAddAmmo")
        self.navArmState = QtWidgets.QPushButton(self.frame)
        self.navArmState.setGeometry(QtCore.QRect(1080, 110, 271, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.navArmState.setFont(font)
        self.navArmState.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navArmState.setStyleSheet("QPushButton\n"
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
        self.navArmState.setIcon(icon14)
        self.navArmState.setIconSize(QtCore.QSize(25, 25))
        self.navArmState.setObjectName("navArmState")
        self.cBoxAmmoType = QtWidgets.QComboBox(self.frame)
        self.cBoxAmmoType.setGeometry(QtCore.QRect(522, 120, 345, 38))
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
        self.cBoxAmmoType.addItem("")
        self.cBoxAmmoType.addItem("")
        self.cBoxAmmoType.addItem("")
        self.cBoxAmmoType.addItem("")
        self.cBoxAmmoType.addItem("")
        self.cBoxAmmoType.addItem("")
        self.cBoxAmmoType.addItem("")
        self.cBoxAmmoType.addItem("")
        self.cBoxAmmoType.addItem("")
        self.navAddEquipment = QtWidgets.QPushButton(self.frame)
        self.navAddEquipment.setGeometry(QtCore.QRect(1080, 210, 271, 44))
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
        self.navAddEquipment.setObjectName("navAddEquipment")
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
        self.navAddWeapon.raise_()
        self.navViewStateArmory.raise_()
        self.label_14.raise_()
        self.lblDataEntrySuccessful.raise_()
        self.edtAmmoQuantity.raise_()
        self.btnAddAmmo.raise_()
        self.navArmState.raise_()
        self.cBoxAmmoType.raise_()
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
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(331, 120, 191, 44))
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
        self.navAddWeapon.setText(_translate("MainWindow", "Add Weapon    "))
        self.navViewStateArmory.setText(_translate("MainWindow", "Armory State Management System"))
        self.label_14.setText(_translate("MainWindow", "Quantity"))
        self.lblDataEntrySuccessful.setText(_translate("MainWindow", "Details Saved Successfully!"))
        self.btnAddAmmo.setText(_translate("MainWindow", "Add Ammo"))
        self.navArmState.setText(_translate("MainWindow", "Armory State Management System"))
        self.cBoxAmmoType.setItemText(0, _translate("MainWindow", "Commanding Officer Secretary"))
        self.cBoxAmmoType.setItemText(1, _translate("MainWindow", "Commanding Officer"))
        self.cBoxAmmoType.setItemText(2, _translate("MainWindow", "Executive Officer"))
        self.cBoxAmmoType.setItemText(3, _translate("MainWindow", "Weapon Engineering Officer"))
        self.cBoxAmmoType.setItemText(4, _translate("MainWindow", "Marine Engineering Officer"))
        self.cBoxAmmoType.setItemText(5, _translate("MainWindow", "Supply Officer"))
        self.cBoxAmmoType.setItemText(6, _translate("MainWindow", "Principal Warfare Officer"))
        self.cBoxAmmoType.setItemText(7, _translate("MainWindow", "Officer of the Day"))
        self.cBoxAmmoType.setItemText(8, _translate("MainWindow", "Officer on Watch"))
        self.navAddEquipment.setText(_translate("MainWindow", "Add Equipment"))
        self.label_6.setText(_translate("MainWindow", "Enter Ammo Details"))
        self.label_7.setText(_translate("MainWindow", "Ammo Type"))