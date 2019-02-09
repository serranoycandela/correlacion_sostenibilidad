import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QFile

import sys
sys.path.insert(0,'/Applications/QGIS3.app/Contents/Frameworks/')
sys.path.insert(0,'/Applications/QGIS3.app/Contents/Resources/python/')
sys.path.insert(0,'/Applications/QGIS3.app/Contents/Resources/python/plugins')

#from osgeo import gdal
from qgis.core import *

from gui_qgiscanvas import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
