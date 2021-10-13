from model import Product
from controller import ProductController

MENU = "1. Add product\n2. Delete product\n3. Print products list\n4. Print products list from the department\n>>>"
product_controller = ProductController()

if __name__ == '__main__':

    while True:
        try:
            choice = input(MENU)
            if choice == '1':
                product_controller.add_product(
                    product=Product(
                        int(input("Enter the id value\n>")),
                        str(input("Enter the name value\n>")),
                        str(input("Enter the department name value\n>")),
                        str(input("Enter the price value\n>")),
                        str(input("Enter the description value\n>"))
                    )
                )
            elif choice == '2':
                product_controller.remove_product(product_controller.find_product_by_id(
                    int(input("Enter the id value\n>"))
                ))
            elif choice == '3':
                print(product_controller.main_list_to_string())
            elif choice == '4':
                print(product_controller.list_to_string(
                    product_controller.get_products_list_from_department(
                        str(input("Enter the department name value\n>"))
                    )))
            elif choice.lower() == 'q':
                exit(0)

        except Exception as e:
            print(e.args[0])
