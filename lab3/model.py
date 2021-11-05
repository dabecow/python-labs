class Product:
    __id = int()
    __name = str()
    __department = str()
    __price = float()
    __description = str()

    # def __init__(self, id, name, department, price, description):
    #     self.__id = id
    #     self.__name = name
    #     self.__department = department
    #     self.__price = price
    #     self.__description = description

    def __init__(self, **kwargs):
        self.__id = kwargs.get("id")
        self.__name = kwargs.get("name")
        self.__department = kwargs.get("department")
        self.__price = kwargs.get("price")
        self.__description = kwargs.get("description")


    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def department(self):
        return self.__department

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    def __str__(self) -> str:
        return '{:>3}|{:>15}|{:>6}|{:>10}|{:>10}'\
            .format(self.__id, self.__name, self.__price, self.__department, self.__description)

