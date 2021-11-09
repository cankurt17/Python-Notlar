

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout



class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        self.yazi=QTextEdit()
        self.buton=QPushButton("Temizle")

        v_box=QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.buton.clicked.connect(self.click)

        self.show()

    def click(self):
        self.yazi.clear()


app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())