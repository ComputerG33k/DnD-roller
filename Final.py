from tkinter import *
import random
class Dice(Frame):
    def __init__(self):
        #Create the main frame
        Frame.__init__(self, bg = "#cc6600")
        self.master.title("DnD dice and Character stats")
        self.grid()
        self._D4Var = IntVar()
        self._D6Var = IntVar()
        self._D8Var = IntVar()
        self._D10Var = IntVar()
        self._D12Var = IntVar()
        self._D20Var = IntVar()
        self._D100Var = IntVar()
        
        #Create and add widgets
        self._outputArea = Text(self, width = 4, height = 7)
        self._outputArea.grid(row = 8, column = 1, sticky = W + E + N + S)
        self._image = PhotoImage(file = "Dice.gif")
        self._imageLabel = Label(self, image = self._image)
        self._imageLabel.grid(row = 0, column = 0, padx = 200, columnspan = 4)
        self._labelD4 = Label(self, text = "D4 Times to roll", bg = "#cc9900")
        self._labelD4.grid(row = 1, column = 0, sticky = W)
        self._entryD4 = Entry(self, textvariable = self._D4Var)
        self._entryD4.grid(row = 1, column = 1)
        self._labelD6 = Label(self, text = "D6 Times to roll", bg = "#cc9900")
        self._labelD6.grid(row = 2, column = 0, sticky = W)
        self._entryD6 = Entry(self, textvariable = self._D6Var)
        self._entryD6.grid(row = 2, column = 1)
        self._labelD8 = Label(self, text = "D8 Times to roll", bg = "#cc9900")
        self._labelD8.grid(row = 3, column = 0, sticky = W)
        self._entryD8 = Entry(self, textvariable = self._D8Var)
        self._entryD8.grid(row = 3, column = 1)
        self._labelD10 = Label(self, text = "D10 Times to roll", bg = "#cc9900")
        self._labelD10.grid(row = 4, column = 0, sticky = W)
        self._entryD10 = Entry(self, textvariable = self._D10Var)
        self._entryD10.grid(row = 4, column = 1)
        self._labelD12 = Label(self, text = "D12 Times to roll", bg = "#cc9900")
        self._labelD12.grid(row = 5, column = 0, sticky = W)
        self._entryD12 = Entry(self, textvariable = self._D12Var)
        self._entryD12.grid(row = 5, column = 1)
        self._labelD20 = Label(self, text = "D20 Times to roll", bg = "#cc9900")
        self._labelD20.grid(row = 6, column = 0, sticky = W)
        self._entryD20 = Entry(self, textvariable = self._D20Var)
        self._entryD20.grid(row = 6, column = 1)
        self._labelD100 = Label(self, text = "D100 Times to roll", bg = "#cc9900")
        self._labelD100.grid(row = 7, column = 0, sticky = W)
        self._entryD100 = Entry(self, textvariable = self._D100Var)
        self._entryD100.grid(row = 7, column = 1)
        
        #Buttons
        self._buttonD4 = Button(self, text = "D4", command = self.rollD4)
        self._buttonD6 = Button(self, text = "D6", command = self.rollD6)
        self._buttonD8 = Button(self, text = "D8", command = self.rollD8)
        self._buttonD10 = Button(self, text = "D10", command = self.rollD10)
        self._buttonD12 = Button(self, text = "D12", command = self.rollD12)
        self._buttonD20 = Button(self, text = "D20", command = self.rollD20)
        self._buttonD100 = Button(self, text = "D100", command = self.rollD100)
        self._button4d6 = Button(self, text = "4d6 drop lowest", command = self.roll4D6)
        self._buttonD4.grid(row = 1, column = 8,)
        self._buttonD6.grid(row = 2, column = 8,)
        self._buttonD8.grid(row = 3, column = 8,)
        self._buttonD10.grid(row = 4, column = 8,)
        self._buttonD12.grid(row = 5, column = 8,)
        self._buttonD20.grid(row = 6, column = 8,)
        self._buttonD100.grid(row = 7, column = 8,)
        self._button4d6.grid(row = 8, column = 8,)

    def rollD4(self):
        self.clear()
        repeat = self._D4Var.get()
        count = 0
        while count < repeat:
            roll = random.randint(1,4)
            count += 1
            self.show(roll)
        
    def rollD6(self):
        self.clear()
        repeat = self._D6Var.get()
        count = 0
        while count < repeat:
            roll = random.randint(1,6)
            count += 1
            self.show(roll)

    def rollD8(self):
        self.clear()
        repeat = self._D8Var.get()
        count = 0
        while count < repeat:
            roll = random.randint(1,8)
            count += 1
            self.show(roll)

    def rollD10(self):
        self.clear()
        repeat = self._D10Var.get()
        count = 0
        while count < repeat:
            roll = random.randint(1,10)
            count += 1
            self.show(roll)

    def rollD12(self):
        self.clear()
        repeat = self._D12Var.get()
        count = 0
        while count < repeat:
            roll = random.randint(1,12)
            count += 1
            self.show(roll)

    def rollD20(self):
        repeat = self._D20Var.get()
        self.clear()
        count = 0
        while count < repeat:
            roll = random.randint(1,20)
            count += 1
            self.show(roll)

    def rollD100(self):
        self.clear()
        repeat = self._D100Var.get()
        count = 0
        while count < repeat:
            roll = random.randint(1,100)
            count += 1
            self.show(roll)

    def show(self, stat):
        self._outputArea.insert("1.0", str(stat) + '\n')
            
    def roll4D6(self):
        self.clear()
        for x in range(6):
            stats = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
            lowest = stats[0]
            lowestIndex = 0

            for x in stats:
                if x < lowest:
                    lowest = x
                    lowestIndex = stats.index(x)
            stats.pop(lowestIndex)
            stat = 0
            for x in stats:
                stat += x
            self.show(stat)
    
    def clear(self):
        self._outputArea.delete("1.0", END)
        
def main():
    Dice().mainloop()

main()
