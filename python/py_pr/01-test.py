class Bag:
    def __init__(self,new_space,new_name):
        self.space = new_space
        self.left_space = new_space
        self.name = new_name
        self.contain_items = []

    def __str__(self):
        return "%s的总容量是%d,装有物品%s,剩余容量%d"%(self.name,self.space,str(self.contain_items),self.left_space)

    def add_item(self,item):
        self.left_space -= item.space
        #self.contain_items.append(item.name)
        #self.contain_items.append(item.color)
        self.contain_items.append(item.infor)

class Wp:
    def __init__(self,new_name,new_color,new_brand,new_space):
    #def __init__(self,new_name,new_color,new_space):
        self.name = new_name
        self.color = new_color
        self.brand = new_brand
        self.space = new_space
        self.infor = {}
        self.infor["name"] = self.name
        self.infor["color"] = self.color
        self.infor["brand"] = self.brand
        self.infor["space"] = self.space
    def __str__(self):
        return "%s占用的容量是%d,颜色是%s,品牌是%s"%(self.name,self.space,self.color,self.brand)
        #return "%s占用的容量是%d 颜色是%s"%(self.name,self.space,self.color)



danjianb = Bag(10,"lv")
print(danjianb)

lipstick = Wp("口红","999","迪奥",1)
print(lipstick)

danjianb.add_item(lipstick)
print(danjianb)



