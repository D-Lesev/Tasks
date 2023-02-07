import sys

from PyQt6.QtWidgets import (
    QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
)


class DistanceCalculator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_edit = QLineEdit()

        self.type_distance = QComboBox()
        self.type_distance.addItems(["Metric (km)", "Imperial (miles)"])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_distance)
        self.output_label = QLabel("")

        # Add widgets to the grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_edit, 0, 1)
        grid.addWidget(self.type_distance, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        self.setLayout(grid)

    def calculate_distance(self):
        constant_speed_miles = 1.609
        current_speed = float(self.distance_edit.text()) / int(self.time_edit.text())
        if self.type_distance.currentText().startswith("Metric"):
            self.output_label.setText(f"Average speed: {current_speed:.2f} km/h")
        elif self.type_distance.currentText().startswith("Imperial"):
            cur_speed_imperial = current_speed / constant_speed_miles
            self.output_label.setText(f"Average speed: {cur_speed_imperial:.2f} mph")


app = QApplication(sys.argv)
dist_calculator = DistanceCalculator()
dist_calculator.show()
sys.exit(app.exec())
