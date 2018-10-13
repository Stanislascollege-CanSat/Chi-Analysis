try:
    import tkinter as tk
except:
    '''
        Program cannot run, due to wrong python version.
    '''

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()