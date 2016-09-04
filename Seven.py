# import required modules

import sys, time
from PySide.QtGui import QApplication, QMainWindow, QStatusBar, QProgressBar, QLabel, QTextEdit, QIcon, QKeySequence, QAction, QMessageBox

class MainWindow(QMainWindow):
    """ Create the Application Main Window CLass
    """
    def __init__(self):
        """ Constructor FUnction
        """
        QMainWindow.__init__(self)
        self.setWindowTitle("Application Title Here")
        self.setGeometry(300, 250, 400, 300)

    def SetupComponents(self):
        """ Setting the Central Widget
        """
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 10000)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.CreateActions()
        self.CreateMenus()
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.pasteAction)
        self.helpMenu.addAction(self.aboutAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.aboutCopyrightAction)
        self.CreateToolBar()
        self.mainToolBar.addAction(self.newAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.copyAction)
        self.mainToolBar.addAction(self.pasteAction)

    # Slots called when the action menus are triggered
    def newFile(self):
       self.textEdit.setText('')

    def exitFile(self):
        self.close()

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor",
                          "This example demonstrates the use "
                          "of Menu Bar")
    def aboutCopyright(self):
        QMessageBox.about(self, "About Simple Text Editor",
                          "This example demonstrates the use "
                          "of Copyright Bar")

    def CreateActions(self):
        """ Function to create actions for menus
        """
        self.newAction = QAction(QIcon('new.png'), '&New',
                                  self, shortcut=QKeySequence.New,
                                  statusTip="Create a New File",
                                  triggered=self.newFile)
        self.exitAction = QAction(QIcon('exit.png'), 'E&xit',
                                  self, shortcut="Ctrl+Q",
                                  statusTip="Exit the Application",
                                  triggered=self.exitFile)
        self.copyAction = QAction(QIcon('copy.png'), 'C&opy',
                                  self, shortcut="Ctrl+C",
                                  statusTip="Copy",
                                  triggered=self.textEdit.copy)
        self.pasteAction = QAction(QIcon('paste.png'), '&Paste',
                                   self, shortcut="Ctrl+V",
                                   statusTip="Paste",
                                   triggered=self.textEdit.paste)
        self.aboutAction = QAction(QIcon('about.png'), 'A&bout',
                                   self, statusTip="Displays info about text editor",
                                   triggered=self.aboutHelp)
        self.aboutCopyrightAction = QAction(QIcon('about.png'), '&Copyright',
                                   self, statusTip="Displays info about Copyright",
                                   triggered=self.aboutCopyright)

    def CreateMenus(self):
        """ Function to create actual menu bar
        """
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.viewMenu = self.menuBar().addMenu("&View")
        self.helpMenu = self.menuBar().addMenu("&Help")

    def CreateToolBar(self):
        """ Function to create tool bar
        """
        self.mainToolBar = self.addToolBar('Main')

if __name__ == '__main__':
    # Exception Handeling
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetupComponents()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

