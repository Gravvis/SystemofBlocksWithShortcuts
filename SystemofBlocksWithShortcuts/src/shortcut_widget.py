from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from taskwidget import TaskWidget

class ShortcutWidget(QWidget):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.icon_label = QLabel()
        self.icon_label.setFixedSize(64, 64)
        self.layout.addWidget(self.icon_label)

        self.file_name_label = QLabel(file_path)
        self.layout.addWidget(self.file_name_label)

        self.task_button = QPushButton("Open Task")
        self.task_button.clicked.connect(self.open_task_widget)
        self.layout.addWidget(self.task_button)

        self.set_icon()

    def set_icon(self):
        icon_path = "assets/icons/placeholder_icon.png"
        icon = QIcon(icon_path)
        self.icon_label.setPixmap(icon.pixmap(64, 64))

    def open_task_widget(self):
        task_widget = TaskWidget(self.file_path)
        task_widget.show()