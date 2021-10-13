import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
from lab3.controller import ProductController
from lab3.model import Product
from tkinter import messagebox
from tkinter import filedialog


class MainWindow(tk.Frame):
    def __init__(self, window_root):

        self.product_controller = ProductController()

        tk.Frame.__init__(self, window_root)
        self.menu_bar = tk.Menu()
        self.file_menu = tk.Menu()
        self.about_menu = tk.Menu()
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)

        self.file_menu.add_command(label="Create", command=self.create_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.save)
        self.file_menu.add_command(label="Save as", command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.quit)

        self.about_menu.add_command(label="Programmer", command=self.show_about)

        window_root.configure(menu=self.menu_bar)

        self.add_product_label = tk.Label(window_root, text="Add product")
        self.add_product_label.grid(column=0, row=0)

        self.id_entry = tk.Entry(window_root, width=10)
        self.id_entry.grid(column=0, row=1)

        self.name_entry = tk.Entry(window_root, width=10)
        self.name_entry.grid(column=0, row=2)

        self.department_combobox = ttk.Combobox(window_root, width=10, text="Department",
                                                values=['Milk', 'Meat', 'Bread'])
        self.department_combobox.grid(column=0, row=3)

        self.price_entry = tk.Entry(window_root, width=10)
        self.price_entry.grid(column=0, row=4)

        self.description_entry = tk.Entry(window_root, width=10)
        self.description_entry.grid(column=0, row=5)

        self.add_product_button = tk.Button(window_root, text="Add", command=self.add_product_button_clicked)
        self.add_product_button.grid(column=0, row=6)

        self.checked = tk.BooleanVar()
        self.checked.set(True)

        self.debug_check_box = tk.Checkbutton(window_root, variable=self.checked, text="Update")
        self.debug_check_box.grid(column=0, row=8)

        self.output_text = scrolledtext.ScrolledText(window_root, width=70, height=10)
        self.output_text.grid(row=9, column=0, columnspan=10)

        self.delete_product_label = tk.Label(window_root, text="Delete")
        self.delete_product_label.grid(column=1, row=0)

        self.id_delete_entry = tk.Entry(window_root, width=10)
        self.id_delete_entry.grid(column=1, row=1)

        self.delete_product_button = tk.Button(window_root, text="Delete", command=self.delete_product_button_clicked)
        self.delete_product_button.grid(column=1, row=2)

        self.search_by_department_label = tk.Label(window_root, text="Search by department")
        self.search_by_department_label.grid(column=2, row=0)

        self.department_search_entry = tk.Entry(window_root, width=10)
        self.department_search_entry.grid(column=2, row=1)

        self.department_search_button = tk.Button(window_root, text="Search",
                                                  command=self.search_by_department_button_clicked)
        self.department_search_button.grid(column=2, row=2)

    def update_scroll_text(self):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.INSERT, self.product_controller.main_list_to_string())

    def update_scroll_text_by(self, text):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.INSERT, text)

    def add_product_button_clicked(self):
        try:
            self.product_controller.add_product(Product(
                int(self.id_entry.get()),
                self.name_entry.get(),
                self.department_combobox.get(),
                self.price_entry.get(),
                self.description_entry.get()
            ))

            if self.checked.get():
                self.update_scroll_text()
        except Exception as e:
            self.show_error_dialog(e.args[0])

    def delete_product_button_clicked(self):
        try:
            self.product_controller.remove_product(self.product_controller.find_product_by_id(
                int(self.id_delete_entry.get())
            ))

            if self.checked.get():
                self.update_scroll_text()

        except Exception as e:
            messagebox.showerror("Error", e.args[0])

    def search_by_department_button_clicked(self):
        try:
            text = self.product_controller.list_to_string(self.product_controller.get_products_list_from_department(
                self.department_search_entry.get()
            ))

            if self.checked.get():
                self.update_scroll_text_by(text)

        except Exception as e:
            messagebox.showerror("Error", e.args[0])

    def create_file(self):
        self.save_as()

    def open_file(self):
        self.filepath = filedialog.askopenfilename()

        if self.filepath == '':
            return

        self.master.title = self.filepath

        try:
            self.product_controller.load(self.filepath)
            self.update_scroll_text()
        except Exception as e:
            self.show_error_dialog(e.args[0])

    def save(self):
        if self.filepath == '':
            self.save_as()
        else:
            self.product_controller.save(self.filepath)

    def save_as(self):
        self.filepath = filedialog.asksaveasfilename()

        if self.filepath == '':
            return

        self.master.title = self.filepath

        try:
            self.product_controller.save(self.filepath)
        except Exception as e:
            self.show_error_dialog(e.args[0])

    def quit(self):
        res = messagebox.askyesno("Quit", "Are you sure? all the unsaved data will be lost.")
        if res is False:
            return

        exit(0)

    def show_about(self):
        tk.messagebox.showinfo("About", "Programmer - Andrei Bikov")

    def show_error_dialog(self, message):
        tk.messagebox.showerror("Error", message)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Products")
    app = MainWindow(root)
    root.mainloop()
