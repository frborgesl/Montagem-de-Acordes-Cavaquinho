# QUALQUER NOTA +4 +3 SEMITONS
from PyQt5 import  uic,QtWidgets
from PyQt5 import QtGui


def mostra_acordes(self):
    if tela_um.btn_C.isChecked():
        acorde_C.show()
        self.do_maior = QtWidgets.QLabel(self)
        self.do_maior.move(50,400)
        self.do_maior.setPixmap(QtGui.QPixmap("C.png"))


    elif tela_um.btn_Csus.isChecked():
        acorde_Csus.show()
    elif tela_um.btn_D.isChecked():
        acorde_D.show()
    elif tela_um.btn_Dsus.isChecked():
        acorde_Dsus.show()
    elif tela_um.btn_E.isChecked():
        acorde_E.show()
    elif tela_um.btn_F.isChecked():
        acorde_F.show()
    elif tela_um.btn_Fsus.isChecked():
        acorde_Fsus.show()
    elif tela_um.btn_G.isChecked():
        acorde_G.show()
    elif tela_um.btn_Gsus.isChecked():
        acorde_Gsus.show()
    elif tela_um.btn_A.isChecked():
        acorde_A.show()
    elif tela_um.btn_Asus.isChecked():
        acorde_Asus.show()
    else:
        acorde_B.show()


app = QtWidgets.QApplication([])
tela_um = uic.loadUi("TelaInicial.ui")
acorde_C = uic.loadUi("TriadeMaior_C.ui")
acorde_Csus = uic.loadUi("TriadeMaior_Csus.ui")
acorde_D = uic.loadUi("TriadeMaior_D.ui")
acorde_Dsus = uic.loadUi("TriadeMaior_Dsus.ui")
acorde_E = uic.loadUi("TriadeMaior_E.ui")
acorde_F = uic.loadUi("TriadeMaior_F.ui")
acorde_Fsus = uic.loadUi("TriadeMaior_Fsus.ui")
acorde_G = uic.loadUi("TriadeMaior_G.ui")
acorde_Gsus = uic.loadUi("TriadeMaior_Gsus.ui")
acorde_A = uic.loadUi("TriadeMaior_A.ui")
acorde_Asus = uic.loadUi("TriadeMaior_Asus.ui")
acorde_B = uic.loadUi("TriadeMaior_B.ui")




tela_um.pushButton.clicked.connect(mostra_acordes)


tela_um.show()
app.exec()