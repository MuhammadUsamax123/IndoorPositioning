class Login(object):
    def setup_Login(self, MainWindow):
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
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(498, 349, 121, 44))
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
        self.edtUsername = QtWidgets.QLineEdit(self.frame)
        self.edtUsername.setGeometry(QtCore.QRect(619, 351, 251, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtUsername.setFont(font)
        self.edtUsername.setStyleSheet("QLineEdit{\n"
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
        self.edtUsername.setObjectName("edtUsername")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(498, 393, 121, 44))
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
        self.edtPassword = QtWidgets.QLineEdit(self.frame)
        self.edtPassword.setGeometry(QtCore.QRect(619, 395, 251, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.edtPassword.setFont(font)
        self.edtPassword.setStyleSheet("QLineEdit{\n"
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
        self.edtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edtPassword.setObjectName("edtPassword")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(498, 437, 121, 44))
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
        self.lblDataEntrySuccessful = QtWidgets.QLabel(self.frame)
        self.lblDataEntrySuccessful.setEnabled(True)
        self.lblDataEntrySuccessful.setGeometry(QtCore.QRect(498, 493, 291, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lblDataEntrySuccessful.setFont(font)
        self.lblDataEntrySuccessful.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblDataEntrySuccessful.setStyleSheet("color: red;\n"
"background-color:#ffffff;\n"
"font-size: 11pt")
        self.lblDataEntrySuccessful.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblDataEntrySuccessful.setObjectName("lblDataEntrySuccessful")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(608, 194, 150, 120))
        self.pushButton_2.setStyleSheet(" border:1px solid #fff;\n"
"    border-radius:4px;\n"
"    outline:none;")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logoMTIPLarge2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.cBoxLoginAs = QtWidgets.QComboBox(self.frame)
        self.cBoxLoginAs.setGeometry(QtCore.QRect(619, 439, 251, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setKerning(True)
        self.cBoxLoginAs.setFont(font)
        self.cBoxLoginAs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cBoxLoginAs.setStyleSheet("QComboBox{ border-width: 1px;\n"
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
        self.cBoxLoginAs.setEditable(False)
        self.cBoxLoginAs.setFrame(True)
        self.cBoxLoginAs.setObjectName("cBoxLoginAs")
        self.cBoxLoginAs.addItem("")
        self.cBoxLoginAs.addItem("")
        self.cBoxLoginAs.addItem("")
        self.cBoxLoginAs.addItem("")
        self.cBoxLoginAs.addItem("")
        self.cBoxLoginAs.addItem("")
        self.cBoxLoginAs.addItem("")
        self.cBoxLoginAs.addItem("")
        self.cBoxLoginAs.addItem("")
        self.btnLogin = QtWidgets.QPushButton(self.frame)
        self.btnLogin.setGeometry(QtCore.QRect(740, 514, 131, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btnLogin.setFont(font)
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet("QPushButton\n"
"{\n"
"    color: #ffffff;\n"
"    background-color:#00B355;\n"
"    border-width: 1px;\n"
"    border-color: #007939;\n"
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
"    background-color:#00D564\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #00B355;\n"
"     border-width: 3px;\n"
"    border-color: #00D564;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogin.setIcon(icon1)
        self.btnLogin.setIconSize(QtCore.QSize(25, 25))
        self.btnLogin.setObjectName("btnLogin")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(448, 174, 471, 421))
        self.label.setStyleSheet("   border:1px solid #aaa;\n"
"    border-radius:4px;\n"
"    outline:none;\n"
"    padding:6px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.pushButton_3.setStyleSheet("background-color: rgba(47, 60, 113, 0.6);")
        self.pushButton_3.setText("")
        self.pushButton_3.setIconSize(QtCore.QSize(1366, 768))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.pushButton_4.setStyleSheet(" border:1px solid #fff;\n"
"    border-radius:4px;\n"
"    outline:none;")
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/shipBackground.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(1366, 768))
        self.pushButton_4.setObjectName("pushButton_4")
        self.btnShutdown = QtWidgets.QPushButton(self.frame)
        self.btnShutdown.setEnabled(True)
        self.btnShutdown.setGeometry(QtCore.QRect(1310, 707, 50, 51))
        self.btnShutdown.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnShutdown.setStyleSheet("QPushButton\n"
"{\n"
"    color: #ffffff;\n"
"    background-color:#E3322C;\n"
"    border-width: 1px;\n"
"    border-color: #E6150B;\n"
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
"    background-color:#F87169\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #E3322C;\n"
"     border-width: 3px;\n"
"    border-color: #F87169;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"\n"
"}")
        self.btnShutdown.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/shutDown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnShutdown.setIcon(icon3)
        self.btnShutdown.setIconSize(QtCore.QSize(32, 32))
        self.btnShutdown.setObjectName("btnShutdown")
        self.pushButton_4.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.edtUsername.raise_()
        self.label_7.raise_()
        self.edtPassword.raise_()
        self.label_8.raise_()
        self.cBoxLoginAs.raise_()
        self.label_9.raise_()
        self.lblDataEntrySuccessful.raise_()
        self.btnLogin.raise_()
        self.pushButton_2.raise_()
        self.btnShutdown.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Usename"))
        self.label_8.setText(_translate("MainWindow", "Password"))
        self.label_9.setText(_translate("MainWindow", "Login as"))
        self.lblDataEntrySuccessful.setText(_translate("MainWindow", "Incorrect Username or Password!"))
        self.cBoxLoginAs.setItemText(0, _translate("MainWindow", "Commanding Officer Secretary"))
        self.cBoxLoginAs.setItemText(1, _translate("MainWindow", "Commanding Officer"))
        self.cBoxLoginAs.setItemText(2, _translate("MainWindow", "Executive Officer"))
        self.cBoxLoginAs.setItemText(3, _translate("MainWindow", "Weapon Engineering Officer"))
        self.cBoxLoginAs.setItemText(4, _translate("MainWindow", "Marine Engineering Officer"))
        self.cBoxLoginAs.setItemText(5, _translate("MainWindow", "Supply Officer"))
        self.cBoxLoginAs.setItemText(6, _translate("MainWindow", "Principal Warfare Officer"))
        self.cBoxLoginAs.setItemText(7, _translate("MainWindow", "Officer of the Day"))
        self.cBoxLoginAs.setItemText(8, _translate("MainWindow", "Officer on Watch"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
