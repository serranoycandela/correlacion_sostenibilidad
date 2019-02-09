# -*- coding: utf-8 -*-

import PyQt5
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QHBoxLayout, QDockWidget, QWidget
import sys
#sys.path.insert(0,'/Applications/QGIS3.app/Contents/Frameworks/')
sys.path.insert(0,'/Applications/QGIS3.app/Contents/Resources/python/')
sys.path.insert(0,'/Applications/QGIS3.app/Contents/Resources/python/plugins')

from osgeo import gdal
from qgis.core import *
from qgis.gui import QgsMapCanvas

layerInput = QgsVectorLayer('path to shape file1', "file 1", "ogr")
layerInputShape = QgsVectorLayer('path to shape file2', "file 2", "ogr")


# canvas settings
canvas = QgsMapCanvas()
canvas.setCanvasColor(Qt.white)
canvas.enableAntiAliasing(True)


#defining OSM
xml = """<GDAL_WMS>
<Service name="TMS">
<ServerUrl>http://tile.openstreetmap.org/${z}/${x}/${y}.png</
ServerUrl>
</Service>
<DataWindow>
<TileLevel>18</TileLevel>
<TileCountX>1</TileCountX>
<TileCountY>1</TileCountY>
<YOrigin>top</YOrigin>
</DataWindow>
<Projection>EPSG:4326</Projection>
<BlockSizeX>256</BlockSizeX>
<BlockSizeY>256</BlockSizeY>
<BandsCount>3</BandsCount>
<Cache />
</GDAL_WMS>"""
vfn = "/vsimem/osm.xml"
gdal.FileFromMemBuffer(vfn, xml)
rasterLyr = QgsRasterLayer(vfn, "OSM")

# puting both vector layers on canvas
extent = QgsRectangle()
layers = []
QgsProject.instance().addMapLayer(layerInput)
extent.combineExtentWith(layerInput.extent())
layers.append(layerInput)
QgsProject.instance().addMapLayer(layerInputShape)
extent.combineExtentWith(layerInputShape.extent())
layers.append(layerInputShape)


#puting osm on canvas
QgsProject.instance().addMapLayer(rasterLyr)
extent.combineExtentWith(rasterLyr.extent())
layers.append(rasterLyr)

extent.scale(1.1)
canvas.setExtent(extent)
canvas.setLayers(layers)

# for legend
root = QgsProject.instance().layerTreeRoot()
bridge = QgsLayerTreeMapCanvasBridge(root, canvas)
model = QgsLayerTreeModel(root)
model.setFlag(QgsLayerTreeModel.AllowNodeReorder)
model.setFlag(QgsLayerTreeModel.AllowNodeRename)
model.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility)
model.setFlag(QgsLayerTreeModel.ShowLegend)
view = QgsLayerTreeView()
view.setModel(model)
view.show()

# embed the view and canvas into dock widget
layout = QHBoxLayout()
layout.addWidget(view)
layout.addWidget(canvas)
docked = QDockWidget()
docked.setContentsMargins(9, 9, 9, 9)
dockedWidget = QWidget()
docked.setWidget(dockedWidget)
docked.setWindowTitle('title')
dockedWidget.setLayout(layout)
docked.show()


# canvas properties
QgsProject.instance().addMapLayer(layerInput)
canvas.setExtent(layerInput.extent())
canvas.setLayers([layerInput])

canvas.refresh()
canvas.show()
app.exec_()
