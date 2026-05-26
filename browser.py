from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import sys

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyBrowser by Turkey")
        self.resize(1024, 768)

        self.webview = QWebEngineView()
        self.setCentralWidget(self.webview)

        nav = QToolBar("Navigation")
        self.addToolBar(nav)

        back_btn = QAction("BACK", self)
        back_btn.triggered.connect(self.webview.back)
        nav.addAction(back_btn)

        forward_btn = QAction("FORW", self)
        forward_btn.triggered.connect(self.webview.forward)
        nav.addAction(forward_btn)

        reload_btn = QAction("REL", self)
        reload_btn.triggered.connect(self.webview.reload)
        nav.addAction(reload_btn)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        nav.addWidget(self.urlbar)

        self.webview.urlChanged.connect(self.update_urlbar)
        self.webview.setUrl(QUrl("https://turkey112.online/"))

    def navigate_to_url(self):
        text = self.urlbar.text().strip()
        if not text:
            return
        if "://" not in text:
            text = "http://" + text
        self.webview.setUrl(QUrl(text))

    def update_urlbar(self, qurl):
        self.urlbar.setText(qurl.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Browser()
    win.show()
    sys.exit(app.exec())
