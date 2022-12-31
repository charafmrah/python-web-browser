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

        # Create a back button and forward button
        self.back_button = QPushButton('Back')
        # Set the minimum width of the back button to a smaller value
        self.back_button.setMinimumWidth(30)
        self.forward_button = QPushButton('Forward')
        # Set the minimum width of the forward button to a smaller value
        self.forward_button.setMinimumWidth(30)

        # Add the back button and forward button to the search layout
        self.search_layout.addWidget(self.back_button)
        self.search_layout.addWidget(self.forward_button)

        # Add the search bar and search button to the search layout
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Enter a URL or search query")
        self.search_bar.returnPressed.connect(self.search)
        self.search_button = QPushButton('Search')
        self.search_layout.addWidget(self.search_bar)
        self.search_layout.addWidget(self.search_button)

        # Add the search layout to the main layout
        self.layout.addLayout(self.search_layout)

        # Create a QWebEngineView widget and add it to the layout
        self.webview = QWebEngineView()
        self.layout.addWidget(self.webview)

        # Connect the search button's clicked signal to the search function
        self.search_button.clicked.connect(self.search)

        # Connect the back button's clicked signal to the webview's back slot
        self.back_button.clicked.connect(self.webview.back)

        # Connect the forward button's clicked signal to the webview's forward slot
        self.forward_button.clicked.connect(self.webview.forward)

        # Load a web page
        self.webview.load(QUrl('https://www.charafmrah.com'))

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
