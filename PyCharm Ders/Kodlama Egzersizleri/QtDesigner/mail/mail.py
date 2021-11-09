# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mail.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import time

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(428, 312)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 51, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.edit_mail = QtWidgets.QLineEdit(Form)
        self.edit_mail.setGeometry(QtCore.QRect(80, 20, 311, 21))
        self.edit_mail.setObjectName("edit_mail")
        self.edit_konu = QtWidgets.QLineEdit(Form)
        self.edit_konu.setGeometry(QtCore.QRect(80, 50, 311, 21))
        self.edit_konu.setObjectName("edit_konu")
        self.edit_mesaj = QtWidgets.QTextEdit(Form)
        self.edit_mesaj.setGeometry(QtCore.QRect(80, 80, 311, 131))
        self.edit_mesaj.setObjectName("edit_mesaj")
        self.gonder_btn = QtWidgets.QPushButton(Form)
        self.gonder_btn.setGeometry(QtCore.QRect(180, 250, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gonder_btn.setFont(font)
        self.gonder_btn.setObjectName("gonder_btn")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 220, 180, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.gonder_btn.clicked.connect(self.mailGonder)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Gmail   :"))
        self.label_2.setText(_translate("Form", "Konu    :"))
        self.label_3.setText(_translate("Form", "Mesaj  :"))
        self.gonder_btn.setText(_translate("Form", "Gönder"))

    def mailGonder(self):

        if self.edit_mail.text().count("@") == 1 and self.edit_mail.text() != "":
            mesaj = MIMEMultipart()
            yazı = self.edit_mesaj.toPlainText()
            mesaj_govdesi = MIMEText(yazı, "plain")
            mesaj.attach(mesaj_govdesi)
            mesaj["From"] = "bencankurt17@gmail.com"
            mesaj["Subject"] = self.edit_konu.text()
            mesaj["To"] = self.edit_mail.text()
            try:
                mail = smtplib.SMTP("smtp.gmail.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login("bencankurt17@gmail.com", "29963207974Can.")
                mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
                self.label_4.setText("Mail gönderildi.")
                mail.close()
            except:
                self.label_4.setText("Bir sorun oluştu")
        else:
            self.label_4.setText("Mail giriniz.")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())