# import required modules

import sys, time
from PySide.QtGui import QApplication, QMainWindow, QStatusBar, QProgressBar, QLabel, QTextEdit, QIcon, QKeySequence

class MainWindow(QMainWindow):
    """ Create the Application Main Window CLass
    """
    def __init__(self):
        """ Constructor FUnction
        """
        QMainWindow.__init__(self)
        self.setWindowTitle("Application Title Here")
        self.setGeometry(300, 250, 400, 300)
        self.statusLabel = QLabel('Showing Progress')
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(1000000)


    def CreateStatusBar(self):
        """ Funtion to Create Status Bar
        """
        self.myStatusBar = QStatusBar()
        self.progressBar.setValue(10)
        self.myStatusBar.addWidget(self.statusLabel, 1)
        self.myStatusBar.addWidget(self.progressBar, 2)
        self.setStatusBar(self.myStatusBar)

    def ShowProgress(self):
        """ Function to Show Progress
        """
        while self.progressBar.value() < self.progressBar.maximum():
            self.progressBar.setValue(self.progressBar.value() + 1)
        self.statusLabel.setText('Ready')

    def SetupCompponents(self):
        """ Setting the Central Widget
        """
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

if __name__ == '__main__':
    # Exception Handeling
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.CreateStatusBar()
        mainWindow.SetupCompponents()
        mainWindow.show()
        mainWindow.ShowProgress()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

