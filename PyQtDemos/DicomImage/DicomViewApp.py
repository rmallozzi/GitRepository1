import sys
from PyQt4 import QtCore, QtGui, uic
import dicom
import numpy as np

#--------------------------------
#Below is the line that needs to be changed depending upon the name of the
#output file from Qt Designer. It is the xml .ui file.

qtCreatorFile = "DicomViewUI.ui" # Enter file here.

#--------------------------------

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #read dicom image
        dcfile = dicom.read_file('Slice93.dcm')
        imagedata = dcfile.pixel_array #numpy array

        #rescale data for 8-bit because QImage doesn't support 16-bit format. Convert to float first before scaling so that
        #rescaling transformations operate properly without over-ranging.
        maxval = imagedata.max()
        minval = imagedata.min()
        tmpImage = (imagedata-minval).astype('float')
        rescaledImage = ( (tmpImage/tmpImage.max())*255 ).astype(np.uint8)

        #load numpy image data into a QImage object, resize it to 512x512, then load into QPixmap
        (nrow,ncol) = rescaledImage.shape
        qimg = QtGui.QImage(rescaledImage,ncol,nrow,ncol,QtGui.QImage.Format_Indexed8)
        qimg_resized = qimg.scaled(512,512,QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
        pxmap = QtGui.QPixmap.fromImage(qimg_resized)
        self.imageDisplay.setPixmap(pxmap)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

