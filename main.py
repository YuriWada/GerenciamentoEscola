from system.schoolsystem import *

class Management:
    def __init__(self):
        self.schoolsystem = SchoolSystem()
    
    def run(self):
        try:
            self.schoolsystem.run()
        except:
            pass

if __name__ == '__main__':
    management = Management()
    management.run()