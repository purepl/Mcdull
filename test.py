#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = ''
__author__ = 'Mcdull'
__mtime__ = '2015/12/16'

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('PyQt')
widget.show()
sys.exit(app.exec_())
