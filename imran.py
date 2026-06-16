class IMRAN:
    def __init__(self, name):
        self.name = name
    
    def Print(self):
        try:
            return self.name.capitalize()
        except TypeError:
            return "Invalid Input"