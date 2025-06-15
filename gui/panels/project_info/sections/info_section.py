# info_section.py

from PyQt6.QtWidgets import QWidget, QGroupBox, QGridLayout, QLabel, QLineEdit, QTextEdit, QVBoxLayout


class InfoSection(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Inputs
        self.title_input = QLineEdit()
        self.owner_input = QLineEdit()
        self.client_input = QLineEdit()
        self.description_input = QTextEdit()

        # Stretch fix for bottom border
        self.description_input.setFixedHeight(100)
        self.description_input.setStyleSheet("margin-bottom: 4px;")
        self.description_input.setPlaceholderText("Enter a brief project description...")

        # Fix horizontal width for better balance
        max_width = 400
        for widget in [self.title_input, self.owner_input, self.client_input, self.description_input]:
            widget.setMaximumWidth(max_width)

        # Layout
        grid = QGridLayout()
        grid.setColumnStretch(0, 1)  # Label side
        grid.setColumnStretch(1, 2)  # Input side

        grid.addWidget(QLabel("Project Title:"), 0, 0)
        grid.addWidget(self.title_input, 0, 1)

        grid.addWidget(QLabel("Project Owner:"), 1, 0)
        grid.addWidget(self.owner_input, 1, 1)

        grid.addWidget(QLabel("Project Client:"), 2, 0)
        grid.addWidget(self.client_input, 2, 1)

        grid.addWidget(QLabel("Project Description:"), 3, 0)
        grid.addWidget(self.description_input, 3, 1)

        group = QGroupBox("📝 Project Information")
        group.setLayout(grid)

        wrapper = QVBoxLayout(self)
        wrapper.addWidget(group)
