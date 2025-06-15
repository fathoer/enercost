# settings_section.py

import os
import pycountry
from PyQt6.QtWidgets import (
    QWidget, QGroupBox, QGridLayout, QLabel, QComboBox,
    QDateEdit, QLineEdit, QHBoxLayout, QVBoxLayout
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QDate


class SettingsSection(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        from PyQt6.QtGui import QIcon
        import os
        import pycountry

        self.country_input = QComboBox()
        self.currency_input = QComboBox()
        self.valuation_date = QDateEdit()
        self.valuation_date.setCalendarPopup(True)
        self.valuation_date.setDate(QDate.currentDate())

        self.unit_system_input = QComboBox()
        self.unit_system_input.addItems(["Metric", "Imperial"])

        # Exchange Rate Row
        self.exchange_rate_input = QLineEdit()
        self.exchange_rate_label = QLabel("1 USD to")
        self.exchange_rate_row = QWidget()
        exchange_layout = QHBoxLayout()
        exchange_layout.setContentsMargins(0, 0, 0, 0)
        exchange_layout.setSpacing(6)
        exchange_layout.addWidget(self.exchange_rate_label)
        exchange_layout.addWidget(self.exchange_rate_input)
        self.exchange_rate_row.setLayout(exchange_layout)
        self.exchange_rate_row.setVisible(False)

        # ⬛ Limit width for all input widgets
        max_width = 400
        for widget in [
            self.country_input, self.currency_input,
            self.valuation_date, self.unit_system_input, self.exchange_rate_input
        ]:
            widget.setMaximumWidth(max_width)

        # Country list with optional flags
        self.country_input.clear()
        flags_path = "gui/resources/flags"
        for country in sorted(pycountry.countries, key=lambda c: c.name):
            code = country.alpha_2.lower()
            name = country.name
            icon_path = os.path.join(flags_path, f"{code}.svg")
            if os.path.exists(icon_path):
                self.country_input.addItem(QIcon(icon_path), name)
            else:
                self.country_input.addItem(name)

        # Currency list with symbols
        currency_data = {
            "USD": "United States Dollar ($)",
            "EUR": "Euro (€)",
            "IDR": "Indonesian Rupiah (Rp)",
            "JPY": "Japanese Yen (¥)",
            "GBP": "British Pound (£)",
            "CNY": "Chinese Yuan (¥)",
            "INR": "Indian Rupee (₹)",
            "AUD": "Australian Dollar (A$)",
            "CAD": "Canadian Dollar (C$)",
            "SGD": "Singapore Dollar (S$)"
        }
        for code, label in currency_data.items():
            self.currency_input.addItem(f"{code} - {label}")

        # Grid layout
        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 2)

        grid.addWidget(QLabel("Project Country:"), 0, 0)
        grid.addWidget(self.country_input, 0, 1)
        grid.addWidget(QLabel("Project Currency:"), 1, 0)
        grid.addWidget(self.currency_input, 1, 1)
        grid.addWidget(QLabel("Valuation Date:"), 2, 0)
        grid.addWidget(self.valuation_date, 2, 1)
        grid.addWidget(QLabel("System Unit:"), 3, 0)
        grid.addWidget(self.unit_system_input, 3, 1)
        grid.addWidget(self.exchange_rate_row, 4, 1)

        # Wrap in GroupBox and return
        from PyQt6.QtWidgets import QGroupBox, QVBoxLayout
        group = QGroupBox("⚙️ Project Settings")
        group.setLayout(grid)

        wrapper = QVBoxLayout(self)
        wrapper.addWidget(group)

