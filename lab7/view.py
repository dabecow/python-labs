import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
import controller
from model import *
from tkinter import messagebox


class MainWindow(tk.Frame):
    def __init__(self, window_root):

        tk.Frame.__init__(self, window_root)

        self.add_product_label = tk.Label(window_root, text="Add product")
        self.add_product_label.grid(column=0, row=0)

        self.name_entry = tk.Entry(window_root, width=10)
        self.name_entry.grid(column=0, row=2)

        self.department_combobox = ttk.Combobox(window_root, width=10, state="readonly",
                                                values=controller.get_departments_names_list())

        self.department_combobox.grid(column=0, row=3)

        self.price_entry = tk.Entry(window_root, width=10)
        self.price_entry.grid(column=0, row=4)

        self.description_entry = tk.Entry(window_root, width=10)
        self.description_entry.grid(column=0, row=5)

        self.add_product_button = tk.Button(window_root, text="Add", command=self.add_product_button_clicked)
        self.add_product_button.grid(column=0, row=6)

        self.output_text = scrolledtext.ScrolledText(window_root, width=70, height=10)
        self.output_text.grid(row=9, column=0, columnspan=10)

        self.delete_product_label = tk.Label(window_root, text="Delete")
        self.delete_product_label.grid(column=1, row=0)

        self.id_delete_entry = tk.Entry(window_root, width=10)
        self.id_delete_entry.grid(column=1, row=1)

        self.delete_product_button = tk.Button(window_root, text="Delete", command=self.delete_product_button_clicked)
        self.delete_product_button.grid(column=1, row=2)

        self.search_by_department_combobox = ttk.Combobox(window_root, width=10, state="readonly",
                                                          values=controller.get_departments_names_list())
        self.search_by_department_combobox.grid(column=2, row=1)

        self.department_search_button = tk.Button(window_root, text="Search",
                                                  command=self.search_by_department_button_clicked)
        self.department_search_button.grid(column=2, row=2)

        self.update_scroll_text()

    def update_scroll_text(self):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.INSERT, controller.main_list_to_string())

    def update_scroll_text_by(self, text):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.INSERT, text)

    def add_product_button_clicked(self):
        try:
            controller.add_product(Product(
                self.name_entry.get(),
                controller.get_department_by_name(self.department_combobox.get()),
                self.price_entry.get(),
                self.description_entry.get()
            ))

            self.update_scroll_text()

        except Exception as e:
            messagebox.showerror(e.__str__())

    def delete_product_button_clicked(self):
        try:
            controller.remove_product(controller.find_product_by_id(
                int(self.id_delete_entry.get())
            ))

            self.update_scroll_text()

        except Exception as e:
            messagebox.showerror("Error", e.__str__())

    def search_by_department_button_clicked(self):
        try:
            text = controller.list_to_string(
                controller.get_products_list_from_department(
                    self.search_by_department_combobox.get()
                ))

            self.update_scroll_text_by(text)

        except Exception as e:
            messagebox.showerror("Error", e.__str__())


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x400")
    root.title("Products")
    app = MainWindow(root)
    root.mainloop()
