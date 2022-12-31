import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the size of the main window
        self.resize(800, 600)

        # Create a QWebEngineView widget
        self.view = QWebEngineView(self)

        # Create a QLineEdit widget for the search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Enter a URL or search query")

        # Create a QWidget to hold the search bar and the web view,
        # and set it as the central widget of the main window
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.search_bar)
        layout.addWidget(self.view)
        self.setCentralWidget(central_widget)

        # Connect the search bar's returnPressed signal to a slot
        self.search_bar.returnPressed.connect(
            self.on_search_bar_return_pressed)

        # Connect the view's loadFinished signal to a slot
        self.view.loadFinished.connect(self.on_load_finished)

        # Set the default URL to open
        self.view.setUrl(QUrl("http://www.google.com"))

    def on_search_bar_return_pressed(self):
        # Update the QWebEngineView's URL when the user hits the Enter key in the search bar
        url = self.search_bar.text()
        self.view.setUrl(QUrl(url))

    def on_load_finished(self):
        # When the page is finished loading, update the search bar with the current URL
        # and set the title of the main window to the title of the web page
        self.search_bar.setText(self.view.url().toString())
        self.setWindowTitle(self.view.title())


app = QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())
