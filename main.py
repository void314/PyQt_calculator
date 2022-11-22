import sys 
from os import path
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

gui_path = path.join(path.dirname(__file__), 'gui.ui')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(gui_path, self)

        # window settings (at your discretion)

        self.setWindowTitle("MyCalc")

        self.lE_out.setPlaceholderText("...")

        self.set_functions() # binding events to objects

    # function declaration

    def set_functions(self):
        self.pB_1.clicked.connect(lambda: self.writeSimbol('1'))
        self.pB_2.clicked.connect(lambda: self.writeSimbol('2'))
        self.pB_3.clicked.connect(lambda: self.writeSimbol('3'))
        self.pB_4.clicked.connect(lambda: self.writeSimbol('4'))
        self.pB_5.clicked.connect(lambda: self.writeSimbol('5'))
        self.pB_6.clicked.connect(lambda: self.writeSimbol('6'))
        self.pB_7.clicked.connect(lambda: self.writeSimbol('7'))
        self.pB_8.clicked.connect(lambda: self.writeSimbol('8'))
        self.pB_9.clicked.connect(lambda: self.writeSimbol('9'))
        self.pB_0.clicked.connect(lambda: self.writeSimbol('0'))
        self.pB_plass.clicked.connect(lambda: self.writeSimbol('+'))
        self.pB_minus.clicked.connect(lambda: self.writeSimbol('-'))

        self.pB_equals.clicked.connect(lambda: self.results())

    def writeSimbol(self, simbol: str):
        self.lE_out.setText(self.lE_out.text() + simbol)

    def results(self):
        try:
            if len(self.lE_out.text()) > 0:
                self.lE_out.setText(str(eval(self.lE_out.text())))
            else:
                self.lE_out.setText('')
        except Exception as e:
            self.lE_out.setText('')

            error = QMessageBox(QMessageBox.Icon.Warning, "Input ERROR", str(e))
            error.exec()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
        main()