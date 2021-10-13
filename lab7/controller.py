from model import *


def add_product(product):
    product.save()


def remove_product(product):
    product.delete_instance()


def list_to_string(products_list):
    string = str()

    for product in products_list:
        string += product.__str__() + '\n'

    return string


def main_list_to_string():
    return list_to_string(Product.select().execute())


def find_product_by_id(local_id):
    try:
        return Product.select().where(Product.id == int(local_id)).get()
    except Exception:
        raise Exception("No product with such id")


def get_products_list_from_department(department_name):
    return Product.select().where(Product.department ==
                                                 Department.select().where(Department.name == department_name))


def get_departments_list():
    return list(Department.select())

def get_departments_names_list():
    return list(map(lambda department: department.name, Department.select()))

def get_department_by_name(name):
    return Department.select().where(Department.name == name).get()
