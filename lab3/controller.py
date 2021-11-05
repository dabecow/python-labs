import pickle


class ProductController:
    __products_list = []

    def add_product(self, product):
        self.__products_list.append(product)

    def remove_product(self, product):
        self.__products_list.remove(product)

    def list_to_string(self, products_list):
        string = str()

        for product in products_list:
            string += product.__str__() + '\n'

        return string

    def main_list_to_string(self):
        return self.list_to_string(self.__products_list)

    def find_product_by_id(self, local_id):
        try:
            return filter(lambda product: product.id == local_id, self.__products_list).__next__()
        except Exception:
            raise Exception("No product with such id")

    def get_products_list_from_department(self, department):
        return list(filter(lambda product: product.department == department, self.__products_list))

    def save(self, path):
        with open(path, "wb") as f:
            pickle.dump(self.__products_list, f)

    def load(self, path):
        with open(path, "rb") as f:
            self.__products_list = pickle.load(f)
