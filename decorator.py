"""Decoratorの練習."""
# coding: utf-8


class Ramen():
    """ラーメン."""

    def __init__(self):
        raise NotImplementedError()

    def get_name(self):
        """ラーメンの名前."""
        raise NotImplementedError()

    def how_much(self):
        """ラーメンの値段."""
        raise NotImplementedError()


class JiroRamen(Ramen):
    """次郎のラーメン."""

    def __init__(self, name="ラーメン", price=500):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def how_much(self):
        return self.price


class AburaJiroRamen(JiroRamen):
    """トッピング次郎のラーメン."""

    def __init__(self, name="ラーメン", price=500):
        self.ramen = JiroRamen(name, price)
        self.nin_niku = 0
        self.yasai = 0

    def get_name(self):
        nin_niku = "ニンニク" * (self.nin_niku > 0) + "マシ" * self.nin_niku
        yasai = "ヤサイ" * (self.yasai > 0) + "マシ" * self.yasai
        return nin_niku + yasai + self.ramen.get_name()

    def how_much(self):
        return self.ramen.how_much()

    def add_nin_niku(self, mashi=1):
        self.nin_niku += mashi
     
    def add_yasai(self, mashi=1):
        self.yasai += mashi
    

class CupNoodle(Ramen):
    """カップラーメン."""

    def __init__(self, name="カップヌードル", price=150):
        self.name = name
        self.price = price
        self.wait_time = 0

    def get_name(self):
        self.wait_a_minutue()
        return "お湯を入れて" + str(self.wait_time) + "分の" + self.name

    def how_much(self):
        return self.price

    def wait_a_minutue(self):
        """."""
        self.wait_time += 1

if __name__ == '__main__':
    j = JiroRamen()
    print(j.get_name(), j.how_much())

    a = AburaJiroRamen(name="クロダそば", price="399")
    print(a.get_name(), a.how_much())
    a.add_nin_niku(4)
    a.add_yasai(3)
    print(a.get_name(), a.how_much())

    c = CupNoodle()
    print(c.get_name(), c.how_much())
    print(c.get_name(), c.how_much())
    print(c.get_name(), c.how_much())
    print(c.get_name(), c.how_much())
