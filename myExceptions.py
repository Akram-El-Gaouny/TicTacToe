class Error(Exception):
    pass

class CellNotEmptyError(Error):
    def __init__(self, message = "The Cell that you picked is Not Empty"):
        self.message = message

class InvalidInputError(Error):
    def __init__(self, message = "The Value you entered is not valid in this context"):
        self.message = message
class HelpError(Error):
    def __init__(self):
        self.message = """
The Following Board Displays The Values Of Corresponding Cells 
Simply Enter The Number You Want to Play When It Is Your Turn!
 1 | 2 | 3 
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
"""
    def __str__(self):
        return self.message
