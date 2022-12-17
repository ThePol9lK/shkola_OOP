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
        a = int(self.ui.enter_1.text())
        x = int(self.ui.enter_2.text())
        if a <= 0 or abs(x) < 1:
            raise ValueError(self.ui.answer.setText("x or n can't be less"))
        s = x
        for k in range(2, a + 1):
            s += ((-1) ** (k - 1)) * (x ** (2 * k - 1)) / (2 * k - 1)
        self.ui.answer.setText(f'Answer is {s}')

    def the_button_was_clicked(self):
      print("Clicked!")


def main():
    app = QApplication(sys.argv)
    window = Count()

    window.show()

    sys.exit(app.exec())

main()