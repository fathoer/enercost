from PyQt6.QtWidgets import QWidget
from .ui import ProjectInfoUI
from .logic import ProjectInfoLogic

class ProjectInfoPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ProjectInfoUI()
        self.logic = ProjectInfoLogic(self.ui)
        self.setLayout(self.ui.layout())