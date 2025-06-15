# doc_section.py

from PyQt6.QtWidgets import (
    QWidget, QGroupBox, QGridLayout, QLabel, QLineEdit, QTextEdit, QVBoxLayout
)


class DocSection(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.prepared_by_input = QLineEdit()
        self.remarks_input = QTextEdit()
        self.remarks_input.setPlaceholderText("Any additional notes or remarks...")
        self.remarks_input.setFixedHeight(100)
        self.remarks_input.setStyleSheet("margin-bottom: 4px;")

        max_width = 400
        for widget in [self.prepared_by_input, self.remarks_input]:
            widget.setMaximumWidth(max_width)

        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 2)

        group = QGroupBox("📄 Documentation")
        group.setLayout(grid)

        wrapper = QVBoxLayout(self)
        wrapper.addWidget(group)
