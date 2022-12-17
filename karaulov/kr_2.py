import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow


class Count(QMainWindow):
    def __init__(self):
      super(Count, self).__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)

      self.ui.pushButton.clicked.connect(lambda: self.on_click())

    def on_click(self):
        n = int(self.ui.enter_2.text())
        x = float(self.ui.enter_1.text())
        if n <= 0:
            raise ValueError(self.ui.answer.setText("n can't be less"))
        if x < -1 or x >= 1:
            raise ValueError(self.ui.answer.setText("x should be in between -1 and 1"))
        s = 0
        for k in range(1, n + 1):
            s += ((-1) ** (k + 1) * x ** k) / k
        self.ui.answer.setText(f'Answer is {s}')

    def the_button_was_clicked(self):
      print("Clicked!")


def main():
    app = QApplication(sys.argv)
    window = Count()

    window.show()

    sys.exit(app.exec())

main()