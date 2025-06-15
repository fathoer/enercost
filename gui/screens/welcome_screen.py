import os
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class WelcomeScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent  # MainWindow

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # ENERCOST Logo
        logo_path = os.path.join("gui", "resources", "logogreen.png")
        logo_label = QLabel()
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(logo_path)
        pixmap = pixmap.scaledToWidth(280, Qt.TransformationMode.SmoothTransformation)
        logo_label.setPixmap(pixmap)

        # Welcome text
        welcome_label = QLabel("Welcome to ENERCOST 2.0")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        welcome_label.setStyleSheet("color: #165d32;")

        # Buttons
        create_btn = QPushButton("Create New Project")
        create_btn.setFixedHeight(36)
        create_btn.clicked.connect(self.open_project_info)

        load_btn = QPushButton("Load a Project")
        load_btn.setFixedHeight(36)
        # TODO: Hook up project loading later

        # Spacer between logo/text and buttons
        layout.addWidget(logo_label)
        layout.addWidget(welcome_label)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addWidget(create_btn)
        layout.addWidget(load_btn)

        # Spacer below buttons
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Footer credit
        credit = QLabel(
            "In memory of my cost estimator mentor\n"
            "Mr. James Thomas Henry Arthur\n"
            "RIP March 2022"
        )
        credit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        credit.setStyleSheet("color: gray; font-size: 10px;")

        layout.addWidget(credit)

        self.setLayout(layout)

    def open_project_info(self):
        if self.parent_window:
            self.parent_window.open_project_info()
