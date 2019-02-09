import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QVBoxLayout
from PyQt5.QtCore import QFile
from gui import Ui_MainWindow
#/Applications/QGIS3.app/Contents/MacOS/bin/pyuic4 gui.ui -o gui.py
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from value_functions import discrete_factor as f
from model import CriteriaVector
import numpy as np
import pandas as pd

from matrices import matrix_list

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        layout = QVBoxLayout(self.ui.frame)
        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas)
        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.plot(range(21),range(21))

        self.v = CriteriaVector(list(np.random.rand(1,21)[0]),
                           matrix_list)

        for id in range(1, 22):

            slider = getattr(self.ui, 'verticalSlider_%d' % id)
            slider.setMinimum(0)
            slider.setMaximum(10)
            slider.setTickInterval(1)
            slider.setSingleStep(1)
            slider.setValue(5)


            slider.sliderReleased.connect(
                lambda id=str(id): self.update(id))
        self.update_sliders()
        # self.ui.verticalSlider_1.sliderReleased.connect(self.update)
        #v.update(0, delta=1)
    def update_sliders(self):
        for id in range(1,22):
            slider = getattr(self.ui, 'verticalSlider_%d' % id)
            slider.setValue(self.v.variables[id-1]*10)



    def update(self, id):

        slider = getattr(self.ui, 'verticalSlider_%s' % id)
        id = int(id)-1
        old_value = 10*self.v.variables[id]
        self.v.update(id, delta=(slider.value()-old_value)/10 )
        self.update_sliders()
        print(old_value, str(slider.value()))

        #event.quieneres()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
