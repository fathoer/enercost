# logic.py

from PyQt6.QtCore import QObject


class ProjectInfoLogic(QObject):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.connect_signals()

    def connect_signals(self):
        # Connect length/width changes to auto area update
        self.ui.area_section.length_input.textChanged.connect(self.update_area)
        self.ui.area_section.width_input.textChanged.connect(self.update_area)

        # Connect currency change to show/hide exchange rate
        self.ui.settings_section.currency_input.currentTextChanged.connect(self.update_exchange_visibility)

        # Connect unit system change to update placeholders
        self.ui.settings_section.unit_system_input.currentTextChanged.connect(self.update_placeholders)

    def update_area(self):
        try:
            length = float(self.ui.area_section.length_input.text())
            width = float(self.ui.area_section.width_input.text())
            area_m2 = length * width
            area_ha = area_m2 / 10_000
            self.ui.area_section.area_display.setText(f"{area_m2:,.0f} m² ({area_ha:.2f} ha)")
        except ValueError:
            self.ui.area_section.area_display.setText("0 m² (0.0 ha)")

    def update_exchange_visibility(self):
        selected = self.ui.settings_section.currency_input.currentText()
        if selected.startswith("USD"):
            self.ui.settings_section.exchange_rate_row.setVisible(False)
        else:
            self.ui.settings_section.exchange_rate_row.setVisible(True)

    def update_placeholders(self):
        unit = self.ui.settings_section.unit_system_input.currentText()
        if unit == "Metric":
            self.ui.area_section.length_input.setPlaceholderText("e.g., 2000")
            self.ui.area_section.width_input.setPlaceholderText("e.g., 1000")
        else:  # Imperial
            self.ui.area_section.length_input.setPlaceholderText("e.g., 6561")
            self.ui.area_section.width_input.setPlaceholderText("e.g., 3280")
