from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create a search bar and search button
        self.search_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_button = QPushButton('Search')
        self.search_layout.addWidget(self.search_bar)
        self.search_layout.addWidget(self.search_button)

        # Create a back button
        self.back_button = QPushButton('Back')

        # Add the search bar, search button, and back button to the layout
        self.layout.addLayout(self.search_layout)
        self.layout.addWidget(self.back_button)

        # Create a QWebEngineView widget and add it to the layout
        self.webview = QWebEngineView()
        self.layout.addWidget(self.webview)

        # Connect the search button's clicked signal to the search function
        self.search_button.clicked.connect(self.search)

        # Connect the back button's clicked signal to the webview's back slot
        self.back_button.clicked.connect(self.webview.back)

        # Load a web page
        self.webview.load(QUrl('https://www.example.com'))

    def search(self):
        # Get the search query from the search bar
        query = self.search_bar.text()

        # Perform a search using the search query
        self.webview.load(QUrl(f'https://www.google.com/search?q={query}'))


def main():
    app = QApplication([])
    window = Browser()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
