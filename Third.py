
import sys
from PySide.QtGui import QApplication, QWidget, QIcon, QLabel, QFont, QToolTip, QPushButton, QMessageBox, QDesktopWidget

# __author__ 'Timothy P Marion'

class SampleWindow(QWidget):
    """ Our Main Window Class """

    # Constructor Function
    def __init__(self):
        # type: () -> object
        QWidget.__init__(self)
        self.setWindowTitle("Icon Sample")
        self.setGeometry(200, 300, 400, 150)
        QToolTip.setFont(QFont("Decorative", 8, QFont.Bold))
        self.setToolTip('Our Main WIndow')
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(300)
        self.setMaximumWidth(800)

    def setIcon(self):
        """ Function to set Icon"""
        appIcon = QIcon('pyside_logo.png')
        self.setWindowIcon(appIcon)

    def setIconMode(self):

        myIcon1 = QIcon('pyside_logo.png')
        myLabel1 = QLabel('sample', self)
        pixmap1 = myIcon1.pixmap(50, 50, QIcon.Active, QIcon.On)
        myLabel1.setPixmap(pixmap1)
        myLabel1.setToolTip('Active')

        myIcon2 = QIcon('pyside_logo.png')
        myLabel2 = QLabel('sample', self)
        pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
        myLabel2.setPixmap(pixmap2)
        myLabel2.move(50, 0)
        myLabel2.setToolTip('Disabled')

        myIcon3 = QIcon('pyside_logo.png')
        myLabel3 = QLabel('sample', self)
        pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
        myLabel3.setPixmap(pixmap3)
        myLabel3.move(100, 0)
        myLabel3.setToolTip('Selected')

    def setButton(self):
        """Function to add a quit button
        """
        myButton = QPushButton('Quit', self)
        myButton.move(50, 100)
        myButton.clicked.connect(self.quitApp)

    def quitApp(self):
        """ Function to confirm a message from the user
        """
        userInfo = QMessageBox.question(self, 'Confirmation',
                                        "This will quit the application. Do you want to Continue?",
                                        QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            myApp.quit()
        if userInfo == QMessageBox.No:
            pass

    def center(self):
        """ Function ti center the application
        """
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def setAboutButton(self):
        """ Function to set about button
        """
        self.aboutButton = QPushButton("About", self)
        self.aboutButton.move(150, 100)
        self.aboutButton.clicked.connect(self.showAbout)

    def showAbout(self):
        """ Funtion to show about button
        """
        QMessageBox.about(self.aboutButton, "About Pyside",
                          "Copyright 2016 Timothy P Marion")

    def setAboutQtButton(self):
        """ Function to set Qt button
        """
        self.aboutQtButton = QPushButton("Qt", self)
        self.aboutQtButton.move(250, 100)
        self.aboutQtButton.clicked.connect(self.showQtAbout)

    def showQtAbout(self):
        """ Function to set Qt Button
        """
        QMessageBox.aboutQt(self.aboutQtButton)


if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        myWindow.setIcon()
        myWindow.setIconMode()
        myWindow.setButton()
        myWindow.center()
        myWindow.setAboutButton()
        myWindow.setAboutQtButton()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)

    except NameError:
        print("Name Error", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
