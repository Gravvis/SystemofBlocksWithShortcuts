from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QTextEdit
from PyQt5.QtGui import QPalette, QColor, QPainter
from PyQt5.QtCore import Qt

class TaskWidget(QWidget):
    def __init__(self, task):
        super().__init__()
        self.task = task
        self.completed = False
        self.draggable = True
        self.resizable = True
        self.transparency = 1.0

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.task_textedit = QTextEdit(self.task)
        self.task_textedit.setReadOnly(True)
        self.task_textedit.setLineWrapMode(QTextEdit.WidgetWidth)
        self.task_textedit.textChanged.connect(self.update_size)
        self.layout.addWidget(self.task_textedit)

        self.completed_checkbox = QCheckBox("Completed")
        self.completed_checkbox.stateChanged.connect(self.toggle_completed)
        self.layout.addWidget(self.completed_checkbox)

        self.setFixedSize(200, 100)
        self.setStyleSheet("border: 2px solid transparent;")

    def is_completed(self):
        return self.completed

    def toggle_completed(self, state):
        self.completed = state == Qt.Checked
        self.update()

    def set_draggable(self, draggable):
        self.draggable = draggable

    def set_resizable(self, resizable):
        self.resizable = resizable

    def set_transparency(self, transparency):
        self.transparency = transparency
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.completed:
            painter = QPainter(self)
            border_color = QColor(255, 0, 0)
            border_color.setAlphaF(self.transparency)
            painter.setPen(border_color)
            painter.setBrush(Qt.NoBrush)
            painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.draggable:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.draggable:
            delta = event.pos() - self.drag_start_position
            new_position = self.pos() + delta
            self.move(new_position)

    def resizeEvent(self, event):
        if self.resizable:
            super().resizeEvent(event)

    def update_size(self):
        self.task_textedit.document().adjustSize()
        width = max(self.task_textedit.sizeHint().width(), self.size().width())
        self.setFixedWidth(width)

    def enterEvent(self, event):
        self.setStyleSheet("border: 2px solid #00FF00;")

    def leaveEvent(self, event):
        self.setStyleSheet("border: 2px solid transparent;")