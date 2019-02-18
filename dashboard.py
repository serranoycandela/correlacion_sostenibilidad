import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QFile, QUrl, QRect
from PyQt5.QtCore import Qt

from gui import Ui_MainWindow
#/Applications/QGIS3.app/Contents/MacOS/bin/pyuic4 gui.ui -o gui.py
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

import matplotlib

matplotlib.use('Agg')
from matplotlib.colors import LinearSegmentedColormap

from palettable.colorbrewer.sequential import YlGn_6
from palettable.colorbrewer.diverging import RdYlGn_11
from palettable.cmocean.sequential import Thermal_13
from value_functions import discrete_factor as f
from model import CriteriaVector
import numpy as np

import pandas as pd
from pandas.plotting import parallel_coordinates
import glyph_writer as gw
from matrices import matrix_list2, subcats2
from PyQt5.QtWebEngineWidgets import QWebEngineView
#import matplotlib.pyplot as plt


class MyLabel(QLabel):
    def __init__(self, text=None, parent=None):
        super(self.__class__, self).__init__()
        self.text = text
        self.parent = parent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.white)
        painter.translate(20, 100)
        painter.rotate(-90)
        if self.text:
            painter.drawText(0, 0, self.text)
        painter.end()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        layout = QVBoxLayout(self.ui.frame)
        static_canvas = FigureCanvas(Figure(figsize=(8, 3)))

        layout.addWidget(static_canvas)
        static_canvas.figure.subplots_adjust(left=0.07, right=0.99, top=0.9, bottom=0.1)
        self._static_ax = static_canvas.figure.subplots()
        colors = [(1, 0, 0), (0.8, 0.8, 0), (0, 0.5, 0)]  # R -> Y -> G
        self.palette = LinearSegmentedColormap.from_list("semaforo", colors, N=255)
        self.v = CriteriaVector([n * 100 for n in list(np.random.rand(1,21)[0])],
                           matrix_list2)

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
            label.setText(subcats2[id])

        self.update_pc(self.v.variables)
        self.update_sliders()

        self.view = QWebEngineView(self.ui.glyph_view)
        self.view.setGeometry(0,0,520,520)
        self.update_glyph()
        self.view.show()
        # self.economica = MyLabel(text="Económica",parent=self.ui.centralwidget)
        # self.economica.setGeometry(QRect(20,300,30,400))
        # self.economica.show()


    def update_sliders(self):
        for id in range(0,21):
            slider = getattr(self.ui, 'slider_%d' % id)
            slider.setValue(self.v.variables[id])

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
        self._static_ax.plot( range(21), old_values, "gainsboro")
        self._static_ax.plot( range(21), self.v.variables, "green")
        self._static_ax.text(3, 105, "Ecológica", fontsize=8)
        self._static_ax.text(9.5, 105, "Económica", fontsize=8)
        self._static_ax.text(13, 105, "Social", fontsize=8)
        self._static_ax.text(16.5, 105, "Gobernanza", fontsize=8)
        self._static_ax.set_ylim(bottom=0, top=100)
        self._static_ax.set_xticklabels([])
        self._static_ax.xaxis.set_ticks(np.arange(0, 21, 1.0))

        self._static_ax.figure.canvas.draw()

    def vector2dict(self):
        # cats = {"Ecológica": [0, 1, 3, 4, 5, 6, 7, 8, 9, 18],
        #         "Económica": [2, 11, 12],
        #         "Socio-cultural": [14, 17, 20],
        #         "Gobernanza": [10, 13, 16, 17, 19]}

        cats = {"Ecológica": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                "Económica": [10, 11, 12],
                "Socio-cultural": [13, 14, 15],
                "Gobernanza": [16, 17, 18, 19, 20]}


        means = {k:np.mean([self.v.variables[n]/100.0 for n in cats[k]]) for k in cats}
        total = np.mean(list(means.values()))


        data = {"total": {"name": "Sostenibilidad Urbana",
                          "value": total},
                "categories": [{"name": k,
                                "value": means[k],
                                "subcategories":
                                [{"name": subcats2[subcat], "value": self.v.variables[subcat]/100.0 }
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
        self.update_pc(old_values)
        self.update_glyph()
        print(old_value, str(slider.value()))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
