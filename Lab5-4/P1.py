""" 
Darin Khamsawat
683040489-2
P1
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout,
    QFileDialog, QMessageBox, QToolBar, QStyle,
    QSpinBox, QColorDialog
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QLocale
from PySide6.QtWidgets import QComboBox


class PersonalInfoCard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: Personal Info Card")
        self.resize(750, 500)

        self.card_color = "#4db1a5"  # default card color

        self.initUI()
        self.create_menu()
        self.create_toolbar()

        self.statusBar().showMessage("Ready")

    
    def initUI(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()

       
        form_layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("First name and Lastname")

        self.age_input = QSpinBox()
        self.age_input.setRange(1, 120)
        self.age_input.setValue(25)
        self.age_input.setLocale(QLocale(QLocale.Language.English, QLocale.Country.UnitedStates))

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("username@domain.name")

        # Position (ComboBox)
        self.role_combo = QComboBox()
        self.role_combo.addItems([
               "Student",
              "Staff",
               "Teacher",
               "Intern",
               "Other"
                     ])

        form_layout.addWidget(QLabel("Position:"))
        form_layout.addWidget(self.role_combo)

        form_layout.addWidget(QLabel("Full name:"))
        form_layout.addWidget(self.name_input)

        form_layout.addWidget(QLabel("Age:"))
        form_layout.addWidget(self.age_input)

        form_layout.addWidget(QLabel("Email:"))
        form_layout.addWidget(self.email_input)

        form_layout.addWidget(QLabel("Position:"))
        form_layout.addWidget(self.role_combo)

        
        # ----- Color  -----
        form_layout.addWidget(QLabel("Your favorite color:"))

        color_layout = QHBoxLayout()

        self.color_preview = QLabel()
        self.color_preview.setFixedSize(30, 30)
        self.color_preview.setStyleSheet(
            f"background-color: {self.card_color}; border: 1px solid black;"
        )

        self.color_btn = QPushButton("Pick New Color")
        self.color_btn.clicked.connect(self.pick_color)

        color_layout.addWidget(self.color_preview)
        color_layout.addWidget(self.color_btn)

        form_layout.addLayout(color_layout)

        self.display = QTextEdit()
        self.display.setReadOnly(True)

        self.set_placeholder_card()

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.display)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # ---------------- CARD ----------------
    def set_placeholder_card(self):
        placeholder_card = """
        <div style="font-family:Segoe UI;">
            <h1 style="font-size:30px; margin-bottom:5px;">
                Your name here
            </h1>

            <p style="font-size:16px; margin-top:0;">
                (Age)
            </p>

            <br>

            <h3 style="font-size:20px; font-weight:500;">
                Your position here
            </h3>

            <p style="font-size:15px;">
                ✉ your_username@domain.name
            </p>

            <br>

            <p style="color:gray; font-size:14px;">
                Fill in your details and click generate
            </p>
        </div>
        """

        self.display.setHtml(placeholder_card)
        self.update_card_style()

    # ---------------- MENU ----------------
    def create_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")

        generate_action = QAction("Generate Card", self)
        generate_action.triggered.connect(self.generate_card)
        file_menu.addAction(generate_action)

        save_action = QAction("Save Card", self)
        save_action.triggered.connect(self.save_card)
        file_menu.addAction(save_action)

        clear_display_action = QAction("Clear Display", self)
        clear_display_action.triggered.connect(self.clear_display)
        file_menu.addAction(clear_display_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu("Edit")

        copy_action = QAction("Copy Card", self)
        copy_action.triggered.connect(self.copy_card)
        edit_menu.addAction(copy_action)

        clear_form_action = QAction("Clear Form", self)
        clear_form_action.triggered.connect(self.clear_form)
        edit_menu.addAction(clear_form_action)

    # ---------------- TOOLBAR ----------------
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        generate_icon = self.style().standardIcon(QStyle.SP_MediaPlay)
        generate_action = QAction(generate_icon, "Generate", self)
        generate_action.triggered.connect(self.generate_card)
        toolbar.addAction(generate_action)

        save_icon = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        save_action = QAction(save_icon, "Save", self)
        save_action.triggered.connect(self.save_card)
        toolbar.addAction(save_action)

        clear_icon = self.style().standardIcon(QStyle.SP_TrashIcon)
        clear_action = QAction(clear_icon, "Clear All", self)
        clear_action.triggered.connect(self.clear_all)
        toolbar.addAction(clear_action)

    # ---------------- CARD STYLE ----------------
    def update_card_style(self):
        self.display.setStyleSheet(f"""
            QTextEdit {{
                background-color: {self.card_color};
                border-radius: 18px;
                padding: 25px;
                border: none;
            }}
        """)

    # ---------------- FUNCTIONS ----------------
    def generate_card(self):
        name = self.name_input.text()
        age = self.age_input.value()
        role = self.role_combo.text()
        email = self.email_input.text()

        if name == '':
            print("please name")
            return
        if age < 18:
            print("valid age please")
            return
        if role == '':
            print("need role")
            return
        if email == '':
            print("need email")
            return

        card_html = f"""
        <div style="font-family:Segoe UI;">
            <h1 style="font-size:30px; margin-bottom:5px;">
                {name}
            </h1>

            <p style="font-size:16px; margin-top:0;">
                ({age})
            </p>

            <br>

            <h3 style="font-size:20px; font-weight:500;">
                {role}
            </h3>

            <p style="font-size:15px;">
                ✉ {email}
            </p>
        </div>
        """

        self.display.setHtml(card_html)
        self.update_card_style()
        self.statusBar().showMessage("Card generated.")

    def save_card(self):
        text = self.display.toPlainText()
        if not text.strip():
            QMessageBox.warning(self, "Warning", "No card to save.")
            return

        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text Files (*.txt)"
        )

        if file_name:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(text)
            self.statusBar().showMessage(f"Saved to {file_name}")

    def copy_card(self):
        QApplication.clipboard().setText(self.display.toPlainText())
        self.statusBar().showMessage("Card copied to clipboard.")

    def clear_form(self):
        self.name_input.clear()
        self.age_input.setValue(25)
        self.email_input.clear()
        self.role_input.clear()
        self.statusBar().showMessage("Form cleared.")

    def clear_display(self):
        self.set_placeholder_card()
        self.statusBar().showMessage("Display cleared.")

    def clear_all(self):
        self.clear_form()
        self.set_placeholder_card()
        self.statusBar().showMessage("Form and display cleared.")

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.card_color = color.name()
            self.color_preview.setStyleSheet(
                f"background-color: {self.card_color}; border: 1px solid black;"
            )
            self.update_card_style()
            self.statusBar().showMessage("Card color changed.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PersonalInfoCard()
    window.show()
    sys.exit(app.exec())