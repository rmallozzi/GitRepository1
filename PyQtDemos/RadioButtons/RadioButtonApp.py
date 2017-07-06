import sys
from PyQt4 import QtCore, QtGui, uic

#--------------------------------
#Below is the line that needs to be changed depending upon the name of the
#output file from Qt Designer. It is the xml .ui file.

qtCreatorFile = "RadioButtonsUI.ui" # Enter file here.

#--------------------------------

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #connect clicked signals to action. Buttons were added to a QButtonGroup object when creating the UI
        radButtons = self.radButtonGroup.buttons()
        for button in radButtons:
            button.clicked.connect(self.buttonClicked)

    #button click callback method. When creating the radio buttons in Qt Designer, they were put into a a
    #QButtonGroup object with the exclusive option set.
    def buttonClicked(self):
        #figure out which button in group was clicked
        for button in self.radButtonGroup.buttons():
            if button.isChecked():
                whichButtonName = button.text()

        newtext = whichButtonName.append(' was Clicked')
        #append output to textbox
        self.textEditOutput.append(newtext)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())