import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QWebEngineView widget and set it as the central widget
        # of the main window
        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

        # Connect the view's loadFinished signal to a slot
        self.view.loadFinished.connect(self.on_load_finished)

        # Set the default URL to open
        self.view.setUrl(QUrl("http://www.google.com"))

    def on_load_finished(self):
        # When the page is finished loading, set the title of the main window
        # to the title of the web page
        self.setWindowTitle(self.view.title())

app = QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())