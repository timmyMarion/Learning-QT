import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QLabel

# Main Function
if __name__ == '__main__':

    # Create the main application
    myApp = QApplication(sys.argv)

    # Create a label and set its properties
    appLabel = QLabel()
    appLabel.setText("Hello World \n Look at my first app using PySide")
    appLabel.setAlignment(Qt.AlignCenter)
    appLabel.setWindowTitle("My first application")
    appLabel.setGeometry(300, 300, 250, 150)

    # Show the label
    appLabel.show()

    # Execute the application and exit
    myApp.exec_()
    sys.exit
