import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPainter, QIcon, QPixmap
from PyQt5.QtCore import QFile, QUrl, QRect, QSize
from PyQt5.QtCore import Qt
from testintro_gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.n = 0
        self.changePix()
        self.ui.introButton.clicked.connect(self.changePix)
        self.ui.inicioButton.clicked.connect(self.inicio)
    def inicio(self):
        self.n = 0
        self.ui.introButton.show()
        self.changePix()

    def changePix(self):
        icon = QIcon()
        self.n += 1
        if self.n < 4:
            elpng = "pw" + str(self.n) + ".png"
            icon.addPixmap(QPixmap(elpng), QIcon.Normal, QIcon.Off)

            self.ui.introButton.setIcon(icon)
            self.ui.introButton.setIconSize(QSize(1600,1000))
        else:
            self.ui.introButton.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
