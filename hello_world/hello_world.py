from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('My First App')
label = QLabel('Hello World!')
label.setAlignment(Qt.AlignCenter)
window.setCentralWidget(label)

window.show()
app.exec_()