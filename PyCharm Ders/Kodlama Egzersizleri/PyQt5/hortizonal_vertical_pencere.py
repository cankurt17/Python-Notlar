



import sys
from PyQt5 import  QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    """h_box=QtWidgets.QHBoxLayout()
    h_box.addWidget(okay)
    h_box.addStretch()
    h_box.addWidget(cancel)"""

    """v_box=QtWidgets.QVBoxLayout()
    v_box.addWidget(okay)
    v_box.addStretch()
    v_box.addWidget(cancel)"""

    h_box=QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box=QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Ders 1")
    pencere.setGeometry(100, 100, 500, 500)

    #pencere.setLayout(h_box)
    pencere.setLayout(v_box)

    pencere.show()
    sys.exit(app.exec_())


Pencere()