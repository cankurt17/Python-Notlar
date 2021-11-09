

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout



class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.radio_yazisi=QLabel("Hangi dilleri biliyorsunuz?")
        self.java=QRadioButton("Java")
        self.php=QRadioButton("Php")
        self.python=QRadioButton("Python")
        self.html=QRadioButton("Html")
        self.arduino=QRadioButton("Arduino")
        self.yazi_alanı=QLabel("")
        self.buton=QPushButton("Gönder")

        v_box=QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.php)
        v_box.addWidget(self.python)
        v_box.addWidget(self.html)
        v_box.addWidget(self.arduino)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alanı)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.buton.clicked.connect(lambda :self.click(self.java.isChecked(),self.php.isChecked(),self.python.isChecked(),self.html.isChecked(),self.arduino.isChecked(),self.yazi_alanı))

        self.show()

    def click(self,java,php,python,html,aruino,yazi):
        if java:
            yazi.setText("Java")
        if php:
            yazi.setText("Php")
        if python:
            yazi.setText("Python")
        if html:
            yazi.setText("Html")
        if aruino:
            yazi.setText("Arduino")




app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())