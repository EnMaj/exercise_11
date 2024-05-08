import dictionary_test_2 as dictionary


class Product:

    def __init__(self, barcode, price):
        self.__price = price
        self.__barcode = barcode
        '''
        self.__country = barcode[:3]
        self.__manufacture = barcode[3:7]
        self.__cod_product = barcode[7:12]
        '''

        if self.__barcode[:2] in dictionary.country.keys():
            self.__country = self.__barcode[:2]
        elif self.__barcode[:3] in dictionary.country.keys():
            self.__country = self.__barcode[:3]

        if self.__barcode[len(self.__country):6] in dictionary.manufacture.keys():
            self.__manufacture = self.__barcode[len(self.__country):6]
        elif self.__barcode[len(self.__country):7] in dictionary.manufacture.keys():
            self.__manufacture = self.__barcode[len(self.__country):7]

        self.__cod_product = self.__barcode[len(self.__country) + len(self.__manufacture):
                                            len(self.__manufacture) + 8]

    @property
    def country(self):
        return dictionary.country[self.__country]

    @country.setter
    def country(self, country):
        pass

    @property
    def manufacture(self):
        return dictionary.manufacture[self.__manufacture]

    @manufacture.setter
    def manufacture(self, manufacture):
        pass

    @property
    def product(self):
        return dictionary.product[self.__cod_product]

    @product.setter
    def product(self, product):
        pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        pass

    @property
    def barcode(self):
        return self.__barcode

    @barcode.setter
    def barcode(self, barcode):
        pass


class Basket:

    def __init__(self):
        self.__basket = []
        self.__total_cost = 0

    def add_product(self, product, basket_file):
        self.__basket.append(product)
        basket_file.write(str(product.barcode) + product.product + str(product.price) + '\n')

    def del_product(self, product, basket_file):
        self.__basket.remove(product)
        lines = basket_file.readlines()
        for line in lines:
            barcode, product, price = line.split()
            if barcode != product.barcode:
                basket_file.write(line)

    def print_basket(self):
        for elem in self.__basket:
            print(f'{elem.barcode} {elem.product} {elem.price} \n')


set_product = []
with open('product.txt', 'r') as product_file:
    for goods in product_file:
        barcode, price = goods.split()
        set_product.append(Product(barcode, int(price)))

basket = Basket()
with open('basket.txt', 'w+') as basket_file:
    basket.add_product(set_product[0], basket_file)
    basket.add_product(set_product[1], basket_file)
    basket.del_product(set_product[0], basket_file)

basket.print_basket()
