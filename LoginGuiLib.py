from PyQt5.QtWidgets import QWidget,QMainWindow,QLineEdit,QPushButton,QMessageBox,QVBoxLayout,QGridLayout,QSizePolicy
import hashlib


class Login(QMainWindow): # Create a class of type QMainWindow for password/login screen gui frame

    def __init__(self, pwdFileName): # Default constructor, Login class takes password file name as an argument
        
        super(Login, self).__init__() # Default constructor of parent class

        self.clickCount = 0 # Instance variables for click counter, user input password and the database password filename
        self.password = ''
        self.pwdFileName = pwdFileName
        
        self.__uiBuild() # Initialize the class with my own gui constructor


    def __uiBuild(self):
        
        self.resize(420,450) # Give initial sizes to the gui window
        self.setWindowTitle("Password GUI") # Set the title of the gui window
        
        self.__createLayout() # Create a layout for widget organization
        self.__createTextBox() # Create a text box as display
        self.__createButtons() # Create buttons for user interaction
        self.__connectSignals() # Connect button press signals with appropriate slots to invoke necessary methods
        

    def __createLayout(self):

        self.generalLayout = QVBoxLayout() # Create a layout for widget organization
        self._centralWidget = QWidget(self) # Create a central widget of type QWidget
        self.setCentralWidget(self._centralWidget) # Set the central widget
        self._centralWidget.setLayout(self.generalLayout) # Set the created layout as the layout of the central widget

    def __createTextBox(self):
        
        self.display = QLineEdit() # Create an instance of QLineEdit to act as display of password field
        self.display.setFixedHeight(60) # Set height of the text box
        self.display.setReadOnly(True) # Type password only by clicking buttons, typing from the keyboard is restricted by this setter method
        self.generalLayout.addWidget(self.display) # Adding the QLineEdit widget to general layout


    def __createButtons(self):

        self.buttons = {} # Create a dictionary to store button objects
        buttonsLayout = QGridLayout() # Create a grid layout for button widgets  
        buttons={ '1': (0, 0), # Create a dictionary to store construction parameters of button objects
                  '2': (0, 1),
                  '3': (0, 2),
                  '4': (1, 0),
                  '5': (1, 1),
                  '6': (1, 2),
                  '7': (2, 0),
                  '8': (2, 1),
                  '9': (2, 2),
                  'C': (3, 0),
                  '0': (3, 1),
                  'Enter': (3, 2)}
        
        for btnText, pos in buttons.items(): # Iterations throughout the buttons dictionary
             self.buttons[btnText] = QPushButton(btnText) # Create buttons using button names and corresponding grid positions throughout the buttons dictionary
             self.buttons[btnText].resize(50, 40) # Give initial sizes to buttons in the gui window
             self.buttons[btnText].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) # Resize buttons automatically when the window size is changed
             buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1]) # Adding button widgets to button layout
             self.generalLayout.addLayout(buttonsLayout) # Adding button layout to the general layout of the gui window


    def __connectSignals(self): 
        
        self.buttons['0'].clicked.connect(self.__click) # If a number button is pressed, invoke _click method
        self.buttons['1'].clicked.connect(self.__click)
        self.buttons['2'].clicked.connect(self.__click)
        self.buttons['3'].clicked.connect(self.__click)
        self.buttons['4'].clicked.connect(self.__click)
        self.buttons['5'].clicked.connect(self.__click)
        self.buttons['6'].clicked.connect(self.__click)
        self.buttons['7'].clicked.connect(self.__click)
        self.buttons['8'].clicked.connect(self.__click)
        self.buttons['9'].clicked.connect(self.__click)
        self.buttons['C'].clicked.connect(self.__clearLine) # If clear (C) button is pressed, invoke _clearLine method
        self.buttons['Enter'].clicked.connect(self.__hashPassword) # If enter button is pressed, invoke _hashPassword method


    def __click(self):

        self.clickCount += 1 # Increment  click counter by 1
        self.display.setText('#' * self.clickCount) # Display clickcount amount of "#" in the password field
        self.display.text() # Update display

        sender = self.sender() # Get properties of sender of the signal
        self.password = self.password + sender.text() # Add the name of the pushed button (signal sender) to password string
        
            
    def __clearLine(self):

        self.display.setText(" ") # Set the password field to empty string
        self.display.text() # Update display
        
        self.clickCount = 0 # Reset the click counter
        
        self.password = '' # Reset the password string to empty


    def __hashPassword(self):

        salt = '5752b37fddff7' # Given salt value is held in a local variable in _hashPassword method
        pwd = self.password + salt # Set the local variable pwd to concatenation of user input password and salt

        result = hashlib.sha256(pwd.encode()).hexdigest() # Hash the user input password with salt and store it in a local variable

        self.__checkPassword(result) # Pass the resulting hash to _checkPassword method


    def __checkPassword(self,hashedpwd):

        with open(self.pwdFileName, 'r') as file: # Open the password file in read-only mode, 'with' command automatically closes the file after assignment
            storedPassword = file.read() # Store the hash in the password file in a local variable

        self.__showMsg(hashedpwd == storedPassword) # Pass the boolean value to _showMsg method

        self.__clearLine() # Clear the password field in the gui


    def __showMsg(self,flag):

        msg=QMessageBox() # Create a message box instance
        msg.setWindowTitle(" ") # with no title

        if (flag): # If the password the user entered is correct, then the message box says "Login Successful"
            msg.setText("Login Successful")
            
        else: # If the password the user entered is wrong, then the message box says "Wrong Password" on a red background as requested
            msg.setStyleSheet("background-color: rgb(255, 0, 0);")
            msg.setText("Wrong Password")

        msg.exec_() # Show the message on screen
