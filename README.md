# Sample Login Window

In this project, it is implemented a password input window using [Python3](https://www.python.org/downloads/) & [PyQT5](https://pypi.org/project/PyQt5/).
Users enter their passwords using the number buttons on the GUI and then the password
written is compared with the content of the password file. 

### GUI
The user enters the password using the number buttons on the GUI then hits ‘Enter’
button to login. Each number appear as ‘#’ on the input field and user can delete all the
written input by clicking on the ‘C’ button. If the entered password is correct a message box
with a message saying “Login Successful” appears on the screen, in case of failure the
message box should say “Wrong Password”, on red background.

### Password File
The password file contains only one line, which is the correct value of the password
hashed by using sha256 with a salt value. Sample example values for the password file are
as follows
Password : 123456
Salt : 5752b37fddff7
Content of the password file :
'26430f85ee7675d8c74fd9c913ffe60f4e9ed7ba4c93c8cca6ee8157c0919d55'

### Usage
```
python main.py
```