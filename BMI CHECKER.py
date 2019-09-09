from tkinter import *


class Bmi:
    def __init__(self):

        self.frame = Frame(root, width=500, height=350).pack
        root.title("BMI CALCULATOR BY SAINT")

        self.name_label = Label(root, text="Enter your name ").pack()
        self.name = StringVar()
        self.name_input = Entry(root, textvariable=self.name).pack()

        self.weight_label = Label(root, text='Enter your weight').pack()
        self.weight = StringVar()
        self.weight_inputblock_1 = Entry(root, textvariable=self.weight).pack()

        self.height_label=Label(root, text="Enter your height").pack()
        self.height = StringVar()
        self.height_inputblock_1= Entry(root, textvariable=self.height).pack()

        self.button = StringVar()
        Button(root, fg= "red", textvariable=self.button, command=self.calculation).pack()
        self.button.set("Calculate")

        Label(root, textvariable=self.name).pack()

        self.bmi_value = StringVar()
        Label(root, textvariable=self.bmi_value).pack()

    def calculation(self):
        self.name = input(" ")
        weight = float(input(": "))
        height = float(input("Enter your height: "))
        bmi = weight / (height**2)
        self.bmi_value.set(f"your BMI score of {bmi}")


root = Tk()

call = Bmi()

root.mainloop()