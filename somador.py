# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(250, 200)
        Janela.setMinimumSize(QtCore.QSize(200, 200))
        Janela.setMaximumSize(QtCore.QSize(1080, 820))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Downloads/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Janela.setWindowIcon(icon)
        Janela.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_valor1 = QtWidgets.QLabel(self.centralwidget)
        self.label_valor1.setObjectName("label_valor1")
        self.gridLayout.addWidget(self.label_valor1, 0, 0, 1, 1)
        self.label_valor2 = QtWidgets.QLabel(self.centralwidget)
        self.label_valor2.setObjectName("label_valor2")
        self.gridLayout.addWidget(self.label_valor2, 1, 0, 1, 1)
        self.lineEdit_valor1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_valor1.setObjectName("lineEdit_valor1")
        self.gridLayout.addWidget(self.lineEdit_valor1, 0, 1, 1, 1)
        self.lineEdit_valor2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_valor2.setObjectName("lineEdit_valor2")
        self.gridLayout.addWidget(self.lineEdit_valor2, 1, 1, 1, 1)
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setObjectName("label_resultado")
        self.gridLayout.addWidget(self.label_resultado, 5, 0, 1, 1)
        self.lineEdit_3_result = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3_result.setObjectName("lineEdit_3_result")
        self.gridLayout.addWidget(self.lineEdit_3_result, 5, 1, 1, 1)
        self.pushButton_somar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_somar.setObjectName("pushButton_somar")
        
        self.pushButton_somar.clicked.connect(self.somar) # liga o botao
                                                          # à função
        self.gridLayout.addWidget(self.pushButton_somar, 2, 1, 1, 1)
        Janela.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Somador"))
        self.label_valor1.setText(_translate("Janela", "Valor 1:"))
        self.label_valor2.setText(_translate("Janela", "Valor 2:"))
        self.label_resultado.setText(_translate("Janela", "Resultado:"))
        self.pushButton_somar.setText(_translate("Janela", "SOMAR"))
        
        
    def somar(self):
        v1 = int(self.lineEdit_valor1.text()) # capturar a digitação
        v2 = int(self.lineEdit_valor2.text())
        soma = v1 + v2
        self.lineEdit_3_result.setText(str(soma))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec_())
