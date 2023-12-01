class Tire:    
    def __init__(self,size,createDate):
        self.size  =  size  # 尺寸
        self.createDate = createDate # 出厂日期

class BenzCar:     
    brand   = '奔驰'  
    country = '德国'  

    @staticmethod
    def pressHorn(): 
        print('嘟嘟~~~~~~')

    def __init__(self,color,engineSN,tires):
        self.color  =  color     # 颜色
        self.engineSN = engineSN # 发动机编号
        self.tires = tires         #轮胎
    
    def changeColor(self,newColor):
        self.color = newColor

class Benz2016(BenzCar):
    price   = 580000
    model   = 'Benz2016'   


class Benz2018(BenzCar):
    price   = 880000
    model   = 'Benz2018'

    def __init__(self, color, engineSN,tires,weight):
        super().__init__(color, engineSN,tires)
        self.weight = weight

tires = [Tire(20,'2020-9-1') for i in range(4)]
car1 = Benz2016('红色','123',tires)
print(f"car1的所有属性和方法:{dir(car1)}")
car2 = Benz2018('黄色','456',tires,100)
print(f"动态获取car1的颜色属性:{getattr(car1,'color')}")
print(f"动态判断car1是否有name属性:{hasattr(car1,'name')}")
print(f"返回对象的内存地址：{id(car1)}")
print(f"判断car1是否是BenzCar的实例：{isinstance(car1,BenzCar)}")
print(f"判断car1的类是否为BenzCar的子类：{issubclass(car1.__class__,BenzCar)}")
print(f"car1的颜色是{car1.color}")
print(f"car1的价格是{car1.price}")
print(f"car2的颜色是{car2.color}")
print(f"car2的价格是{car2.price}")
print(f"car2的轮胎出厂日期是{car2.tires[0].createDate}")

car1.changeColor('黄色')
print(f"car1的颜色是{car1.color}")
print(f"car2的重量是{car2.weight}")
