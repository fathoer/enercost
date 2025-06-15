# ui.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame
)
from .sections.info_section import InfoSection  # 📝 Modular section
from .sections.settings_section import SettingsSection

class ProjectInfoUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("project_info_ui")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        from .sections.info_section import InfoSection
        from .sections.settings_section import SettingsSection
        from .sections.area_section import AreaSection
        from .sections.doc_section import DocSection
        from .sections.separator import horizontal_separator

        self.info_section = InfoSection()
        self.settings_section = SettingsSection()
        self.area_section = AreaSection()
        self.doc_section = DocSection()

        layout.addWidget(horizontal_separator())
        layout.addWidget(self.info_section)
        layout.addWidget(horizontal_separator())
        layout.addWidget(self.settings_section)
        layout.addWidget(horizontal_separator())
        layout.addWidget(self.area_section)
        layout.addWidget(horizontal_separator())
        layout.addWidget(self.doc_section)
        layout.addWidget(horizontal_separator())
        layout.addLayout(self.build_button_row())

    def add_separator(self):
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        return line

    def build_button_row(self):
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")
        hbox.addWidget(self.save_button)
        hbox.addWidget(self.cancel_button)
        return hbox
