import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPainter, QIcon, QPixmap
from PyQt5.QtCore import QFile, QUrl, QRect, QSize, QTextStream
from PyQt5.QtCore import Qt
#binaries=[
     # ('/Library/Frameworks/Python.framework/Versions/3.6/lib/libtk8.6.dylib', 'tk'),
     # ('/Library/Frameworks/Python.framework/Versions/3.6/lib/libtcl8.6.dylib', 'tcl')],


# - Desplegar un diálogo o ventana emergente que de un poco más de información de a qué se
#   refiere el componente (sólo si es fácil de programar)


import qdarkstyle

from gui import Ui_MainWindow
#/Applications/QGIS3.app/Contents/MacOS/bin/pyuic4 gui.ui -o gui.py
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.colors import LinearSegmentedColormap

from value_functions import discrete_factor as f
from model import CriteriaVector
import numpy as np
import math

import pandas as pd
from pandas.plotting import parallel_coordinates
import glyph_writer as gw
from matrices import matrix_list3, subcats3, abrevia3, tooltip
from PyQt5.QtWebEngineWidgets import QWebEngineView
from os.path import dirname, realpath, join, abspath
#import matplotlib.pyplot as plt
from pandas import ExcelFile


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.inicioButton.setEnabled(False)
        self.ui.guardarButton.setEnabled(False)
        self.ui.back.setEnabled(False)
        self.ui.loadExcel.clicked.connect(self.load_excel)
        self.ui.guardarButton.clicked.connect(self.guardar)
        self.ui.back.clicked.connect(self.de_reversa)

        layout = QVBoxLayout(self.ui.frame)
        static_canvas = FigureCanvas(Figure(figsize=(8, 3)))
        ecologica_pix = QPixmap('ecologica.png')
        self.ui.ecolo.setPixmap(ecologica_pix)
        economica_pix = QPixmap('economica.png')
        self.ui.econo.setPixmap(economica_pix)
        social_pix = QPixmap('social.png')
        self.ui.social.setPixmap(social_pix)
        gober_pix = QPixmap('gobernanza.png')
        self.ui.gober.setPixmap(gober_pix)
        layout.addWidget(static_canvas)
        static_canvas.figure.subplots_adjust(left=0.07, right=0.99, top=0.9, bottom=0.1)
        self._static_ax = static_canvas.figure.subplots()
        colors = [(1, 0, 0), (0.8, 0.8, 0), (0, 0.5, 0)]  # R -> Y -> G
        self.palette = LinearSegmentedColormap.from_list("semaforo", colors, N=255)
        self.v = CriteriaVector([n * 100 for n in list(np.random.rand(1,21)[0])],
                           matrix_list3)
        self.n = 0
        self.changePix()
        self.ui.introButton.clicked.connect(self.changePix)
        self.ui.inicioButton.clicked.connect(self.inicio)
        self.ui.creditosButton.clicked.connect(self.creditos)
        # setup ranges for sliders, connect them
        for id in range(0, 21):
            slider = getattr(self.ui, 'slider_%d' % id)
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setTickInterval(5)
            slider.setSingleStep(1)
            slider.setValue(50)
            slider.sliderReleased.connect(
                lambda id=str(id): self.update(id))
            label = getattr(self.ui, 'label_%d' % id)
            titulo = subcats3[id].split(". ")
            label.setText("<html><head/><body><font size='3'><p><b>"+titulo[0]+". </b>"+titulo[1]+"</p></font></body></html>")
            label.setToolTip(tooltip[titulo[0]])
            lcdNumber = getattr(self.ui, 'lcdNumber_%d' % id)
            lcdNumber.setToolTip(tooltip[titulo[0]])


        try:
            self.dirPath = dirname(abspath(__file__))
        except NameError:  # We are the main py2exe script, not a module
            self.dirPath = dirname(abspath(sys.argv[0]))


        self.view = QWebEngineView(self.ui.glyph_view)
        self.view.setGeometry(0,0,520,520)
        self.update_glyph()
        self.view.show()

        self.update_pc(self.v.variables)
        self.update_sliders()
        self.history = []
        self.history.append(self.v.variables[:])



    def de_reversa(self):
        self.history = self.history[:-1]
        old_values = self.v.variables[:]
        self.v.variables = self.history[-1][:]
        self.update_sliders()

        self.update_glyph()
        self.update_pc(old_values)
        if len(self.history)==1:
            self.ui.back.setEnabled(False)

    def guardar(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Guardar","","Excel Files (*.xlsx)", options=options)
        if fileName:
            if not fileName.endswith(".xlsx"):
                fileName = fileName + ".xlsx"

            df = pd.DataFrame({'Clave'     : abrevia3,
                               'Criterio'  : subcats3,
                               'Valor'     : self.v.variables
                                })
            new = df["Criterio"].str.split(". ", n = 1, expand = True)

            df["Criterio"]= new[1]
            df.Valor = df.Valor.round()
            df.to_excel(fileName, sheet_name='Sheet1', index=False)

    def load_excel(self):
        esteFileChooser = QFileDialog()
        #esteFileChooser.setFileMode(QFileDialog.Directory)
        if esteFileChooser.exec_():
            print(esteFileChooser.selectedFiles()[0])
            df = pd.read_excel(esteFileChooser.selectedFiles()[0], sheet_name=0)
            self.v.variables = list(df['Valor'])
            self.history = []
            self.history.append(self.v.variables[:])
            self.ui.back.setEnabled(False)
            self.update_glyph()
            self.update_pc(self.v.variables)
            self.update_sliders()
            self.ui.introButton.hide()
            self.ui.guardarButton.setEnabled(True)
            self.ui.inicioButton.setEnabled(True)


    def creditos(self):
        self.ui.introButton.show()
        icon = QIcon()
        elpng = "pw4.png"
        icon.addPixmap(QPixmap(elpng), QIcon.Normal, QIcon.Off)
        #self.ui.loadExcel.setEnabled(False)
        self.ui.guardarButton.setEnabled(False)
        self.ui.inicioButton.setEnabled(True)
        self.ui.introButton.setIcon(icon)
        self.ui.introButton.setIconSize(QSize(1368,779))

    def inicio(self):
        self.n = 0
        self.ui.introButton.show()
        self.ui.inicioButton.setEnabled(False)
        self.ui.guardarButton.setEnabled(False)
        self.changePix()

    def changePix(self):
        icon = QIcon()
        self.n += 1
        if self.n > 1:
            self.ui.inicioButton.setEnabled(True)
        if self.n < 3:
            elpng = "pw" + str(self.n) + ".png"
            icon.addPixmap(QPixmap(elpng), QIcon.Normal, QIcon.Off)

            self.ui.introButton.setIcon(icon)
            self.ui.introButton.setIconSize(QSize(1368,779))
        else:
            self.ui.introButton.hide()
            self.ui.guardarButton.setEnabled(True)

    def update_sliders(self):
        for id in range(0,21):
            slider = getattr(self.ui, 'slider_%d' % id)
            slider.setValue(self.v.variables[id])
            lcd = getattr(self.ui, 'lcdNumber_%d' % id)
            lcd.display(int(self.v.variables[id]))
    def logistic(self, x):
        x_0_1 = x/100.0
        result_0_1 =  1 / (1.0 + math.exp(-10 * (x - 0.5)))
        return result_0_1


    def index2rgb(self, palette, index):
        index255 = int(255.0 * self.logistic(index))
        color_0_1 = palette(index255)
        list_rgb = [color_0_1[0],color_0_1[1],color_0_1[2]]
        return list_rgb

    def update_pc(self,old_values):
        # df = pd.DataFrame(self.v.variables,
        #                   columns=["values"])
        # parallel_coordinates(df, '0', ax=self._static_ax)
        print(old_values)
        print(self.v.variables)
        self._static_ax.clear()
        xcoords = [9.5, 12.5, 15.5]
        for xc in xcoords:
            self._static_ax.axvline(x=xc, color="lightgray")
        line_color = self.index2rgb(self.palette,self.total)
        self._static_ax.plot( range(21), old_values, "gainsboro")
        self._static_ax.plot( range(21), self.v.variables, color=line_color)
        self._static_ax.text(3, 105, "Ambiental", fontsize=8)
        self._static_ax.text(9.5, 105, "Económica", fontsize=8)
        self._static_ax.text(13, 105, "Social", fontsize=8)
        self._static_ax.text(16.5, 105, "Gobernanza", fontsize=8)
        self._static_ax.set_ylim(bottom=0, top=102)
        self._static_ax.set_xticklabels([])
        self._static_ax.xaxis.set_ticks(np.arange(0, 21, 1.0))

        self._static_ax.figure.canvas.draw()

    def vector2dict(self):
        # cats = {"Ecológica": [0, 1, 3, 4, 5, 6, 7, 8, 9, 18],
        #         "Económica": [2, 11, 12],
        #         "Socio-cultural": [14, 17, 20],
        #         "Gobernanza": [10, 13, 16, 17, 19]}

        cats = {"Ambiental": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                "Económica": [10, 11, 12],
                "Socio-cultural": [13, 14, 15],
                "Gobernanza": [16, 17, 18, 19, 20]}


        means = {k:np.mean([self.v.variables[n]/100.0 for n in cats[k]]) for k in cats}
        self.total = np.mean(list(means.values()))


        data = {"total": {"name": "Sustentabilidad Urbana",
                          "value": self.total},
                "categories": [{"name": k,
                                "value": means[k],
                                "subcategories":
                                [{"name": abrevia3[subcat], "value": self.v.variables[subcat]/100.0 }
                                 for subcat in cats[k]]}
                for k in cats]}

        print(data)

        return data




    def update_glyph(self):
        data1 = self.vector2dict()
        #print(gw.makeGlyph(800, data1, labels=True, toEnsableLabelsLater=True))
        #svg_bytes = bytearray(gw.makeGlyph(520, data1, labels=True, toEnsableLabelsLater=True), encoding='utf-8')

        self.view.setHtml(gw.makeBarGlyph(500, data1, labels=True, toEnsableLabelsLater=True,palette=self.palette))


        #self.svgWidget.renderer().load(svg_bytes)



    def update(self, id):

        slider = getattr(self.ui, 'slider_%s' % id)
        id = int(id)
        old_values = self.v.variables[:]
        old_value = self.v.variables[id]
        self.v.update(id, delta=(slider.value()-old_value) )
        self.update_sliders()

        self.update_glyph()
        self.update_pc(old_values)
        self.history.append(self.v.variables[:])
        if len(self.history)==2:
            self.ui.back.setEnabled(True)
        print(old_value, str(slider.value()))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window.show()
    app.setWindowIcon(QIcon(join(window.dirPath,'logo.ico')))
    window.setWindowIcon(QIcon(join(window.dirPath,'logo.ico')))
    sys.exit(app.exec_())
