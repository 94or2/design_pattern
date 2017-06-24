"""FactoryMethodの練習."""
# coding: utf-8


class Worker():
    """社畜."""

    def __init__(self, name="ななし"):
        self.name = name

    def get_name(self):
        return self.name

    def work(self):
        return self.name + "は働いています."


class Reader(Worker):
    """中間管理職."""

    def order(self, worker_name="ななし"):
        if worker_name is None:
            return self.name + "は働いています"
        return self.name + "は" + worker_name + "に指示をだします."


class Engineer(Worker):
    """エンジニア."""

    def work(self):
        return self.name + "はプログラムを書いています."


class Sales(Worker):
    """営業."""

    def work(self):
        return self.name + "は営業にでかけています."


class PC():
    """パソコン."""

    def __init__(self, name="WindowsPC"):
        self.on_use = False

    def run(self):
        return self.name + "は正常に稼働中です."


class Group():
    """グループ."""

    def __init__(self):
        self.engineers = []
        self.sales = []
        self.PCs = []

    def add_group_name(self, group_name):
        self.group_name = group_name

    def add_reader(self, reader):
        self.reader = reader

    def add_engineers(self, engineers):
        self.engineers = engineers

    def add_sales(self, sales):
        self.sales = sales

    def add_PCs(self, PCs):
        self.PCs = PCs

    def get_info(self):
        return self.group_name + "：リーダーは" + self.reader.get_name()


class GroupFactory():
    """グループを作る抽象クラス."""

    def get_reader(self):
        raise NotImplementedError()

    def get_engineers(self):
        raise NotImplementedError()

    def get_sales(self):
        raise NotImplementedError()

    def get_PCs(self):
        raise NotImplementedError()


class TeamJKFactory(GroupFactory):
    """チームJKを作る."""

    def get_group_name(self):
        return "チームJK"

    def get_reader(self):
        return Reader(name="上甲")

    def get_engineers(self):
        return [Engineer(name) for name in ["金平", "北村", "合田"]]

    def get_sales(self):
        return None

    def get_PCs(self):
        return [PC("VAIO")] * 4


class TeamJSFactory(GroupFactory):
    """チームJSを作る."""

    def get_group_name(self):
        return "チームJS"

    def get_reader(self):
        return Reader(name="黒田")

    def get_engineers(self):
        return [Engineer(name) for name in ["小村", "多田", "山口"]]

    def get_sales(self):
        return None

    def get_PCs(self):
        return [PC("VAIO")] * 4


class ShinsotsuFactory(GroupFactory):
    """１７新卒を作る."""

    def get_group_name(self):
        return "17新卒"

    def get_reader(self):
        return Reader(name="木村")

    def get_engineers(self):
        return [Engineer(name) for name
                in ["黒田", "小村", "多田", "山口", "上甲", "金平", "北村", "合田"]]

    def get_sales(self):
        return [Sales(name) for name
                in ["太田", "井樋", "工藤", "松野"]]

    def get_PCs(self):
        return [PC("VAIO")] * 8 + [PC("Surface")] * 5


class E_seikatsu():
    """実際にグループを作るとき使うクラス."""

    def __init__(self, group_name="チームななし"):
        group = Group()
        factory = self.createFactory(group_name)
        group.add_group_name(factory.get_group_name())
        group.add_reader(factory.get_reader())
        group.add_engineers(factory.get_engineers())
        group.add_sales(factory.get_sales())
        group.add_PCs(factory.get_PCs())
        self.group = group

    def createFactory(self, group_name):
        if group_name == "チームJK":
            return TeamJKFactory()
        if group_name == "チームJS":
            return TeamJSFactory()
        if group_name == "17新卒":
            return ShinsotsuFactory()

        print("定義されていないチーム名です.")
        return None


if __name__ == '__main__':
    jk = E_seikatsu("チームJK")
    print(jk.group.get_info())
    shisotsu17 = E_seikatsu("17新卒")
    print(shisotsu17.group.get_info())
