import socket

from controller import ClientController
import tkinter as tk
import tkinter.messagebox as messagebox
from lab6.server.server import IP_ADDRESS, PORT
import socket


class MainWindow(tk.Frame):

    def show_fatal(self, reason):
        messagebox.showerror("Fatal", "There was an error: " + str(reason))
        exit(-1)

    def __init__(self, window_root):

        try:
            self.controller = ClientController()
        except Exception as e:
            self.show_fatal(e)

        tk.Frame.__init__(self, window_root)

        self.expression_label = tk.Label(window_root, text="Enter the expression")
        self.expression_label.grid(row=0)
        self.expression_entry = tk.Entry(window_root, width=10)
        self.expression_entry.grid(row=1)
        self.send_button = tk.Button(window_root, text="Send", command=self.send_expression)
        self.send_button.grid(row=2)
        self.result_label = tk.Label(window_root, text="Result:")
        self.result_label.grid(row=4)

    def send_expression(self):
        try:

            if len(str(self.expression_entry.get())) == 0:
                return

            self.result_label.config(
                text=str(self.controller.send_expression(
                    str(self.expression_entry.get())
                )))
        except Exception as e:
            self.show_fatal(e)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("170x170")
    root.title("Expression")
    app = MainWindow(root)
    root.mainloop()
