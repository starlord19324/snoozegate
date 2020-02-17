from PySide import QtCore, QtGui
import sys
from ui import Ui_MainWindow

# Create application
app = QtGui.QApplication(sys.argv)

# Create form and init UI
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Hook logic

# Run main loop
sys.exit(app.exec_())
