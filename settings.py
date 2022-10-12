class Settings:
    ''' a class to store settings for number generator '''
    ''' can change settings for GUI later on ... '''

    def __init__(self):
        ''' initialize settings '''

        self.max = 10
        
    def easy_mode(self):
        self.max = 10
        return self.max
        
    def medium_mode(self):
        self.max = 100
        return self.max
        
    def hard_mode(self):
        self.max = 1000
        return self.max
        
    def custom_mode(self, max):
        self.max = max
        return self.max