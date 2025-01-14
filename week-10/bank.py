class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    def updatePrice(self, amount):
        self.__price = amount
        return self.__price

    def addStock(self, amount):
        if amount > 0:
            self.__stock += amount
        else:
            print("ไม่สามารถเพิ่มสินค้าได้")

    def discountStock(self, amount):
        if amount > 0 and amount <= self.__stock:
            self.__stock -= amount
        else:
            print("ไม่สามารถลดสินค้าได้")

    def checkProduct(self):
        return f"ชื่อ : {self.name}\nราคาสินค้า : {self.__price}\nจำนวนสินค้า : {self.__stock}"

product1 = Product("kong", 2550, 8)
product1.updatePrice(1750) 
product1.addStock(7) 
product1.discountStock(4)  

print(product1.checkProduct())