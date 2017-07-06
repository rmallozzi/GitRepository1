import sys
from PyQt4 import QtCore, QtGui, uic

#--------------------------------
#Below is the line that needs to be changed depending upon the name of the
#output file from Qt Designer. It is the xml .ui file.

qtCreatorFile = "SliderUI.ui" # Enter file here.

#--------------------------------

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #connect slider to its callback
        self.sliderCntrl1.valueChanged.connect(self.sliderValueChanged)

    #button click callback method
    def sliderValueChanged(self):
        sliderVal = self.sliderCntrl1.sliderPosition()
        newtext = 'Slider Changed. New position = {}'.format(sliderVal)
        #append output to textbox
        self.textEditOutput.append(newtext)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())