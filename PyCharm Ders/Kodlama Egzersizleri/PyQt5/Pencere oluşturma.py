



import sys
from PyQt5 import  QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Ders 1")
    pencere.setGeometry(100,100,500,500)

    text=QtWidgets.QLabel(pencere)
    image=QtWidgets.QLabel(pencere)
    button=QtWidgets.QPushButton(pencere)

    button.setText("Button")
    button.move(200,350)

    text.setText("Selam Pyhton.")
    image.setPixmap(QtGui.QPixmap("python.png"))

    text.move(200,100)
    image.move(70,150)

    pencere.show()
    sys.exit(app.exec_())

Pencere()