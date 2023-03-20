from output import Ui_MainWindow
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication(sys.argv)
MainWindow = QMainWindow()
window = Ui_MainWindow()
window.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())