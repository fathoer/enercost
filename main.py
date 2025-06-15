import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtCore import QSize
from gui.screens.welcome_screen import WelcomeScreen
from gui.panels.project_info import ProjectInfoPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ENERCOST 2.0")
        self.setMinimumSize(960, 600)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.welcome_screen = WelcomeScreen(self)
        self.project_info_panel = ProjectInfoPanel()

        self.stack.addWidget(self.welcome_screen)       # Index 0
        self.stack.addWidget(self.project_info_panel)   # Index 1

        self.stack.setCurrentIndex(0)  # Show welcome screen first

    def open_project_info(self):
        self.stack.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # === Load QSS ===
    qss_file = os.path.join("gui", "style", "enercost.qss")
    with open(qss_file, "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
