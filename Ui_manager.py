from tkinter import *


class Ui_manager():
    __window = Tk()
    __active_buttons = list()
    __button_result = IntVar()
    __choice_result = IntVar()
    __current_label = None

    @staticmethod
    def run():
        Ui_manager.__window.geometry("500x400")
        Ui_manager.__window.title("Eternal land")

    @staticmethod
    def clear():
        if Ui_manager.__current_label != None:
            Ui_manager.__current_label.destroy()
            Ui_manager.__current_label = None
        if len(Ui_manager.__active_buttons) != 0:
            for button in Ui_manager.__active_buttons:
                button.destroy()
            Ui_manager.__active_buttons = list()

    @staticmethod
    def create_label(out_massege):
        label = Label(master=Ui_manager.__window, text=out_massege)
        Ui_manager.__current_label = label
        label.pack()

    @staticmethod
    def add_radiobutton(input_massage, value):
        rb = Radiobutton(master=Ui_manager.__window, text=input_massage, value=value,
                         variable=Ui_manager.__choice_result)
        Ui_manager.__active_buttons.append(rb)
        rb.pack()


    @staticmethod
    def wait_result():
        button = Button(master=Ui_manager.__window, text="Далее", command=Ui_manager.__on_click)
        button.pack()
        Ui_manager.__active_buttons.append(button)
        button.wait_variable(Ui_manager.__button_result)
        return Ui_manager.__button_result.get()

    @staticmethod
    def wait_continue():
        is_click = BooleanVar()
        next_button = Button(master=Ui_manager.__window, text="Далее", command=lambda: is_click.set(True))
        next_button.pack()
        Ui_manager.__active_buttons.append(next_button)
        next_button.wait_variable(is_click)


    @staticmethod
    def __on_click():
        if Ui_manager.__choice_result.get() == 0:
            return
        Ui_manager.__button_result.set(Ui_manager.__choice_result.get())
