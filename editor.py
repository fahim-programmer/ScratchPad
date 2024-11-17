from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtPrintSupport import *

class CodeEditor(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWordWrapMode(QTextOption.WordWrap)
        self.defaultFontSize = 12
        self.theme = "light"
        self.textColor = "#000000"
        self.backgroundColor = "#ffffff"
        self.setStyleSheet(f"font: 75 {self.defaultFontSize}pt Consolas; color: {self.textColor}; background-color: {self.backgroundColor};")

    def increaseFont(self):
        self.defaultFontSize = self.defaultFontSize + 1
        self.setStyleSheet(f"font: 75 {self.defaultFontSize}pt Consolas; color: {self.textColor}; background-color: {self.backgroundColor};")

    def decreaseFont(self):
        self.defaultFontSize = self.defaultFontSize - 1
        self.setStyleSheet(f"font: 75 {self.defaultFontSize}pt Consolas; color: {self.textColor}; background-color: {self.backgroundColor};")
    
    def toggleDarkLight(self):
        if self.theme == "light":
            self.textColor = "#ffffff"
            self.backgroundColor = "#000000"
            self.setStyleSheet(f"font: 75 {self.defaultFontSize}pt Consolas; color: {self.textColor}; background-color: {self.backgroundColor};")
            self.theme = "dark"
            # make it dark
        else:
            # make it light
            self.textColor = "#000000"
            self.backgroundColor = "#ffffff"
            self.setStyleSheet(f"font: 75 {self.defaultFontSize}pt Consolas; color: {self.textColor}; background-color: {self.backgroundColor};")
            self.theme = "light"
			
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Tab:
            cursor = self.textCursor()
            cursor.insertText("    ")  # Insert 4 spaces
        elif event.key() == Qt.Key_F9:
            self.increaseFont()
        elif event.key() == Qt.Key_F10:
            self.decreaseFont()
        else:
            super().keyPressEvent(event)

    def insertFromMimeData(self, source):
        # Insert plain text from the MIME data
        self.insertPlainText(source.text())