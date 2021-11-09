

import sys
from PyQt5 import QtWidgets
import sqlite3

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.baglanti_olustur()

        self.init_ui()

    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uyeler (kullanici_adi TEXT,parola TEXT)")
        baglanti.commit()

    def init_ui(self):

        self.k_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris=QtWidgets.QPushButton("Giriş yap")
        self.yazi=QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.k_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")

        self.giris.clicked.connect(self.login)

        self.show()

    def login(self):
        adi=self.k_adi.text()
        parola=self.parola.text()

        self.cursor.execute("SELECT * FROM uyeler WHERE kullanici_adi = ?and parola =?",(adi,parola))
        data = self.cursor.fetchall()
        if  len(data)==0:
            self.yazi.setText("Böyle bir kullanıcı yok.\nLütfen tekrar deneyiniz...")
        else:
            self.yazi.setText("Hoşgeldiniz "+adi+".")
app=QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())

