import collections

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import funcs


class Ui_MainWindow(object):
    def __init__(self):
        self.MainWindow = None
        self.freqAnalysis = None
        self.freqCipher = None
        self.nonCipherInput = ""
        self.analyze1 = 0
        self.analyze2 = 0
        self.seed = 0
        self.blockText = ""

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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cipherText.setFont(font)
        self.cipherText.setObjectName("cipherText")
        self.verticalLayout_5.addWidget(self.cipherText)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.key = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key.sizePolicy().hasHeightForWidth())
        self.key.setSizePolicy(sizePolicy)
        self.key.setMaximum(29)
        self.key.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.key.setObjectName("key")
        self.horizontalLayout_8.addWidget(self.key)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_8)
        self.cipherButton = QtWidgets.QPushButton(self.widget)
        self.cipherButton.setObjectName("cipherButton")
        self.horizontalLayout_5.addWidget(self.cipherButton)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setMaximum(99999)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_5.addWidget(self.spinBox)
        self.blockCipher = QtWidgets.QPushButton(self.widget)
        self.blockCipher.setObjectName("blockCipher")
        self.horizontalLayout_5.addWidget(self.blockCipher)
        self.analyzeCipherButton = QtWidgets.QPushButton(self.widget)
        self.analyzeCipherButton.setObjectName("analyzeCipherButton")
        self.horizontalLayout_5.addWidget(self.analyzeCipherButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.cipherView = QtWidgets.QLabel(self.widget)
        self.cipherView.setMinimumSize(QtCore.QSize(622, 369))
        self.cipherView.setMaximumSize(QtCore.QSize(622, 369))
        self.cipherView.setText("")
        self.cipherView.setPixmap(QtGui.QPixmap("key.jpeg"))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.analysisText.setFont(font)
        self.analysisText.setObjectName("analysisText")
        self.verticalLayout_4.addWidget(self.analysisText)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.fromTxtButton = QtWidgets.QPushButton(self.widget)
        self.fromTxtButton.setObjectName("fromTxtButton")
        self.horizontalLayout_9.addWidget(self.fromTxtButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.analyzeView = QtWidgets.QLabel(self.widget)
        self.analyzeView.setMinimumSize(QtCore.QSize(622, 369))
        self.analyzeView.setMaximumSize(QtCore.QSize(622, 369))
        self.analyzeView.setText("")
        self.analyzeView.setPixmap(QtGui.QPixmap("key.jpeg"))
        self.analyzeView.setScaledContents(True)
        self.analyzeView.setObjectName("analyzeView")
        self.horizontalLayout_4.addWidget(self.analyzeView)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.widget)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.decipherButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decipherButton.sizePolicy().hasHeightForWidth())
        self.decipherButton.setSizePolicy(sizePolicy)
        self.decipherButton.setObjectName("decipherButton")
        self.horizontalLayout_10.addWidget(self.decipherButton)
        self.blockDecipherButton = QtWidgets.QPushButton(self.centralwidget)
        self.blockDecipherButton.setObjectName("blockDecipherButton")
        self.horizontalLayout_10.addWidget(self.blockDecipherButton)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.decipheredText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.decipheredText.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decipheredText.sizePolicy().hasHeightForWidth())
        self.decipheredText.setSizePolicy(sizePolicy)
        self.decipheredText.setMinimumSize(QtCore.QSize(0, 40))
        self.decipheredText.setMaximumSize(QtCore.QSize(16777215, 140))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.decipheredText.setFont(font)
        self.decipheredText.setObjectName("decipheredText")
        self.verticalLayout.addWidget(self.decipheredText)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.performanceScore = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.performanceScore.sizePolicy().hasHeightForWidth())
        self.performanceScore.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.performanceScore.setFont(font)
        self.performanceScore.setAlignment(QtCore.Qt.AlignCenter)
        self.performanceScore.setObjectName("performanceScore")
        self.horizontalLayout_7.addWidget(self.performanceScore)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
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

        """ GUI RELATED """
        self.blockCipher.clicked.connect(self.cipherADV_ECB)
        self.cipherButton.clicked.connect(self.cipher)
        self.MainWindow = MainWindow
        self.freqCipher = collections.OrderedDict
        self.freqAnalysis = collections.OrderedDict
        self.analyzeCipherButton.clicked.connect(self.analyze)
        self.pushButton_2.clicked.connect(self.analyze)  # TODO: safe rework here!
        self.decipherButton.clicked.connect(self.decipher)
        self.decipherButton.setEnabled(False)
        self.blockDecipherButton.clicked.connect(self.blockDecipherADV_ECB)
        self.blockDecipherButton.setEnabled(False)
        self.fromTxtButton.clicked.connect(self.loadFromFile)

    def cipherADV_ECB(self):
        """ciphering"""
        textToCipher = self.cipherText.toPlainText()
        boyut = self.spinBox.value()
        self.nonCipherInput = textToCipher

        self.seed = funcs.randomBinaryGenerator(boyut)
        self.cipherText.clear()

        self.blockText = funcs.blockCipher(self.seed, textToCipher, boyut)
        self.cipherText.insertPlainText(self.blockText)

    def cipher(self):
        """ciphering"""
        textToCipher = self.cipherText.toPlainText()
        keyToShift = self.key.value()

        self.nonCipherInput = textToCipher  # variable that holds initial input to criticise score
        self.cipherText.clear()
        self.cipherText.insertPlainText(funcs.caesarCipher(textToCipher, keyToShift))

    def analyze(self):
        sender = self.MainWindow.sender()
        if sender.objectName() == "analyzeCipherButton":
            self.freqCipher = funcs.freqAnalysis(self.cipherText.toPlainText(), "1.png")
            self.cipherView.setPixmap(QtGui.QPixmap("1.png"))
            if self.freqCipher:
                self.analyze1 = 1
        else:
            self.freqAnalysis = funcs.freqAnalysis(self.analysisText.toPlainText(), "2.png")
            self.analyzeView.setPixmap(QtGui.QPixmap("2.png"))
            if self.freqAnalysis:
                self.analyze2 = 1

        if self.analyze1 and self.analyze2:
            self.decipherButton.setDisabled(False)
            self.blockDecipherButton.setDisabled(False)

    def decipher(self):
        decipheredResult = funcs.decipherZipped(self.cipherText.toPlainText(),
                                                funcs.compareFreqs(self.freqCipher, self.freqAnalysis))
        self.decipheredText.clear()
        self.decipheredText.insertPlainText(decipheredResult)
        self.score()

    def blockDecipherADV_ECB(self):
        decipheredResult = funcs.blockDecipher(self.seed, self.blockText, self.spinBox.value())
        self.decipheredText.clear()
        self.decipheredText.insertPlainText(decipheredResult)
        # self.score()

    def score(self):
        difference = funcs.intervalBetween(self.nonCipherInput, self.decipheredText.toPlainText())
        performance = 100 * (len(self.nonCipherInput) - difference) / len(self.decipheredText.toPlainText())
        self.performanceScore.setText("%" + performance.__str__())

    def loadFromFile(self):
        name = QFileDialog.getOpenFileName(None, "Load Text", "", "Txt Files (*.txt)")
        if name[0]:
            str = open(name[0], 'r', encoding="utf-8").read()
            self.analysisText.clear()
            self.analysisText.insertPlainText(str)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Kriptolanacak Metin"))
        self.label_3.setText(_translate("MainWindow", "Sezar Anahtar"))
        self.cipherButton.setText(_translate("MainWindow", "Sezar Kriptola"))
        self.label_4.setText(_translate("MainWindow", "Blok Boyutu (bit)"))
        self.blockCipher.setText(_translate("MainWindow", "Blok Kriptola"))
        self.analyzeCipherButton.setText(_translate("MainWindow", "Analiz Et"))
        self.label.setText(_translate("MainWindow", "Analiz Metni"))
        self.pushButton_2.setText(_translate("MainWindow", "Analiz Et"))
        self.fromTxtButton.setText(_translate("MainWindow", "txt\'den Yükle"))
        self.decipherButton.setText(_translate("MainWindow", "SEZAR ÇÖZ"))
        self.blockDecipherButton.setText(_translate("MainWindow", "BLOK ÇÖZ"))
        self.performanceScore.setPlaceholderText(_translate("MainWindow", "Performans Skoru"))

