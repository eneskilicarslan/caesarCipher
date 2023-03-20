# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5101.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1294, 1096)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.cipherText = QtWidgets.QPlainTextEdit(self.widget)
        self.cipherText.setObjectName("cipherText")
        self.verticalLayout_5.addWidget(self.cipherText)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cipherButton = QtWidgets.QPushButton(self.widget)
        self.cipherButton.setObjectName("cipherButton")
        self.horizontalLayout_5.addWidget(self.cipherButton)
        self.analyzeCipherButton = QtWidgets.QPushButton(self.widget)
        self.analyzeCipherButton.setObjectName("analyzeCipherButton")
        self.horizontalLayout_5.addWidget(self.analyzeCipherButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.cipherView = QtWidgets.QLabel(self.widget)
        self.cipherView.setMinimumSize(QtCore.QSize(622, 369))
        self.cipherView.setMaximumSize(QtCore.QSize(622, 369))
        self.cipherView.setText("")
        self.cipherView.setPixmap(QtGui.QPixmap("dido.jpg"))
        self.cipherView.setScaledContents(True)
        self.cipherView.setObjectName("cipherView")
        self.horizontalLayout_3.addWidget(self.cipherView)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setLineWidth(10)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.analysisText = QtWidgets.QPlainTextEdit(self.widget)
        self.analysisText.setObjectName("analysisText")
        self.verticalLayout_4.addWidget(self.analysisText)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.analyzeView = QtWidgets.QLabel(self.widget)
        self.analyzeView.setMinimumSize(QtCore.QSize(622, 369))
        self.analyzeView.setMaximumSize(QtCore.QSize(622, 369))
        self.analyzeView.setText("")
        self.analyzeView.setPixmap(QtGui.QPixmap("kop.jpeg"))
        self.analyzeView.setScaledContents(True)
        self.analyzeView.setObjectName("analyzeView")
        self.horizontalLayout_4.addWidget(self.analyzeView)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.decipherButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decipherButton.sizePolicy().hasHeightForWidth())
        self.decipherButton.setSizePolicy(sizePolicy)
        self.decipherButton.setObjectName("decipherButton")
        self.verticalLayout.addWidget(self.decipherButton)
        self.decipheredText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.decipheredText.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decipheredText.sizePolicy().hasHeightForWidth())
        self.decipheredText.setSizePolicy(sizePolicy)
        self.decipheredText.setMinimumSize(QtCore.QSize(0, 40))
        self.decipheredText.setMaximumSize(QtCore.QSize(16777215, 140))
        self.decipheredText.setObjectName("decipheredText")
        self.verticalLayout.addWidget(self.decipheredText)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.performanceScore = QtWidgets.QLineEdit(self.centralwidget)
        self.performanceScore.setAlignment(QtCore.Qt.AlignCenter)
        self.performanceScore.setObjectName("performanceScore")
        self.horizontalLayout_7.addWidget(self.performanceScore)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1294, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Kriptolanacak Metin"))
        self.cipherButton.setText(_translate("MainWindow", "Kriptola"))
        self.analyzeCipherButton.setText(_translate("MainWindow", "Analiz Et"))
        self.label.setText(_translate("MainWindow", "Analiz Metni"))
        self.pushButton_2.setText(_translate("MainWindow", "Analiz Et"))
        self.decipherButton.setText(_translate("MainWindow", "ÇÖZ"))
        self.performanceScore.setPlaceholderText(_translate("MainWindow", "Performans Skoru"))