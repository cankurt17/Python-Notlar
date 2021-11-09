

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout



class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.checkbox=QCheckBox("Python")
        self.yazi=QLabel("")
        self.buton=QPushButton("Tıkla")

        v_box=QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.buton)
        self.setLayout(v_box)

        self.setWindowTitle("Checkbox")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked()))

        self.show()

    def click(self,checkbox):
        if checkbox:
            self.yazi.setText("Python seçildi.")
        else:
            self.yazi.setText("Python seçilmedi.")



app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())