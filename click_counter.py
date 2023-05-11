"""
Click counter

Program is a GUI that has four buttons.
Reset: The changed values are changed back to the same as in beginning.
Increase: Increases the value in the label at the top of the window by one.
Decrease: Decreases the value in the label at the top of the window by one.
Quit: End the program.

 Writer of the program

 Name: EILeh
"""

from tkinter import *


class Counter:
    def __init__(self):

        self.__mainwindow = Tk()

        self.__current_value = 0
        self.__current_value_label = Label(self.__mainwindow,
                                           text=self.__current_value)
        self.__current_value_label.grid(row=0, columnspan=5)

        self.__reset_button = Button(self.__mainwindow, text="Reset",
                                     command=self.reset)
        self.__reset_button.grid(row=1, column=0)

        self.__increase_button = Button(self.__mainwindow, text="Increase",
                                     command=self.increase)
        self.__increase_button.grid(row=1, column=2)

        self.__decrease_button = Button(self.__mainwindow, text="Decrease",
                                     command=self.decrease)
        self.__decrease_button.grid(row=1, column=3)

        self.__quit_button = Button(self.__mainwindow, text="Quit",
                                     command=self.quit)
        self.__quit_button.grid(row=1, column=4)

        self.__mainwindow.mainloop()

    def reset(self):
        self.__current_value = 0
        self.__current_value_label.configure(text=self.__current_value)

    def increase(self):
        self.__current_value += 1
        self.__current_value_label.configure(text=self.__current_value)

    def decrease(self):
        self.__current_value -= 1
        self.__current_value_label.configure(text=self.__current_value)

    def quit(self):
        self.__mainwindow.destroy()


def main():

    Counter()


if __name__ == "__main__":
    main()
