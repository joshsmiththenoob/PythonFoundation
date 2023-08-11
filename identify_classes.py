'''

Truly identify Classes by Problem Statment
藉由問題描述中的名詞來定義Class

問題描述例子 A Fast food shop system

Bank : 



class命名規則 : CamelCase 駝峰式大寫，且為單數

'''

import time

class House:
    def __init__(self, color: str, size: int) -> None: # 初始化方法(Method) : 在建立新物件時，就定義這個物件的特性(包括屬性、或直接執行什麼樣的事情(函式 or 方法))
        self.items = []
        self.color = color
        self.size = size
        print(f'{color}\'s House building....')
        time.sleep(5)
        print(f'{color}\'s House builded!')


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius
        

class Retangle:
    def __init__(self, length: float, width:float) -> None:
        self.length = length
        self.width = width


class Movie:
    def __init__(self, title, year, language, rating) -> None:
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

a = House('Red', 200)
b = House('Blue', 300)
