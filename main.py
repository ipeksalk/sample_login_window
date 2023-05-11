import sys
from PyQt5.QtWidgets import QApplication
from LoginGuiLib import Login


app = QApplication(sys.argv) # An app object is required to create a Qt app

gui = Login("password.txt") # Create an instance of Login class from the library, passing the password file's name as an argument to the constructor of Login class
gui.show() # Start showing the gui on the screen

sys.exit(app.exec_()) # Shut down python when gui is closed by user click to close button
