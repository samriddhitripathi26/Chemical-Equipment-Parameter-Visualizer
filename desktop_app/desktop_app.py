import sys
import pandas as pd

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFileDialog, QTableWidget,
    QTableWidgetItem, QMessageBox, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class CSVUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Equipment CSV Upload")
        self.setGeometry(200, 100, 900, 650)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #0f0f0f;
                color: #e5e5e5;
                font-family: Segoe UI;
                font-size: 14px;
            }

            QFrame {
                background-color: #181818;
                border-radius: 14px;
            }

            QLabel#title {
                font-size: 22px;
                font-weight: 600;
            }

            QLabel#subtitle {
                color: #9a9a9a;
                margin-bottom: 12px;
            }

            QPushButton {
                background-color: #2d2d2d;
                border: 1px solid #3a3a3a;
                padding: 10px 24px;
                border-radius: 8px;
                font-size: 15px;
            }

            QPushButton:hover {
                background-color: #3a3a3a;
            }

            QPushButton:disabled {
                background-color: #1f1f1f;
                color: #666;
            }

            QTableWidget {
                background-color: #121212;
                gridline-color: #2a2a2a;
                border: none;
            }

            QHeaderView::section {
                background-color: #1f1f1f;
                padding: 10px;
                border: none;
                font-weight: 600;
            }

            QTableWidget::item {
                padding: 8px;
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(40, 30, 40, 30)

        # ===== Upload Card =====
        self.upload_card = QFrame()
        upload_layout = QVBoxLayout(self.upload_card)
        upload_layout.setSpacing(14)

        title = QLabel("Equipment CSV Upload")
        title.setObjectName("title")

        subtitle = QLabel("Upload your CSV file to analyze equipment data")
        subtitle.setObjectName("subtitle")

        self.file_label = QLabel("No file selected")

        self.upload_btn = QPushButton("Upload CSV")
        self.upload_btn.clicked.connect(self.load_csv)

        upload_layout.addWidget(title)
        upload_layout.addWidget(subtitle)
        upload_layout.addWidget(self.file_label)
        upload_layout.addWidget(self.upload_btn)

        # ===== Summary Card =====
        self.summary_card = QFrame()
        self.summary_card.hide()
        summary_layout = QVBoxLayout(self.summary_card)

        self.summary_label = QLabel("Upload Summary")
        self.summary_label.setFont(QFont("Segoe UI", 16, QFont.Bold))

        self.count_label = QLabel("Total Equipment: 0")

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(
            ["Flowrate", "Pressure", "Temperature", "Type"]
        )

        summary_layout.addWidget(self.summary_label)
        summary_layout.addWidget(self.count_label)
        summary_layout.addWidget(self.table)

        main_layout.addWidget(self.upload_card)
        main_layout.addWidget(self.summary_card)

    def load_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        self.file_label.setText(file_path.split("/")[-1])
        self.upload_btn.setDisabled(True)
        self.upload_btn.setText("Uploading...")

        try:
            df = pd.read_csv(file_path)
            required = ["Flowrate", "Pressure", "Temperature", "Type"]

            for col in required:
                if col not in df.columns:
                    raise ValueError(f"Missing column: {col}")

            self.populate_table(df)
            self.summary_card.show()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

        finally:
            self.upload_btn.setDisabled(False)
            self.upload_btn.setText("Upload CSV")

    def populate_table(self, df):
        self.table.setRowCount(len(df))
        self.count_label.setText(f"Total Equipment: {len(df)}")

        for row in range(len(df)):
            self.table.setItem(row, 0, QTableWidgetItem(str(df.iloc[row]["Flowrate"])))
            self.table.setItem(row, 1, QTableWidgetItem(str(df.iloc[row]["Pressure"])))
            self.table.setItem(row, 2, QTableWidgetItem(str(df.iloc[row]["Temperature"])))
            self.table.setItem(row, 3, QTableWidgetItem(str(df.iloc[row]["Type"])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CSVUploader()
    window.show()
    sys.exit(app.exec_())