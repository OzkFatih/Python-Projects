from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
         # Set window properties
        self.setWindowTitle("Chat Program")
        self.setGeometry(100, 100, 400, 500)
         # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
         # Create layouts
        main_layout = QVBoxLayout()
        message_layout = QHBoxLayout()
        send_layout = QHBoxLayout()
         # Create widgets
        self.message_box = QTextEdit()
        self.message_box.setReadOnly(True)
        self.message_input = QLineEdit()
        self.send_button = QPushButton("Send")
         # Add widgets to layouts
        message_layout.addWidget(self.message_box)
        send_layout.addWidget(self.message_input)
        send_layout.addWidget(self.send_button)
         # Add layouts to main layout
        main_layout.addLayout(message_layout)
        main_layout.addLayout(send_layout)
         # Set main layout
        central_widget.setLayout(main_layout)
         # Connect signals to slots
        self.send_button.clicked.connect(self.send_message)
        self.message_input.returnPressed.connect(self.send_message)
    def send_message(self):
        message = self.message_input.text()
        if message:
            self.message_box.append(message)
            self.message_input.clear()
            self.message_box.verticalScrollBar().setValue(self.message_box.verticalScrollBar().maximum())
if __name__ == '__main__':
    app = QApplication([])
    window = ChatWindow()
    window.show()
    app.exec()