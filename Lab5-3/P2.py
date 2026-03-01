""" 
Darin Khamsawat
683040489-2
P2
"""
import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox,
    QSpinBox, QMessageBox, QGroupBox
)
from PySide6.QtCharts import (
    QChart, QChartView, QBarSeries,
    QBarSet, QBarCategoryAxis, QValueAxis
)
from PySide6.QtCore import Qt


class SalesChartApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monthly Sales Chart")
        self.resize(1100, 650)

        self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        self.categories = ["Electronics", "Clothing", "Food", "Others"]

        self.sales_data = {
            category: [0] * 12 for category in self.categories
        }

        self.init_ui()

  
    def init_ui(self):
        main_layout = QHBoxLayout(self)

       
        left_panel = QVBoxLayout()

        import_group = QGroupBox("Import Data")
        import_layout = QVBoxLayout()

        self.filename_input = QLineEdit()
        self.filename_input.setPlaceholderText("e.g. Lab5-3/sales_data.txt")

        import_layout.addWidget(QLabel("Filename:"))
        import_layout.addWidget(self.filename_input)

        self.import_btn = QPushButton("Import Data")
        self.import_btn.setObjectName("importBtn")
        self.import_btn.clicked.connect(self.import_data)
        import_layout.addWidget(self.import_btn)

        import_group.setLayout(import_layout)

        add_group = QGroupBox("Add Sales Data")
        add_layout = QVBoxLayout()

        self.month_combo = QComboBox()
        self.month_combo.addItems(self.months)

        self.sales_input = QSpinBox()
        self.sales_input.setRange(0, 1000000)

        self.category_combo = QComboBox()
        self.category_combo.addItems(self.categories)

        add_layout.addWidget(QLabel("Month:"))
        add_layout.addWidget(self.month_combo)

        add_layout.addWidget(QLabel("Sales Amount:"))
        add_layout.addWidget(self.sales_input)

        add_layout.addWidget(QLabel("Product Category:"))
        add_layout.addWidget(self.category_combo)

        self.add_btn = QPushButton("Add Data")
        self.add_btn.setObjectName("addBtn")
        self.add_btn.clicked.connect(self.add_data)

        self.clear_btn = QPushButton("Clear Chart")
        self.clear_btn.setObjectName("clearBtn")
        self.clear_btn.clicked.connect(self.clear_chart)

        add_layout.addWidget(self.add_btn)
        add_layout.addWidget(self.clear_btn)

        add_group.setLayout(add_layout)

        left_panel.addWidget(import_group)
        left_panel.addWidget(add_group)
        left_panel.addStretch()

      
        self.chart = QChart()
        self.chart.setTitle("Monthly Sales by Product Category")

        self.chart_view = QChartView(self.chart)

        main_layout.addLayout(left_panel, 1)
        main_layout.addWidget(self.chart_view, 3)

        self.apply_styles()
        self.update_chart()

    
    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f8;
                font-size: 13px;
            }

            QGroupBox {
                font-weight: bold ;
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                margin-top: 10px;
                padding: 10px;
                background-color: white;
            }

            QLineEdit, QComboBox, QSpinBox {
                padding: 6px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            QPushButton {
                padding: 8px;
                border-radius: 6px;
                font-weight: bold;
                color: white;
            }

            QPushButton#importBtn {
                background-color: #3498db;
            }

            QPushButton#addBtn {
                background-color: #2ecc71;
            }

            QPushButton#clearBtn {
                background-color: #e74c3c;
            }

            QPushButton:hover {
                opacity: 0.85;
            }
        """)

   
    def import_data(self):
        filename = self.filename_input.text().strip()

        if not os.path.exists(filename):
            QMessageBox.warning(self, "Error", "File does not exist!")
            return

        self.clear_chart()

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue

                month, category, sales = parts

                if month in self.months and category in self.categories:
                    index = self.months.index(month)
                    self.sales_data[category][index] += int(sales)

        self.update_chart()

   
    def add_data(self):
        month = self.month_combo.currentText()
        sales = self.sales_input.value()
        category = self.category_combo.currentText()

        index = self.months.index(month)
        self.sales_data[category][index] += sales

        self.update_chart()

   
    def clear_chart(self):
        self.sales_data = {
            category: [0] * 12 for category in self.categories
        }
        self.update_chart()

  
    def update_chart(self):
        self.chart.removeAllSeries()

  
        for axis in self.chart.axes():
            self.chart.removeAxis(axis)

        series = QBarSeries()

        colors = {
            "Electronics": Qt.blue,
            "Clothing": Qt.red,
            "Food": Qt.green,
            "Others": Qt.magenta
        }

        max_value = 0

        for category in self.categories:
            bar_set = QBarSet(category)
            values = self.sales_data[category]
            bar_set.append(values)
            bar_set.setColor(colors[category])
            series.append(bar_set)

            if values:
                max_value = max(max_value, max(values))

        self.chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(self.months)

        axis_y = QValueAxis()
        axis_y.setTitleText("Sales Amount")
        axis_y.setRange(0, max_value + 5000)

        self.chart.addAxis(axis_x, Qt.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignLeft)

        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SalesChartApp()
    window.show()
    sys.exit(app.exec())