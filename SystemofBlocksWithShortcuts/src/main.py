import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
import random
import os
import colorsys

from task_widget import TaskWidget

class ShortcutWidget(QWidget):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.icon_label = QLabel()
        self.icon_label.setFixedSize(64, 64)
        self.layout.addWidget(self.icon_label)

        self.file_name_label = QLabel(os.path.basename(file_path))
        self.layout.addWidget(self.file_name_label)

        self.set_icon()
        self.set_color()

    def set_icon(self):
        icon_path = "assets/icons/placeholder_icon.png"
        icon = QIcon(icon_path)
        self.icon_label.setPixmap(icon.pixmap(64, 64))

    def set_color(self):
        base_hue = random.randint(0, 359) / 360.0  # Random base hue value
        offset = random.randint(120, 180) / 360.0  # Random offset for complimentary color
        hue = (base_hue + offset) % 1.0  # Complimentary hue
        saturation = random.uniform(0.6, 0.9)  # Random saturation between 0.6 and 0.9
        lightness = random.uniform(0.6, 0.9)  # Random lightness between 0.6 and 0.9
        r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)

        color = f"rgb({int(r * 255)}, {int(g * 255)}, {int(b * 255)})"
        self.setStyleSheet(f"background-color: {color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shortcut Widget")
        self.setGeometry(200, 200, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_shortcut_widgets()

    def create_shortcut_widgets(self):
        file_paths = [
            "path/to/file1.txt",
            "path/to/file2.txt",
            "path/to/file3.txt",
            # Add more file paths here
        ]

        for file_path in file_paths:
            shortcut_widget = ShortcutWidget(file_path)
            self.layout.addWidget(shortcut_widget)


if __name__ == "__main__":
    # Check if dependencies are installed
    try:
        import PyQt5
        import pywin32
    except ImportError as e:
        error_message = f"Error: {str(e)}"
        error_message += "\n\nPlease make sure the following dependencies are installed:\n\n"
        error_message += "- PyQt5: Official website - https://www.riverbankcomputing.com/software/pyqt/\n"
        error_message += "- pywin32: Official website - https://github.com/mhammond/pywin32\n"

        # Display error message in a popup window
        app = QApplication(sys.argv)
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Dependency Error")
        error_box.setText(error_message)
        error_box.exec()

        sys.exit(1)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())