import os
import pycountry
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QComboBox, QGridLayout, QHBoxLayout
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize


class ProjectInfoPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()
        layout.setContentsMargins(40, 40, 40, 20)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(12)

        font_size = "10pt"

        # === 1. Project Title ===
        layout.addWidget(self._label("Project Title", font_size), 0, 0)
        self.title_input = QLineEdit()
        layout.addWidget(self.title_input, 0, 1, 1, 2)

        # === 2. Country (with flags) ===
        layout.addWidget(self._label("Country", font_size), 1, 0)
        self.country_input = QComboBox()
        self._load_country_flags()
        layout.addWidget(self.country_input, 1, 1, 1, 2)

        # === 3. Currency (full label) ===
        layout.addWidget(self._label("Currency", font_size), 2, 0)
        self.currency_input = QComboBox()
        self._load_currency_options()
        layout.addWidget(self.currency_input, 2, 1, 1, 2)

        # === 4. Area Length + Unit ===
        layout.addWidget(self._label("Area Length", font_size), 3, 0)
        self.length_input = QLineEdit()
        self.length_unit = QComboBox()
        self.length_unit.addItems(["m", "ft"])
        layout.addLayout(self._inline_field(self.length_input, self.length_unit), 3, 1, 1, 2)

        # === 5. Area Width + Unit ===
        layout.addWidget(self._label("Area Width", font_size), 4, 0)
        self.width_input = QLineEdit()
        self.width_unit = QComboBox()
        self.width_unit.addItems(["m", "ft"])
        layout.addLayout(self._inline_field(self.width_input, self.width_unit), 4, 1, 1, 2)

        # === 6. Calculated Area (read-only) ===
        layout.addWidget(self._label("Area (calculated)", font_size), 5, 0)
        self.area_display = QLineEdit()
        self.area_display.setReadOnly(True)
        self.area_display.setPlaceholderText("e.g., 2,500 m²")
        layout.addWidget(self.area_display, 5, 1, 1, 2)

        self.setLayout(layout)

    def _label(self, text, font_size):
        label = QLabel(text)
        label.setStyleSheet(f"font-size: {font_size}; color: #165d32;")
        return label

    def _inline_field(self, input_box, unit_box):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)
        layout.addWidget(input_box)
        layout.addWidget(unit_box)
        return layout

    def _load_country_flags(self):
        self.country_input.setIconSize(QSize(18, 12))
        flags_path = os.path.join("gui", "resources", "flags")
        countries = sorted(pycountry.countries, key=lambda c: c.name)

        for country in countries:
            code = country.alpha_2.lower()
            name = country.name
            flag_file = os.path.join(flags_path, f"{code}.svg")
            if os.path.exists(flag_file):
                icon = QIcon(flag_file)
                self.country_input.addItem(icon, name)
            else:
                self.country_input.addItem(name)

    def _load_currency_options(self):
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
