import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QPushButton,
    QVBoxLayout, QLineEdit, QMainWindow
)
from PyQt6.QtCore import Qt, QSize

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Calculator")
        self.setContentsMargins(20,20,20,20)
        self.resize(400,400)

    #create UI
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight) #align right, text size modified in styles.css
        self.display.setMinimumSize(QSize(100,100))
        layout.addWidget(self.display)

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        #numbers + operations (done this way to change rows easily)
        r1,r2,r3,r4 = 0,1,2,3
        buttons = [
            ("7",r1,0),("8",r1,1),("9",r1,2),("/",r1,3),
            ("4",r2,0),("5",r2,1),("6",r2,2),("*",r2,3),
            ("1",r3,0),("2",r3,1),("3",r3,2),("-",r3,3),
            ("0",r4,0),(".",r4,1),("=",r4,2),("+",r4,3),
        ]

        for text,row,col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_button_clicked)
            button.setMinimumSize(QSize(50,50))
            grid_layout.addWidget(button,row,col)

        #clear input/output
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_all)
        clear_button.setStyleSheet("background-color: #f6b26b; font-size: 25px; color: black")
        layout.addWidget(clear_button)

    #calculations
    def on_button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

    def clear_all(self):
        self.display.clear()

if __name__ == "__main__":
    app = QApplication([])
    calc = Calculator()
    calc.show()

    with open("./CalculatorClone/styles.css","r") as file:
        calc.setStyleSheet(file.read())

    sys.exit(app.exec())