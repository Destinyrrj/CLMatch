import os
import sys
import psutil
import subprocess
import re
import random
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Slot
import platform
import logging
import threading
import time
import sphinx

