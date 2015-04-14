__author__ = 'Girish'

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from mdviewer import Ui_MainWindow
from markdown import markdownFromFile, markdown


class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Markdown reader")

        self.actionOpen.triggered.connect(self.getFile)

    def getFile(self):
        filename =QFileDialog.getOpenFileNameAndFilter(self,"Open md files","","Markdown (*.md)")
        if filename:
            self.file = filename
            with open(self.file[0]) as file:
                self.data=file.read()
            self.webView.setHtml(markdown(self.data))

    def md_to_html(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
