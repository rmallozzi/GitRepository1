import sys
from PyQt4 import QtCore, QtGui, uic

#--------------------------------
#Below is the line that needs to be changed depending upon the name of the
#output file from Qt Designer. It is the xml .ui file.

qtCreatorFile = "GraphicsView.ui" # Enter file here.

#--------------------------------

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #set up jpg image
        pxmap = QtGui.QPixmap('ticks2.jpg')
        self.labelForImage.setPixmap(pxmap)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())