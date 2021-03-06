"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import os
from pathlib import Path

APP = ['dashboard.py']
DATA_FILES = []
#OPTIONS = {'includes': ["PyQt5", "matplotlib"]}
OPTIONS = {
    "py2app": {
         "bdist_base": os.path.join(str(Path(os.getcwd()).parent), 'build'),
         "dist_dir": os.path.join(str(Path(os.getcwd()).parent), 'dist'),
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options=OPTIONS,

    setup_requires=['py2app'],
)
