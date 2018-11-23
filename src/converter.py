# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 15:37:36 2018

@author: Prashant
"""
import sys
import time
from PyQt5 import QtWidgets
from PyQt5 import uic
import currency

class UserInterface(QtWidgets.QDialog):
    def __init__(self):
        super(UserInterface, self).__init__()
        uic.loadUi('frame.ui', self)
        self.cunvert.clicked.connect(self.convert_clicked)
        self.show()

    def convert_clicked(self):
    	frm = self.from_cur.text()
    	to = self.to_cur.text()
    	try:
    		self.value.setText(currency.convert(frm, to))
    	except AttributeError:
    		self.value.setText("Currency Not Found")
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    window.setWindowTitle('Currency Converter in Python');
    sys.exit(app.exec_())