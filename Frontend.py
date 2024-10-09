import os
import sys
import psutil
import subprocess
import re
import random
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QColorDialog
from PySide6.QtCore import Slot, Qt
import platform
import logging
import threading
import time
import sphinx

class ColorComparisonApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Color Comparison')

        self.color1_label = QtWidgets.QLabel('Choose a color for comparison 1', self)
        self.color1_label.setGeometry(20, 20, 200, 30)

        self.color1_button = QtWidgets.QPushButton('Choose...', self)
        self.color1_button.setGeometry(230, 20, 100, 30)
        self.color1_button.clicked.connect(self.choose_color1)

        self.color2_label = QtWidgets.QLabel('Choose a color for comparison 2', self)
        self.color2_label.setGeometry(20, 60, 200, 30)

        self.color2_button = QtWidgets.QPushButton('Choose...', self)
        self.color2_button.setGeometry(230, 60, 100, 30)
        self.color2_button.clicked.connect(self.choose_color2)

        self.similarity_label = QtWidgets.QLabel('Similarity: 0%', self)
        self.similarity_label.setGeometry(20, 100, 200, 30)

    def choose_color1(self):
        color1 = QColorDialog.getColor(self)
        if color1.isValid():
            self.color1_label.setStyleSheet(f'background-color: rgb({color1.red()}, {color1.green()}, {color1.blue()});')

    def choose_color2(self):
        color2 = QColorDialog.getColor(self)
        if color2.isValid():
            self.color2_label.setStyleSheet(f'background-color: rgb({color2.red()}, {color2.green()}, {color2.blue()});')

    def calculate_similarity(self, color1, color2):
        r1, g1, b1 = color1.red() / 255, color1.green() / 255, color1.blue() / 255
        r2, g2, b2 = color2.red() / 255, color2.green() / 255, color2.blue() / 255

        similarity = (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2
        similarity = round(100 - (similarity ** 0.5) * 100, 2)

        return similarity

    def update_similarity_label(self):
        color1 = self.color1_label.styleSheet().split('rgb(')[1].split(',')[0].split(')')[0]
        color2 = self.color2_label.styleSheet().split('rgb(')[1].split(',')[0].split(')')[0]

        similarity = self.calculate_similarity(QtGui.QColor(color1), QtGui.QColor(color2))
        self.similarity_label.setText(f'Similarity: {similarity}%')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorComparisonApp()
    window.show()
    sys.exit(app.exec_())