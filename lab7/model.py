from peewee import *

database = SqliteDatabase('products.db')


class BaseModel(Model):
    class Meta:
        database = database


class Department(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(unique=True)

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name


class Product(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    department = ForeignKeyField(Department, related_name="products")
    price = IntegerField()
    description = CharField()

    def __init__(self, name, department, price, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.department = department
        self.price = price
        self.description = description

    def __str__(self) -> str:
        return '{:>3}|{:>15}|{:>6}|{:>10}|{:>10}' \
            .format(self.id, self.name, self.price, self.department.name, self.description)


Department.create_table()

Product.create_table()

if Department.select().count() == 0:
    milk_department = Department('Milk')
    meat_department = Department('Meat')
    bread_department = Department('Bread')
    milk_department.save()
    meat_department.save()
    bread_department.save()

#
# product = Product('test', department, 222, 'test')
# product.save()
