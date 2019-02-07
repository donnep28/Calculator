from tkinter import *

class calculator(object):

    Count = 0

    def __init__(self, master, stack = []):
        # Set up application
        self.stack = stack
        self.master = master
        master.title('Calculator App')

        # create screen widget
        self.screen = Text(master, state = 'disabled', width = 40, height = 4, background = 'black', foreground = 'green')

        # Position screen in window
        self.screen.grid(row = 0, column = 0, columnspan = 5, padx = 6, pady = 6)
        self.screen.configure(state = 'normal')

        # Initialize screen value as empty
        self.equation = ''

        # Create the widgets for the buttons
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton('C')
        b5 = self.createButton('(')
        b6 = self.createButton(4)
        b7 = self.createButton(5)
        b8 = self.createButton(6)
        b9 = self.createButton('/')
        b10 = self.createButton(')')
        b11 = self.createButton(1)
        b12 = self.createButton(2)
        b13 = self.createButton(3)
        b14 = self.createButton('*')
        b15 = self.createButton('CE')
        b16 = self.createButton('.')
        b17 = self.createButton(0)
        b18 = self.createButton('%')
        b19 = self.createButton('-')
        b20 = self.createButton('+')
        b21 = self.createButton('=',None,34)

        # Store buttons in a list
        buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21]

        # Initialize counter
        count = 0
        # arrange buttons in grid
        for row in range(1,5):
            for column in range(5):
                buttons[count].grid(row = row, column = column)
                count += 1
        # Add the space bar on the bottom
        buttons[19].grid(row = 4, column = 4, columnspan = 3, rowspan = 2)
        buttons[20].grid(row = 5, column = 0, columnspan = 4)

    def createButton(self, val, write = True, width = 8):
        if val == '+':
            return Button(self.master, text = val, command = lambda: self.click(val, write), width = width, height = 3)
        return Button(self.master, text = val, command = lambda: self.click(val, write), width = width)

    def click(self, text, write):
        if text == '=' and self.equation:
            self.equals()
        elif text == 'C':
            self.clear_screen()
        elif text == 'CE' and self.equation:
            self.undo()
        else:
            self.insert_screen(text)

    def equals(self):
        print(self.equation)
        answer = str(eval(self.equation))
        self.clear_screen()
        self.insert_screen(answer, newline = True)

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state = 'normal')
        self.screen.delete('1.0', END)

    def undo(self):
        self.equation = ''
        i = 0
        while i < (len(self.stack) - 1):
            self.equation += self.stack[i]
            i += 1
        self.stack = self.stack[0:-1]
        self.screen.configure(state = 'normal')
        self.screen.delete('1.0', END)
        self.screen.insert(END, self.equation)
        calculator.Count -= 1
        self.screen.configure(state = 'disabled')


    def insert_screen(self, value, newline = False):
        self.screen.configure(state = 'normal')
        self.screen.insert(END, value)
        self.stack.append(str(value))
        self.equation += self.stack[calculator.Count]
        calculator.Count += 1
        self.screen.configure(state = 'disabled')

root = Tk()
my_gui = calculator(root)
root.mainloop()
