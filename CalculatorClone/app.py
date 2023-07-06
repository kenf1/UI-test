import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Calculator")
        self.setContentsMargins(20,20,20,20)
        self.resize(400,600)

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        #input buttons
        for i in range(3):
            for j in range(3):
                button = QPushButton(f"{10-(i*3+j+1)}")
                grid.addWidget(button,i,j)

        self.show()

if __name__ == "__main__":
    app = QApplication([])
    calc = Calculator()
    app.exec()

    sys.exit(app.exec())