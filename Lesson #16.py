#Serhii Vysochyn
#1

class Persone():
    def __init__(self, first_name: str, last_name: str, age: int,):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Student(Persone):
    def __init__(self, first_name: str, last_name: str, age: int, group: str):
        super().__init__(first_name, last_name, age)
        self.group = group

    def next_group(self, school_group=1):
        self.group += school_group


class Teacher(Persone):
    def __init__(self, first_name: str, last_name: str, age: int, salary: int):
        super().__init__(first_name, last_name, age)
        self.salary = salary

    def salary_bonus(self, bonus_plas=50):
        self.salary += bonus_plas

    def no_bonus(self, bonus_plas=50):
        self.salary -= bonus_plas


some_teacher = Teacher('Kiano','Rivz', 50, 200)
print(some_teacher.salary)
some_teacher.salary_bonus()
print(some_teacher.salary)

some_student = Student('Serg', 'Jo', 16, 4)
print(some_student.group)
some_student.next_group()
print(some_student.group)

#2

class Mathematican():
    pass

class Square(Mathematican):
    def __init__(self, squares: list):
        self.squares = squares
        self.squares = [i**2 for i in squares]


class Positives(Mathematican):
    def __init__(self, positives: list):
        self.positives = positives
        self.positives = list(filter(lambda x: x > 0, positives))

class Leaps(Mathematican):
    def __init__(self, leap_years: list):
        self.leap_years = leap_years
        #self.leap_years =

m = Square([7, 11, 5])
print(m.squares)
n = Positives([4, -4, 2, -3, 8, 7])
print(n.positives)

#3

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self, products):
        self.products = products
        self.income = 0

    def add(self, product, amount):
        self.products.append((product, amount))
        self.price = product.price * 1.3

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product in self.products:
            if identifier_type == 'name' and product[0].name == identifier:
                product[0].price = product[0].price * (1 - percent/100)
            elif identifier_type == 'type' and product[0].type == identifier:
                product[0].price = product[0].price * (1 - percent/100)

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product[0].name == product_name:
                if product[1] >= amount:
                    product[1] -= amount
                    self.income += product[0].price * amount
                    return
                else:
                    raise ValueError('Not enough items in the store')
        raise ValueError('Product not found')

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        for product in self.products:
            if product[0].name == product_name:
                return (product[0].name, product[1])
        raise ValueError('Product not found')

p = Product('sport', 't-short', 50)
p2 = Product('food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen')
