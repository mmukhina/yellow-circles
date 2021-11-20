import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Yellow Circle')
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        try:
            self.paint()
        except Exception as e:
            print(e)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        size = random.randint(0, 600)
        x = random.randint(0, 600 - size)
        y = random.randint(0, 600 - size)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, size, size)

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
