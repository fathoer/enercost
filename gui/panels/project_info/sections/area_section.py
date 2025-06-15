# area_section.py

from PyQt6.QtWidgets import (
    QWidget, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout
)


class AreaSection(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.length_input = QLineEdit()
        self.length_input.setPlaceholderText("e.g., 2000")

        self.width_input = QLineEdit()
        self.width_input.setPlaceholderText("e.g., 1000")

        self.area_display = QLabel("0 m² (0.0 ha)")
        self.area_display.setStyleSheet("color: #165d32; font-weight: bold;")

        # 🔧 Width fix
        max_width = 400
        for widget in [self.length_input, self.width_input]:
            widget.setMaximumWidth(max_width)

        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 2)

        grid.addWidget(QLabel("Length:"), 0, 0)
        grid.addWidget(self.length_input, 0, 1)
        grid.addWidget(QLabel("Width:"), 1, 0)
        grid.addWidget(self.width_input, 1, 1)
        grid.addWidget(QLabel("Total Area:"), 2, 0)
        grid.addWidget(self.area_display, 2, 1)

        group = QGroupBox("📐 Project Area")
        group.setLayout(grid)

        wrapper = QVBoxLayout(self)
        wrapper.addWidget(group)
