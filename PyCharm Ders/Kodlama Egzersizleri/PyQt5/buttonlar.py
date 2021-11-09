

import sys
from PyQt5 import QtWidgets,QtGui

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,500)
        self.init_ui()
    def init_ui(self):
        self.yazı_alanı=QtWidgets.QLabel("Bana henüz tıklanmadı...")
        self.button=QtWidgets.QPushButton("Bana Tıkla")
        self.say=0

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.button)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.button.clicked.connect(self.click)

        self.show()

    def click(self):
        self.say +=1
        self.yazı_alanı.setText("Bana {} kez tıklandı".format(self.say))

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
