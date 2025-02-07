# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaMenu(object):
    def setupUi(self, TelaMenu):
        TelaMenu.setObjectName("TelaMenu")
        TelaMenu.resize(472, 337)
        self.centralwidget = QtWidgets.QWidget(TelaMenu)
        self.centralwidget.setObjectName("centralwidget")
        TelaMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastros = QtWidgets.QMenu(self.menubar)
        self.menuCadastros.setObjectName("menuCadastros")
        self.menuRelatorios = QtWidgets.QMenu(self.menubar)
        self.menuRelatorios.setObjectName("menuRelatorios")
        TelaMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaMenu)
        self.statusbar.setObjectName("statusbar")
        TelaMenu.setStatusBar(self.statusbar)
        self.actionCadProduto = QtWidgets.QAction(TelaMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("prod.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCadProduto.setIcon(icon)
        self.actionCadProduto.setObjectName("actionCadProduto")
        
        self.actionCadProduto.triggered.connect(self.cadastrar_produto)
        
        self.actionCadVendedor = QtWidgets.QAction(TelaMenu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("vend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCadVendedor.setIcon(icon1)
        self.actionCadVendedor.setObjectName("actionCadVendedor")
        self.actionSair = QtWidgets.QAction(TelaMenu)
        self.actionSair.setObjectName("actionSair")
        
        self.actionSair.triggered.connect(self.sair)
        
        self.actionRelVendas = QtWidgets.QAction(TelaMenu)
        self.actionRelVendas.setObjectName("actionRelVendas")
        self.actionRelCompras = QtWidgets.QAction(TelaMenu)
        self.actionRelCompras.setObjectName("actionRelCompras")
        self.actionOpcao1 = QtWidgets.QAction(TelaMenu)
        self.actionOpcao1.setCheckable(True)
        self.actionOpcao1.setObjectName("actionOpcao1")
        self.actionOpcao2 = QtWidgets.QAction(TelaMenu)
        self.actionOpcao2.setObjectName("actionOpcao2")
        self.menuCadastros.addAction(self.actionCadProduto)
        self.menuCadastros.addAction(self.actionCadVendedor)
        self.menuCadastros.addSeparator()
        self.menuCadastros.addAction(self.actionSair)
        self.menuRelatorios.addAction(self.actionRelVendas)
        self.menuRelatorios.addAction(self.actionRelCompras)
        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuRelatorios.menuAction())

        self.retranslateUi(TelaMenu)
        QtCore.QMetaObject.connectSlotsByName(TelaMenu)

    def retranslateUi(self, TelaMenu):
        _translate = QtCore.QCoreApplication.translate
        TelaMenu.setWindowTitle(_translate("TelaMenu", "MainWindow"))
        self.menuCadastros.setTitle(_translate("TelaMenu", "&Cadastros"))
        self.menuRelatorios.setTitle(_translate("TelaMenu", "&Relatórios"))
        self.actionCadProduto.setText(_translate("TelaMenu", "&Produto"))
        self.actionCadProduto.setShortcut(_translate("TelaMenu", "Ctrl+P"))
        self.actionCadVendedor.setText(_translate("TelaMenu", "&Vendedor"))
        self.actionCadVendedor.setShortcut(_translate("TelaMenu", "Ctrl+V"))
        self.actionSair.setText(_translate("TelaMenu", "Sai&r"))
        self.actionSair.setShortcut(_translate("TelaMenu", "Alt+S"))
        self.actionRelVendas.setText(_translate("TelaMenu", "&Vendas"))
        self.actionRelCompras.setText(_translate("TelaMenu", "&Compras"))
        self.actionOpcao1.setText(_translate("TelaMenu", "Opcao1"))
        self.actionOpcao2.setText(_translate("TelaMenu", "Opcao2"))

    def sair(self):
        sys.exit()
        #TelaMenu.close()
        
    def cadastrar_produto(self):
        #print("ABRIU A TELA DE CADASTRO DE PRODUTO.")
        
        from cproduto import Ui_CadProduto
        self.tela = QtWidgets.QMainWindow()
        self.cad = Ui_CadProduto()
        self.cad.setupUi(self.tela)
        self.tela.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaMenu = QtWidgets.QMainWindow()
    ui = Ui_TelaMenu()
    ui.setupUi(TelaMenu)
    TelaMenu.show()
    sys.exit(app.exec_())
