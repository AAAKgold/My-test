class SweetPotato:
    """定义一个地瓜类"""
    def __init__(self):
        self.cookString = "生的"
        self.cookLevel = 0
        self.condiments = []#用来保存添加的佐料

    def __str__(self):
        return "地瓜的状态是%s(%d),添加的佐料有%s"%(self.cookString,self.cookLevel,str(self.condiments)) 

    def cook(self,cookTime):

        self.cookLevel += cookTime

        if self.cookLevel >= 0 and self.cookLevel < 3:
            self.cookString = "生的"
        elif self.cookLevel >= 3 and self.cookLevel < 6:
            self.cookString = "半生不熟"
        elif self.cookLevel >= 6 and self.cookLevel < 9:
            self.cookString = "熟透了"
        elif self.cookLevel >= 9:
            self.cookString = "烤糊了"

    def addCondiments(self,item):
        self.condiments.append(item)


di_gua = SweetPotato()
print(di_gua)

di_gua.cook(1)
print(di_gua)

di_gua.addCondiments("洋葱")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("大蒜")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("韭菜")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("番茄汁")
di_gua.cook(1)
print(di_gua)

